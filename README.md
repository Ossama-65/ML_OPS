# Documentation Complète et Approfondie du Projet MLOps

## Introduction 🌟

Bienvenue dans la documentation complète du projet MLOps. Ce projet vise à démontrer l'application pratique et systématique des meilleures pratiques en Machine Learning Operations (MLOps). En combinant des outils modernes comme Terraform, Ansible, Docker, et GitHub Actions, nous avons conçu une solution robuste pour la gestion, le déploiement et la surveillance des pipelines ML. 🌟 Notre objectif principal est de garantir la reproductibilité, la transparence et l'automatisation complète des processus, tout en répondant aux défis courants rencontrés dans les environnements ML industriels.

---

## Objectifs du Projet 🎯

1. **Infrastructure Cloud**  
   - Provisionnement et gestion des ressources AWS via Terraform.  
   - Configuration automatisée des serveurs avec Ansible.  

2. **Application ML**  
   - Développement d'un pipeline complet intégrant la transformation des données, l'entraînement et la prédiction.  
   - Suivi et gestion des modèles ML avec MLflow pour le versioning et la traçabilité.  

3. **Pipeline CI/CD**  
   - Déploiement et intégration continus grâce à GitHub Actions.  

4. **Monitoring et Visualisation**  
   - Collecte de métriques et surveillance en temps réel via Prometheus et Grafana.  

5. **Documentation et Collaboration**  
   - Documentation détaillée couvrant chaque composant et étape du projet.  
   - Explications des choix techniques et adoption des meilleures pratiques.  

---

## Contexte du Projet 🌍

Avec la montée en puissance du Machine Learning dans divers secteurs, les défis liés à la mise à l'échelle, à la maintenabilité et au déploiement continu des modèles ML sont devenus critiques. Ce projet vise à répondre à ces défis en :

- **Standardisant** le développement des pipelines ML.  
- **Facilitant** la collaboration entre équipes interfonctionnelles.  
- **Réduisant** les erreurs humaines grâce à l'automatisation des processus critiques.

Les entreprises adoptant des approches MLOps comme celle-ci bénéficient d'une augmentation de leur efficacité et d'une meilleure reproductibilité des résultats ML. 🌐

---

## Architecture Globale du Projet 🏗️

### Schéma d'Architecture

```
+-------------------+
| Utilisateur       |
+--------+----------+
         |
         v
+--------+----------+
| API Flask         |
+--------+----------+
         |
         v
+-------------------+
| Modèles ML        |
+-------------------+
         |
         v
+-------------------+
| Infrastructure    |
+-------------------+
```

### Composants Clés

1. **API Flask** : Une interface utilisateur pour interagir avec les modèles et effectuer des prédictions. 🌐
2. **Modèles ML** : Enregistrés, versionnés et gérés avec MLflow.  
3. **Infrastructure** : Déployée sur AWS via Terraform et configurée avec Ansible.  
4. **Monitoring** : Surveillance et alertes configurées grâce à Prometheus et Grafana.  

---

## Étapes de Déploiement 🛠️

### 1. Cloner le Dépôt
```bash
git clone https://github.com/Ossama-65/ML_OPS.git
cd ML_OPS
```

### 2. Provisionner l'Infrastructure
```bash
cd terraform
terraform init
terraform apply
```

### 3. Configurer les Serveurs
```bash
cd ansible
ansible-playbook -i inventory playbook.yml
```

### 4. Déployer le Monitoring
```bash
cd monitoring
sudo docker-compose up -d
```

Ces étapes garantissent que l'infrastructure, les configurations, et les outils de surveillance sont opérationnels avant de passer au développement et à l'utilisation des modèles ML. 🛡️

---

## Description des Modules 📂

### 1. **Dossier `src`**  
Ce dossier regroupe tout le code source relatif aux étapes du pipeline ML :

- `data/make_data.py` : Génération de données factices pour les tests.  
- `features/build_features.py` : Prétraitement et génération des caractéristiques.  
- `models/train_model.py` : Entraînement des modèles ML.  
- `models/predict.py` : Utilisation des modèles pour des prédictions.  
- `lib/utils.py` : Fonctions utilitaires partagées entre les scripts.

### 2. **Dossier `monitoring`**  
Inclut les configurations nécessaires pour la surveillance en temps réel :

- **Prometheus** : Fichier `prometheus.yml` pour la collecte des métriques.  
- **Grafana** : Dashboards définis dans `mlops_dashboard.json` et `infra_dashboard.json`.  

### 3. **Dossier `terraform`**  
Automatise le provisionnement des ressources cloud AWS :

- **S3** : Stockage des données et des modèles.  
- **EC2** : Exécution des scripts et des API.  
- **VPC** : Isolation sécurisée de l'environnement.

### 4. **Fichier `requirements.txt`**  
Spécifie les bibliothèques Python nécessaires au projet, garantissant la compatibilité et la portabilité. 📋

---

## API Documentation 🌐

### Endpoint `/predict`

- **Méthode** : `POST`  
- **Description** : Permet de soumettre des caractéristiques et de recevoir des prédictions.  
- **Exemple** :

#### Requête
```json
{
  "feature1": [1, 2, 3],
  "feature2": [10, 20, 30]
}
```

#### Réponse
```json
{
  "predictions": [0, 1, 0]
}
```

L'API est conçue pour une interopérabilité maximale et une expérience utilisateur fluide. 🚀

---

## CI/CD avec GitHub Actions 🤖

Chaque commit déclenche automatiquement :

1. **Tests Automatisés** : Analyse de la qualité du code et exécution des tests unitaires.  
2. **Build Docker** : Construction et validation des images Docker.  
3. **Déploiement** : Mise à jour automatique des modèles et de l'API en production.

L'intégration continue garantit que chaque modification respecte les normes de qualité définies pour le projet. 🔧

---

## Monitoring 🔍

### Prometheus

- Collecte les métriques des composants de l'infrastructure et des applications.  
- Génère des alertes configurées dans `alerts.rules.yml` en cas de défaillances ou de seuils critiques dépassés.

### Grafana

- Fournit des dashboards interactifs pour visualiser les données collectées :
  - **mlops_dashboard.json** : Suivi des indicateurs clés liés aux modèles ML.  
  - **infra_dashboard.json** : État de l'infrastructure cloud.  

Ces outils permettent de détecter rapidement les anomalies et d'assurer une disponibilité continue du système. 📊

---

## Résolution des Problèmes 🔧

1. **Erreur AWS CLI** : Assurez-vous que vos identifiants AWS sont correctement configurés dans `~/.aws/credentials`.  
2. **Échec du Terraform Apply** : Vérifiez les permissions associées à votre compte AWS.  
3. **Docker ne démarre pas** : Redémarrez le service Docker avec la commande `sudo systemctl restart docker`.  

Ces solutions couvrent les problèmes les plus courants rencontrés lors de la mise en œuvre de l'infrastructure et des outils.

---

## Auteurs 🧑‍🎓🧑‍🎓✍️

- Manel Zerguit : Responsable de l'intégration CI/CD.
- Ossama Louridi : Spécialiste en monitoring et infrastructure cloud.
- Aziz BenAyed : Développement des pipelines ML et API. 


Ce document a été conçu pour offrir une vue détaillée et pratique du projet MLOps. Il s'adresse à la fois aux débutants et aux experts souhaitant implémenter une solution ML complète et fiable.

