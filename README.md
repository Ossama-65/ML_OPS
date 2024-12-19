# Documentation avancée du Projet MLOps

## Introduction 📊🌐🚀
Ce projet explore le développement d'une chaîne complète MLOps qui fusionne les meilleures pratiques DevOps avec des outils spécialisés en Machine Learning. L'objectif est d'automatiser et d'optimiser le cycle de vie du Machine Learning en adoptant une méthodologie systématique fondée sur l'Infrastructure as Code (IaC) et des pipelines CI/CD robustes. L'intégration couvre l'infrastructure cloud, le versioning des modèles, le monitoring des performances et une documentation exhaustive pour garantir la reproductibilité et la transparence.

Ce projet met en avant des solutions adaptées aux défis courants du Machine Learning, notamment la gestion des versions des données et des modèles, le déploiement d'API fiables et le suivi en temps réel des métriques opérationnelles via des outils de monitoring avancés.

## Structure du Projet 📁🔄🏠

La structure de ce projet suit une architecture modulaire bien définie :

```
MLOps-END-TO-END/
├── .github/workflows
│   ├── ci-cd.yml
├── ansible/
│   ├── playbook.yml
├── data/
│   ├── processed_data.csv
├── monitoring/
│   ├── prometheus/
│   │   ├── prometheus.yml
│   │   ├── alerts.rules.yml
│   ├── grafana/
│       ├── datasources/datasource.yml
│       ├── dashboards/mlops_dashboard.json
│       ├── dashboards/infra_dashboard.json
├── notebooks/
│   └── analyses.ipynb
├── src/
│   ├── data/make_data.py
│   ├── features/build_features.py
│   ├── models/train_model.py
│   ├── models/predict.py
│   ├── lib/utils.py
├── terraform/
│   ├── main.tf
├── README.md
├── requirements.txt
├── test_app.py
```

Cette architecture est conçue pour faciliter le développement collaboratif et le déploiement à grande échelle.

## Installation et Configuration 🚀🌎⚙️

### Prérequis 🔧💡
Pour configurer et exécuter ce projet, assurez-vous d'avoir les éléments suivants :
- **Docker** : Pour conteneuriser les applications.
- **Terraform** : Pour provisionner l'infrastructure cloud.
- **Ansible** : Pour automatiser la configuration des serveurs.
- **AWS CLI** : Pour interagir avec les services AWS tels que S3.
- **Python 3.8+** : Avec `pip` pour la gestion des dépendances.

### Étapes d'installation 🛠️🌐

1. **Cloner le Repository** :
   ```bash
   git clone https://github.com/ton-repo/mlops-end-to-end.git
   cd mlops-end-to-end
   ```

2. **Configurer les Variables Terraform** :
   Modifiez `terraform/variables.tf` pour renseigner vos identifiants AWS et la région souhaitée.

3. **Provisionner l'Infrastructure** :
   ```bash
   cd terraform
   terraform init
   terraform apply
   ```

4. **Configurer les Serveurs avec Ansible** :
   ```bash
   cd ansible
   ansible-playbook -i inventory playbook.yml
   ```

5. **Déployer le Monitoring** :
   ```bash
   cd monitoring
   docker-compose up -d
   ```

6. **Installer les Dépendances Python** :
   ```bash
   pip install -r requirements.txt
   ```

7. **Lancer l'API Flask** :
   ```bash
   python3 src/app.py
   ```

## Utilisation 🔄📊🌐

### Pipeline ML

1. **Génération des Données** :
   ```bash
   python3 src/data/make_data.py
   ```

2. **Transformation des Données** :
   ```bash
   python3 src/features/build_features.py --environment prod
   ```

3. **Entraînement du Modèle** :
   ```bash
   python3 src/models/train_model.py --name my_model --environment prod
   ```

4. **Prédiction avec le Modèle** :
   ```bash
   python3 src/models/predict.py --name my_model --model latest --environment prod
   ```

### Monitoring 🖅⚙️⚡️

- Accéder à Grafana : `http://<IP_SERVEUR>:3000`
- Accéder à Prometheus : `http://<IP_SERVEUR>:9090`

### CI/CD avec GitHub Actions ⚓️⌛⚖️

Chaque push déclenche automatiquement les pipelines CI/CD définis dans `.github/workflows/ci-cd.yml`. Les étapes incluent :
- Tests automatisés.
- Construction des images Docker.
- Déploiement dans l'environnement de production.

## Documentation des APIs 🔍📊⚙️

### Endpoint : `/predict`
- **Méthode** : `POST`
- **Payload** :
  ```json
  {
    "feature1": [1, 2, 3],
    "feature2": [10, 20, 30]
  }
  ```
- **Réponse** :
  ```json
  {
    "predictions": [0, 1, 0]
  }
  ```

## Monitoring et Troubleshooting 🔧🛠️💡

### Visualisation des Metrics
Grafana et Prometheus permettent un suivi détaillé des performances de l'infrastructure et des modèles. Les dashboards sont configurés pour afficher les métriques essentielles :
- Temps de réponse des API.
- Disponibilité des services.
- Performances des modèles (ex. : précision, F1-score).

### Résolution des Problèmes Courants

1. **Erreur de connexion S3** :
   - Vérifiez que vos identifiants AWS sont correctement configurés dans `~/.aws/credentials`.
   - Assurez-vous que le bucket spécifié existe.

2. **Problème avec Docker** :
   - Redémarrez le service Docker :
     ```bash
     sudo systemctl restart docker
     ```

3. **Erreur Terraform** :
   - Vérifiez vos permissions AWS.
   - Supprimez les ressources conflictuelles avant de relancer `terraform apply`.

## Auteurs 🧑‍🎓🧑‍🎓✍️

- Manel Zerguit : Responsable de l'intégration CI/CD.
- Ossama Louridi : Spécialiste en monitoring et infrastructure cloud.
- Aziz BenAyed : Développement des pipelines ML et API.


