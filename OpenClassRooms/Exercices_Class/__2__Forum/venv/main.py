from Classes import *

if __name__ in "__main__":
    user = User("Toto", "123Soleil") # Instancie un utilisateur
    moderator = Moderator("Super", "Super123") # Instancie un modérateur

    user.login() # L'utilisateur se connecte
    content = "Exercice de muscu" # Contenu du post

    cake_thread = user.make_thread("Cake", "Vous aimez")
    cake_thread.display()

    moderator.post(cake_thread, content="oui")
    cake_thread.display()

    irrevelant_post = user.post(cake_thread, content="Football")
    cake_thread.display()

    moderator.post(cake_thread, content="Votre post est HS, je le supprime")
    moderator.delete(cake_thread, irrevelant_post)
    cake_thread.display()

    image = ImageFile(name="Fuck", size=3)
    user.post(cake_thread, content="Voilà une image", file=image)
    cake_thread.display()