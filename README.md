# Pipeline BI sur Azure — NYC Taxi Analytics

> 🚧 **Work in progress** — ce projet est encore en cours de développement. Certains composants (pipelines, datasets, rapport Power BI) sont en cours de finalisation et ce README sera mis à jour au fur et à mesure.

## 📌 Vue d'ensemble

Ce projet vise à construire un pipeline **Business Intelligence de bout en bout sur Azure**, en s'appuyant sur le jeu de données public **NYC Taxi Trip**. L'objectif est d'ingérer les données brutes des courses de taxi, de les transformer via un pipeline de données, puis de les restituer dans un tableau de bord **Power BI** (demande de courses, revenus, moyens de paiement, etc.).

Le dépôt contient un projet **Azure Data Factory (ADF)** exporté via l'intégration Git (dossiers de type ARM), ainsi que les ressources associées (Data Lake, Azure SQL).

## 🗂️ Structure du dépôt

```
├── dataflow/         # Définitions des Data Flows (logique de transformation)
├── dataset/          # Définitions des datasets (schémas source/sink)
├── factory/          # Paramètres globaux de la Data Factory
├── linkedService/    # Linked Services (connexions ADLS, Azure SQL, etc.)
├── pipeline/         # Définitions des pipelines (orchestration)
├── publish_config.json
└── README.md
```

Cette organisation correspond à l'export standard d'Azure Data Factory lorsqu'il est connecté à un dépôt Git (Author → Git configuration).

## 🏗️ Architecture (cible)

```
NYC Taxi Data (raw)
        │
        ▼
Azure Data Factory  ──►  Azure Data Lake Storage Gen2 (Bronze / Silver / Gold)
        │
        ▼
      Azure SQL Database
        │
        ▼
     Power BI Dashboard
```

*Ce schéma reflète l'architecture cible visée. Tous les composants ne sont pas encore implémentés — voir [Statut](#-statut--todo) ci-dessous.*

## 🎯 Objectifs

- Ingérer les données brutes des courses de taxi NYC dans Azure Data Lake Storage Gen2
- Nettoyer et transformer les données via les Data Flows d'ADF (couches Bronze → Silver → Gold)
- Charger les données modélisées dans Azure SQL Database
- Construire un tableau de bord Power BI permettant d'explorer :
  - Les tendances de demande et de volume de courses
  - Les revenus par période / zone
  - La répartition des moyens de paiement
  - Les schémas de prise en charge / dépose par borough

## ✅ Statut / TODO

- [x] Ressources Data Factory initiales créées (linked services, datasets, squelettes de pipelines)
- [ ] Finaliser le pipeline d'ingestion (données brutes → Data Lake)
- [ ] Construire les transformations Data Flow (nettoyage, enrichissement)
- [ ] Mettre en place la structure des couches Bronze / Silver / Gold
- [ ] Connecter la couche de service Azure SQL
- [ ] Construire et publier le rapport Power BI
- [ ] Ajouter les instructions de déploiement / configuration
- [ ] Ajouter un échantillon de données ou un lien vers le dataset source

## 🔧 Prérequis (une fois terminé)

- Un abonnement Azure
- Une instance Azure Data Factory
- Un compte Azure Data Lake Storage Gen2
- Azure SQL Database
- Power BI Desktop / Power BI Service

## 🚀 Démarrage

> Les étapes détaillées seront ajoutées une fois le pipeline finalisé.

1. Cloner ce dépôt
2. Connecter le dépôt à une instance Azure Data Factory via **l'intégration Git**
3. Mettre à jour les chaînes de connexion des `linkedService` pour pointer vers votre propre stockage/base de données
4. Publier les ressources de la factory
5. Déclencher le pipeline manuellement ou via une planification

## 📊 Source des données

Ce projet utilise les données publiques **NYC Taxi & Limousine Commission (TLC) Trip Record Data**, publiées par NYC.gov.

## 🤝 Contribution

Ceci est un projet personnel d'apprentissage, encore en développement actif. Suggestions et retours bienvenus via les Issues.

## 📄 Licence

_Aucune licence spécifiée pour le moment._