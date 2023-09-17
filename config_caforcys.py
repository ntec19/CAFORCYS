#!/usr/bin/env python3
#
# module setup.py 
# v20230916


################################################################
# CONSTANTES :

DICT_SRC = {}
# https://www.data.gouv.fr/fr/datasets/annuaire-de-leducation/


DICT_SCOPE_COURSES = {}


TEMPO           = 0.1
NSEP            = 32  # pour l'affichage des séparateurs
NEWLINE         = "\n"  # pour le saut de ligne dans le print de DOC

# pour sanitize()
CHAR_SEP        = "+"
CHAR_SUB        = "_"
MAJ             = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SPE             = "ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÑÒÓÔÕÖŒÙÚÛÜ"
NBR             = "0123456789-"
LEG_CHAR        = MAJ + MAJ.lower() + SPE + SPE.lower() + NBR



################################################################
# FONCTIONS :

try:
    #import sys
    #import os
    import time
    #import shutil
    import csv
except:
    print("❌ Une des bibliothèques standards est manquante !\n")
    sys.exit(1)

try:
    import requests
except:
    print("❌ La bibliothèque request est manquante !\n")
    sys.exit(1)


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def stamp():
    now = time.localtime()
    res = time.strftime("%Y%m%d_%H%M%S", now)
    return res


def sanitize(s):
    res = ""
    for letter in s:
        if letter in LEG_CHAR:
            res += letter
        else:
            res += CHAR_SUB
    return res


def touche():
    input("-" * NSEP + "\n⌨️ Appuyez sur la touche 'Entrée' pour continuer.\n" + "_" * NSEP + "\n")


def info(s):
    print(f"\n{'-'*NSEP}\nℹ️ : {s}\n{'_'*NSEP}\n")






################################################################
# fin du module 'config_caforcys.py'