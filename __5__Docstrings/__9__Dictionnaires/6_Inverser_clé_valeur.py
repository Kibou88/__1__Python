# Inverser clé-valeur
#-----------------------

from pprint import pprint

LONG_NAMES = {'anm_scn': 'Animation Scene',
              'anm_out': 'Animation Publish',
              'sim_scn': 'Simulation Scene'}

pprint(list(zip(LONG_NAMES.values(), LONG_NAMES.keys())))
SHORT_NAMES = dict(zip(LONG_NAMES.values(), LONG_NAMES.keys()))