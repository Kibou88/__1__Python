import re

adresses_mail = ['christian_martin@gmail.com',
				 'JaiOublieLarobasegmail.com',
				 'MarieHutchinson03523@yahoo.co.uk',
				 'UnEaDreSSeMail!38BIZarre@unSiTeBizarre.com',
				 'ceciNestPasUneDresseMail']

# L'adresse christian_martin@gmail.com est valide
# L'adresse JaiOublieLarobasegmail.com est invalide
# L'adresse MarieHutchinson03523@yahoo.co.uk est valide
# L'adresse UnEaDreSSeMail!38BIZarre@unSiTeBizarre.com est valide
# L'adresse ceciNestPasUneDresseMail est invalide

for mail in adresses_mail:
	match = re.match(r'(.+@\w+)', mail)
	print (f"l'adresse {mail} est {'valide' if match != None else 'invalide'}")