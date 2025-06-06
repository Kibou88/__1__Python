# main.py
# ------------------------------------------------------------------
# But:
# Contient la logique du programme
# ------------------------------------------------------------------
# Date de création: 2025-06-03
# Date de modification: 2025-06-03
# ------------------------------------------------------------------
# Version: V1.0

import requests
import sys
import time
from constantes import *

page = requests.get(URL)

if page.status_code != 200:
    print("La page demandee n'est pas accessible")
    time.sleep(3)
    sys.exit()

