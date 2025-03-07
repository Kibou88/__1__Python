# Args et Kwargs
# - Apprendre à utiliser les args et kwargs
#-------------------------------------------
"""
Le plus important sont '*' et '**'.
Les noms 'args' et 'kwargs' sont des conventions
"""

def addition(a, b):
    return a + b

print(addition(5, 10))

"""
Si on veut passer autant d'éléments non nommés qu'on veut
"""
def additions(*args):
    return sum(args)

print(additions(5, 10, 15, 20))