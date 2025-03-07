# Différence entre is et ==
# - Faire la différence is et ==
##########################################

print("== : teste la correspondance entre les valeurs de 2 variables")
print("is : teste la correspondance entre les espaces en mémoire des variables")
a=[1,2,3]
b=[1,2,3]

print(a==b) # Retourne True
print(a is b) # Retourne False
print(id(a))
print(id(b))

c = 50 #Singleton
d = 50 #Singleton => même espace en mémoire
print(c==d) # Retourne True
print(c is d) # Retourne True