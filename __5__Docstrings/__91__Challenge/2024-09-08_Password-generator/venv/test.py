from pathlib import Path

file_mots = Path.cwd() / "input" / "mots.txt"

with open(file_mots, "r", encoding='utf-8') as f:
    lignes = f.read().split(" ")
