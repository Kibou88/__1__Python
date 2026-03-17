class Colors:
    """ ANSI color codes étendus """
    # Couleurs de base (normales)
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"

    # Couleurs vives (bright/high intensity)
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"

    # Nouvelles couleurs ajoutées (bright 90-97 et gris)
    BRIGHT_BLACK = "\033[0;90m"
    BRIGHT_RED = "\033[0;91m"
    BRIGHT_GREEN = "\033[0;92m"
    BRIGHT_YELLOW = "\033[0;93m"
    BRIGHT_BLUE = "\033[0;94m"
    BRIGHT_PURPLE = "\033[0;95m"
    BRIGHT_CYAN = "\033[0;96m"
    BRIGHT_WHITE = "\033[0;97m"

    # Styles
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"

    # Exemples de backgrounds (optionnel, à utiliser avec précaution)
    BG_RED = "\033[0;41m"
    BG_GREEN = "\033[0;42m"
    BG_BLUE = "\033[0;44m"


if __name__ == "__main__":
    colors = Colors()

    # Test des couleurs de texte
    print(colors.END + "Test des couleurs normales et vives :")
    print(colors.BLACK + "Noir" + colors.END)
    print(colors.RED + "Rouge" + colors.END)
    print(colors.GREEN + "Vert" + colors.END)
    print(colors.BROWN + "Marron" + colors.END)
    print(colors.BLUE + "Bleu" + colors.END)
    print(colors.PURPLE + "Violet" + colors.END)
    print(colors.CYAN + "Cyan" + colors.END)
    print(colors.LIGHT_GRAY + "Gris clair" + colors.END)

    # print(colors.DARK_GRAY + "Gris foncé" + colors.END) # Couleur confondu avec la console
    print(colors.LIGHT_RED + "Rouge clair" + colors.END)
    print(colors.LIGHT_GREEN + "Vert clair" + colors.END)
    print(colors.YELLOW + "Jaune" + colors.END)
    print(colors.LIGHT_BLUE + "Bleu clair" + colors.END)
    print(colors.LIGHT_PURPLE + "Violet clair" + colors.END)
    print(colors.LIGHT_CYAN + "Cyan clair" + colors.END)
    print(colors.LIGHT_WHITE + "Blanc clair" + colors.END)

    print(colors.BRIGHT_BLACK + "Noir vif" + colors.END)
    print(colors.BRIGHT_RED + "Rouge vif" + colors.END)
    print(colors.BRIGHT_GREEN + "Vert vif" + colors.END)
    print(colors.BRIGHT_YELLOW + "Jaune vif" + colors.END)
    print(colors.BRIGHT_BLUE + "Bleu vif" + colors.END)
    print(colors.BRIGHT_PURPLE + "Violet vif" + colors.END)
    print(colors.BRIGHT_CYAN + "Cyan vif" + colors.END)
    print(colors.BRIGHT_WHITE + "Blanc vif" + colors.END)

    # Test des styles
    print(colors.BOLD + "Gras" + colors.END)
    print(colors.UNDERLINE + "Souligné" + colors.END)

    # Test backgrounds (attention à la lisibilité)
    print(colors.BG_RED + "Fond rouge" + colors.END + " <- Reset automatique")
