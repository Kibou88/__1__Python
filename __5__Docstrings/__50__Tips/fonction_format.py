# fonction format
# - Apprendre à utiliser la fonction format
#-------------------------------------------
text = '{} {}'.format('Pierre', 'Dupont')
print(text)

print('{0} {1}'.format('Pierre', 'Dupont'))

print('{1} {0}'.format('Pierre', 'Dupont'))

print('{0} {0}'.format('Pierre', 'Dupont'))

print('{} a {} ans'.format('Pierre', 18))

print('{:10} {}'.format('Debut', 'Fin')) # Rajouter 10 espaces apres 'Debut'

print('{:>10} {}'.format('Debut', 'Fin')) # Rajouter 10 espaces avant 'Debut'

print('{} {:=>10}'.format('Debut', 'Fin')) # Rajouter 10 = avant 'Fin'

print('{:+^25}'.format('Pierre'))

print('{:.3}'.format('Pierre'))

class MaVoiture(object):
    def __init__(self):
        self.couleur = 'Rouge'
        self.marque = 'Ferrari'

print("J'ai une {o.marque} de couleur {o.couleur}".format(o=MaVoiture()))