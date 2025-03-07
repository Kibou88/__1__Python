# Module Sys
# - Apprendre à utiliser le module Sys
#----------------------------------------
"""
Permet d'identifier le système sur lequel se lance le programme
"""

import sys

print(sys.version)
print(sys.version_info.major)
print(sys.version_info.minor)
print(sys.platform)
print(sys.path)
print(sys.getwindowsversion().major)
print(sys.executable)
print(sys.argv)