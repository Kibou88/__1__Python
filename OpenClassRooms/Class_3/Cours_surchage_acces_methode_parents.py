class Drink:
    """classe Boisson"""
    def __int__(self, price):
        """Initialise le prix"""
        self.price = price

    def drink(self):
        """Boire la boisson"""
        print("Je ne sais pas ce que c'est mais c'est bon")

class Coffee(Drink):
    """classe Café"""
    prices = {"simple":1, "serré":1, "allongé":1.5}
    """Initialisation dico prices"""
    def __init__(self, type):
        """Initialise le prix du café"""
        self.type = type
        super().__init__(price=self.prices.get(type, 1))

    def drink(self):
        """Boire le café"""
        print("Un bon café pour me réveiller")