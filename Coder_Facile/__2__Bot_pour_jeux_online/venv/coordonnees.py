def Cord(coordonnee):
    """Fonction permettant de récupérer les coordonnées des différents points importants du jeu"""
    match coordonnee.lower():
        case "play now":
            return 793,256 # Format x et y
        case "big play":
            return 835, 153
        case "skip":
            return 1023, 309
        case "continue":
            return 806,252

        case "phone":
            return 499,313
        case "menu_topping":
            return 473, 234
        case "t_shrimp":
            return 435, 171
        case "t_nori":
            return 435, 231
        case "t_roe":
            return 512, 231
        case "t_salmon":
            return 435,289
        case "t_unagi":
            return 512,182
        case "menu_rice":
            return 460,251
        case "buy_rice":
            return 473, 252
        case "delivery_norm":
            return 435,246

        case "f_rice":
            return 20,290
        case "f_nori":
            return -28, 346
        case "f_roe":
            return 20,346
        case "table 1":
            return 11, 160
        case "table 2":
            return 116,160
        case "table 3":
            return 216,160
        case "table 4":
            return 318,160
        case "table 5":
            return 422,160
        case "table 6":
            return 527,160