"""
Pour chaque question, indiquez si le match est valide ou non et ce qu'il retourne.
Questions pour cet exercice
"""
import re
a = re.match(r'[a-z]+\d{2}', 'item01') # Valide: item01
print(a) # OK

b = re.match(r'[a-zA-Z]+\s\w+', 'Pierre Dupont') # Valide: Pierre Dupont
print(b) # OK

c = re.match(r'\s+', 'pierre dupont') # Faux
print(c) # OK

d = re.match(r'\w+', 'pierre dupont') # Valide: pierre
print(d) # OK

e = re.match(r'\w+([-+=]?)', 'pierre-dupont') # Valide: pierre-dupont
print(e) # KO: pierre-

f = re.match(r'\w+([-+=]?)', 'pierre/dupont') # Faux
print(f) # KO: pierre

g = re.match(r'\w+([-+=]+)', 'pierre/dupont') # Faux
print(g) # OK