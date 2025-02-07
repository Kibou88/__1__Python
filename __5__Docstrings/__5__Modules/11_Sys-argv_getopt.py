# Sys.argv et getopt
# - Apprendre à utiliser sys.argv et getopt
#------------------------------------------
import getopt
import sys

"""
sys.argv: The list of command line arguments passed to a Python script.
getopt: This module helps scripts to parse the command line arguments in sys.argv
"""
# run this script using this command line
#

def main(argv):
    """
    Sous la forme: getopt.getopt(args, shortopts, longopts=[])
     - args: the argument list to be parsed
     - shortopts: the string of option letters that the script wants to recognize, with options that require an
            argument followed by a colon (i.e: 'lw:a:' => options w and a require option
     - longopts: if specified, must be a list of strings with the names of the long options which should be supported.
          The leading '--' characters should not be included in the option name

     Return:
         - A pair option-value
    """
    try:
        opts, args = getopt.getopt(argv, "hw:a:", ["write=", "post"])

    except getopt.GetoptError as err:
        print(err)
        sys.exit(2) # Mauvaise utilisation des options de la ligne de commande

    print(f"opts: {opts}") # Retourne les options (-) et (--) et leurs arguments dans un tuple
    print(f"args: {args}") # Retourne tous les arguments qui n'ont pas d'option

    for opt in opts:
        if opt:
            print(opt)

if __name__ == '__main__':
    # A lancer avec un terminal
    # A tester avec ces lignes de commandes
    # -python3 11_Sys-argv_getopt.py -h -b -w file.txt -abcd  --write='test' => # option -b not recognized & stop du script
    # -python3 11_Sys-argv_getopt.py -h -w file.txt -abcd  --write='test' => va dérouler le script
    print(sys.argv[1:])
    main(sys.argv[1:])