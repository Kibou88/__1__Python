# Exemple d'utilisation de args et kwargs
#-----------------------------------------
def liste_invitee(invite_vip, *args):
    print(f'{invite_vip} est un VIP')
    for invite in args:
        print(f'{invite} est un invite normal')

liste_invitee('Paul', 'Pierre', 'Marie', 'Max')

def liste_invitee2(invite_vip, *args, **kwargs):
    print(f'{invite_vip} est un VIP')
    for invite in args:
        print(f'{invite} est un invite normal')

    indesirables = kwargs.get('indesirable')
    if indesirables:
        print(f'Ces invites sont indesirables {", ".join(indesirables)}')

liste_invitee2('Paul', 'Pierre', 'Marie', 'Max', indesirable=['Simon', 'Julie', 'Theo'])