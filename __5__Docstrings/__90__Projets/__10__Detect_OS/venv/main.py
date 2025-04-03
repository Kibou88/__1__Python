# main.py
# But:
# Contient la logique du code
# -----------------------------------
# Date de création: 2025-03-04
# Date de dernière modification: 2025-03-04
# ------------------------------------------
# version: 1.0

#-----------------------------------------------------------------------------------

import platform

class OS_type():
    def __init__(self):
        self.os_name = platform.system()
    def type_platform(self):
        if self.os_name == "Windows":
            print("Je suis sous Windows")
        elif self.os_name == "Linux":
            print("Je suis sous Linux")

if __name__ == "__main__":
    OS_type().type_platform()