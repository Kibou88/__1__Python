# Modules dir et __doc__
# - Apprendre à utiliser les modules dir et __doc__
#----------------------------------------
import os
from pprint import pprint
"""
dir va lister toutes les méthodes/attributs
"""
# pprint(dir(os))
pprint(dir(list))

"""
__doc__ va récupérer les informations du docstring (ressemble à Help)
"""
print([].__doc__)
print([].remove.__doc__)