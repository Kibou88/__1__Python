# Opérations sur les sets
#
#---------------------------------------------------------
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = {1, 4, 7, 8}
"""
Union: Unir plusieurs sets en un seul
"""
print("Union:")
print(a.union(b))
print(a | b)
print(a.union(b, c))
print(a | b | c)
print()

"""
Intersection: Prends les éléments communs de plusieurs sets
"""
print("Intersection:")
print(a.intersection(b))
print(a & b)
print(a.intersection(b, c))
print(a & b & c)
print()

"""
Difference: Prends les éléments uniques d'un set avec plusieurs sets
"""
print("Difference:")
print(a.difference(b))
print(a - b)
print(a.difference(b, c))
print(a - b - c)
print()

"""
Difference symetrique: Prends les éléments uniques de chaque set
"""
print("Difference symetrique:")
print(a.symmetric_difference(b))
print(a ^ b)
print()

