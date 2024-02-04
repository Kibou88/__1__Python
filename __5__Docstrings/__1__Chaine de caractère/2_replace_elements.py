# Manipuler les chaines de caractères part 2
# - Remplacer des éléments d'une chaine
##########################################

def string_replace_1_element(test,element_removed_1, element_added_1):
    """Fonction pour modifier un élément de la chaîne"""
    test = test.replace(element_removed_1, element_added_1)
    print("L'élément {} a été modifié par l'élément {}".format(element_removed_1, element_added_1))
    print("Nouvelle chaîne: ", test)
    print("")

def string_replace_2_elements(test, element_removed_1, element_added_1, element_removed_2, element_added_2):
    """Fonction pour modifier 2 éléments de la chaîne"""
    test=test.replace(element_removed_1, element_added_1).replace(element_removed_2, element_added_2)
    print("Les éléments {0} et {1} ont été retirés et les éléments {2} et {3} ont été ajoutés"
          .format(element_removed_1, element_removed_2, element_added_1, element_removed_2))
    print("Nouvelle chaîne: ", test)

if __name__ == "__main__":
    test = "Bonjour tout le monde"
    print("Chaîne de base: ", test)
    print("")
    element_removed_1 = "jour"
    element_removed_2 = " "
    element_added_1 = "soir"
    element_added_2 = ""

    string_replace_1_element(test, element_removed_1, element_added_1)
    string_replace_2_elements(test, element_removed_1, element_added_1, element_removed_2, element_added_2)