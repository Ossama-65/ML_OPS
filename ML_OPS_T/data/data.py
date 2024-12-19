import pandas as pd

# Exemple de données fictives
data = {
    'feature1': [1, 2, 3, 4, 5],
    'feature2': [10, 20, 30, 40, 50],
    'specie': [0, 1, 0, 1, 0]
}
df = pd.DataFrame(data)

# Enregistrer le fichier CSV
df.to_csv('processed_data.csv', index=False)
print("Fichier processed_data.csv créé !")
