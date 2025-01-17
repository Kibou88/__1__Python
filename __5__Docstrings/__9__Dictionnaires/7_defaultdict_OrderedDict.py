# defaultdict et OrderedDict
# - Apprendre à utiliser defaultdict et OrderedDict
#-------------------------------------------------------
mot = 'anticonstitutionnellement'

d = {}
for lettre in mot:
    if not d.get(lettre):
        d[lettre] = 1
    else:
        d[lettre] += 1

print(d.items())

from collections import defaultdict

d1 = defaultdict(int)
for lettre in mot:
    d1[lettre] += 1
print(d1.items())
#----------------------------------------------
#------Python 3.11 or older plus besoin de l'utiliser-----
from collections import OrderedDict

mon_dict = {}
# mon_dict2 = OrderedDict()

mon_dict['Un'] = 'Pierre'
mon_dict['Deux'] = 'Paul'
mon_dict['Trois'] = 'Marie'
mon_dict['Quatre'] = 'Julien'
mon_dict['Cinq'] = 'Jules'

print(mon_dict.items())