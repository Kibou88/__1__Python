import os
def concatenation_chemin(base, *args):
	return os.path.normpath(base + "/" + "/".join(args))

chemin_complet = concatenation_chemin('C:/Utilisateurs', 'ThibH', 'Images')
print(chemin_complet)