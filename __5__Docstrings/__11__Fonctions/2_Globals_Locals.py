# Fonctions Globals et Locals
# - Apprendre l'utilité de ces 2 fonctions
##########################################

def foo(): #Toutes variables déclarées dans la fonction est en local
    b=10
    print("Globals dans la fonction: \n", globals())
    print("Locals dans la fonction: \n", locals())
    print(c+b)

a=5
c=15
print("Globals: \n", globals())
print("Locals: \n", locals())
foo()
