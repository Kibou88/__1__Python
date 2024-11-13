# main.py
# But:
# Contient la logique du code
# -----------------------------------
# Date de création: 2024-11-13
# Date de dernière modification: 2024-11-13
# ------------------------------------------
# version: 1.0

#-----------------------------------------------------------------------------------

# Appel des librairies externes
from time import perf_counter, sleep, time


class Chrono():
    """

    """

    def __init__(self):
        self.timelaps = 0
        self.timestop = 0


    def start(self):
        self.timelaps = perf_counter()

    def stop(self):
        self.timestop = perf_counter() - self.timelaps


    def reset(self):
        self.timelaps = 0

    def show(self):
        return f"{round(perf_counter() - self.timelaps, 2)}"

    def __repr__(self):
        return f"{round(self.timestop,2)}"

