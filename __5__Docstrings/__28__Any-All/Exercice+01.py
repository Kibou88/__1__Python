fichiers = ['C:/dossier_test/fichier01.jpg',
			'C:/dossier_test/fichier02.tif',
			'C:/dossier_test/fichier03.png',
			'C:/dossier_test/fichier04.jpg',
			'C:/dossier_test/fichier05.jpg']

au_moins_un_png = any(fichier.endswith(".jpg") for fichier in fichiers)
print(au_moins_un_png)
tous_des_jpg = all(fichier.endswith(".jpg") for fichier in fichiers)
print(tous_des_jpg)