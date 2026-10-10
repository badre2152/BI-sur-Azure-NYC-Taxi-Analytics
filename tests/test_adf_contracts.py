"""Static contract checks for the exported Azure Data Factory resources."""

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_resource(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class AdfContracts(unittest.TestCase):
    def test_data_flow_only_runs_after_successful_copy(self):
        pipeline = read_resource("pipeline/pl_web_to_raw.json")
        activities = pipeline["properties"]["activities"]
        copy = next(a for a in activities if a["type"] == "Copy")
        flows = [a for a in activities if a["type"] == "ExecuteDataFlow"]
        self.assertTrue(flows)
        for flow in flows:
            dependencies = flow["dependsOn"]
            self.assertTrue(any(
                dep["activity"] == copy["name"]
                and dep["dependencyConditions"] == ["Succeeded"]
                for dep in dependencies
            ))

    def test_trip_duration_subtracts_pickup_from_dropoff(self):
        flow = read_resource("dataflow/df_raw_to_curated.json")
        script = "\n".join(flow["properties"]["typeProperties"]["scriptLines"])
        self.assertIn(
            "trip_duration = tpep_dropoff_datetime - tpep_pickup_datetime",
            script,
        )
        self.assertNotIn(
            "trip_duration = tpep_pickup_datetime - tpep_dropoff_datetime",
            script,
        )

    def test_all_adf_resource_json_files_are_parseable(self):
        for directory in ("pipeline", "dataflow", "dataset", "linkedService", "factory"):
            for path in (ROOT / directory).glob("*.json"):
                with self.subTest(path=str(path)):
                    json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
