from abc import ABC

class File(ABC):
    """Class File
    CLASSE ABSTRAITE
    2 properties: name and size"""
    def __init__(self, name, size):
        self.name = name
        self.size = size
    def display(self):
        pass

class Image(File):
    """Class Image
    Parent: File"""

    def display(self):
        print("The file {} is displayed".format(self.name))
    pass

class ImageGIF(Image):
    """Class Image GIF
    Parent: Image"""
    def display(self):
        super().display()
        print("It's a GIF file")
        pass

class ImageJPG(Image):
    """Class Image JPG
    Parent: Image"""
    def display(self):
        super().display()
        print("It's a JPG file")
        pass

class User:
    """Class User

    2 properties: username and password"""
    def __init__(self, usernamne, password):
        self.username = usernamne
        self.password = password

    def login(self):
        print("Welcome {}!".format(self.username))

    def post(self, thread, content, file=none):
        # Méthode copier sur le corrigé de l'exercice
        # Poste un message dans un fil de discussion
        if file:
            post = Discussion(self, "aujourd'hui", content, file)
        else:
            post = Post(user=self, time_poste="aujourd'hui", content=content)
            thread.add_post(post)
        pass

    def make_thread(self, title, content):
        # Méthode copier sur le corrigé de l'exercice
        # Créé un nouveau fil de discussion
        post = Post(self, "aujourd'hui", content)
        return Thread(title, "aujourd'hui", post)

    def __str__(self):
        # Méthode copier sur le corrigé de l'exercice
        # représentation de l'utilisateur
        return self.username

class Moderator(User):
    """Class Moderator
    Parent: User"""
    def modify_post(self, post, content):
        # Méthode copier sur le corriger de l'exercice
        post.content = content
    def delete_post(self, thread, post):
        # Méthode copier sur le corriger de l'exercice
        index = thread.posts.index(post)
        del thread.posts[index]

class Post:
    """Class Post

    3 properties: content, user and publish_date"""
    def __init(self, content, user, publish_date):
        self.content = content
        self.user = user
        self.publish_date = publish_date

    def display(self):
        print("There is the post posted by {}, published the {} and it contains {}"
              .format(self.user, self.publish_date, self.content))

class Discussion(Post):
    """Class Discussion
    Parent: Post"""
    # Classe copier sur le corrigé de l'exercice
    def __init__(self, user, time_posted, content, file):
        """Initialise le fichier."""
        super().__init(user, time_posted, content)
        self.file = file

    def display(self):
        """Affiche le contenu et le fichier."""
        super().display()
        print("pièce jointe:")
        self.file.display()


class Thread:
    """Fil de discussions."""

    def __init__(self, title, time_posted, post):
        """Initialise le titre, la date et les posts.

        Attention ici: on commence par un seul post, celui du sujet.
        Les réponses à ce post ne pourrons s'ajouter qu'ultérieurement.
        En effet, on ne créé pas directement un nouveau fil avec des réponses. ;)
        """
        self.title = title
        self.time_posted = time_posted
        self.posts = [post]

    def display(self):
        print(f"There is the post {self.title}, posted the {self.time_posted}")
        # Partie copier sur le corrigé de l'exercice
        for post in self.posts:
            post.display()
            print()
        print("------------------")
    def add_post(self, post):
        # Méthode copier sur le corrigé de l'exercice
        self.posts.append(post)
        print("Well done, the post is added")