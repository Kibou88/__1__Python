import json

fichier_json = "data.json"

with open(fichier_json,"r") as f:
    data = json.load(f)
print(data["first_name"])