from pathlib import Path

p = Path('.')

# Récupère le nom + extension du fichier
test = [x.name for x in p.iterdir() if (x.is_file() and x.suffix == ".jpg")]
files_found = [x for x in p.iterdir() if (x.is_file() and x.suffix == ".jpg")]
print(test)
print(files_found)
for file in files_found:
    print(file)