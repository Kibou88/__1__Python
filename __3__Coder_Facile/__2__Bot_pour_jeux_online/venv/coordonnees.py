def Cord(coordonnee):
    """Fonction permettant de récupérer les coordonnées des différents points importants du jeu"""
    match coordonnee.lower():
        case "play now":
            return 598,530 # Format x et y
        case "big play":
            return 611, 437
        case "play":
            return 620,394
        case "skip":
            return 859, 639
        case "continue":
            return 668,585

        case "phone":
            return 863,569
        case "menu_topping":
            return 830, 456
        case "t_shrimp":
            return 786, 404
        case "t_nori":
            return 786, 464
        case "t_roe":
            return 877, 466
        case "t_salmon":
            return 784,518
        case "t_unagi":
            return 878,406
        case "menu_rice":
            return 838,474
        case "buy_rice":
            return 838,474
        case "delivery_norm":
            return 796,474
        case "t_exit":
            return 888,520

        case "f_rice":
            return 381,522
        case "f_nori":
            return 330, 570
        case "f_roe":
            return 378,577

        case "table 1":
            return 366, 386
        case "table 2":
            return 476,387
        case "table 3":
            return 575,390
        case "table 4":
            return 676,390
        case "table 5":
            return 778,390
        case "table 6":
            return 880,395
        case "fold mat":
            return 484, 565

        case"s1_hg": # Récupère le coin haut gauche du sushi voulu table 1
            return 407,288
        case "s1_bd":
            return 459,336
        case "s2_hg":  # Récupère le coin haut gauche du sushi voulu table 2
            return 535, 288
        case "s2_bd":
            return 587, 336
        case "s3_hg":  # Récupère le coin haut gauche du sushi voulu table 3
            return 663,288
        case "s3_bd":
            return 715, 336
        case "s4_hg":  # Récupère le coin haut gauche du sushi voulu table 4
            return 791, 288
        case "s4_bd":
            return 843, 336
        case "s5_hg":  # Récupère le coin haut gauche du sushi voulu table 5
            return 919,288
        case "s5_bd":
            return 971, 336
        case "s6_hg":  # Récupère le coin haut gauche du sushi voulu table 6
            return 1047,288
        case "s6_bd":
            return 1099, 336