#!/usr/bin/env python3
#
# module setup.py 
# v20230916


################################################################
# Sources de données

'''
Jeux de données susceptibles d'être pertinents :

Inserjeunes Voie professionnelle scolaire par lycée d'enseignement professionnel
https://www.data.gouv.fr/fr/datasets/inserjeunes-voie-professionnelle-scolaire-par-lycee-denseignement-professionnel/

Inserjeunes Voie professionnelle scolaire par lycée d'enseignement professionnel et par examen passé
https://www.data.gouv.fr/fr/datasets/inserjeunes-voie-professionnelle-scolaire-par-lycee-denseignement-professionnel-et-par-examen-passe/

Inserjeunes Voie professionnelle scolaire par lycée d'enseignement professionnel et formation fine
https://www.data.gouv.fr/fr/datasets/inserjeunes-voie-professionnelle-scolaire-par-lycee-denseignement-professionnel-et-formation-fine/

Inserjeunes Apprentissage par centre de formation d'apprentis (CFA)
https://www.data.gouv.fr/fr/datasets/inserjeunes-apprentissage-par-centre-de-formation-dapprentis-cfa/

Inserjeunes Apprentissage par centre de formation d'apprentis (CFA) et niveau de formation CAP à BTS
https://www.data.gouv.fr/fr/datasets/inserjeunes-apprentissage-par-centre-de-formation-dapprentis-cfa-et-niveau-de-formation-cap-a-bts/

Inserjeunes Apprentissage par centre de formation d'apprentis (CFA) et formation fine niveau CAP à BTS
https://www.data.gouv.fr/fr/datasets/inserjeunes-apprentissage-par-centre-de-formation-dapprentis-cfa-et-formation-fine-niveau-cap-a-bts/

Idéo-Actions de formation-Ile-de-France
https://www.data.gouv.fr/fr/datasets/ideo-actions-de-formation-ile-de-france/

Effectifs des élèves en voie professionnelle ou BTS par niveau, sexe et lycée professionnel – Date d’observation au début du mois d’octobre chaque année
https://www.data.gouv.fr/fr/datasets/effectifs-des-eleves-en-voie-professionnelle-ou-bts-par-niveau-sexe-et-lycee-professionnel-date-dobservation-au-debut-du-mois-doctobre-chaque-annee/

Diplômes préparés dans les établissements du secondaire et formations intermédiaires
https://www.data.gouv.fr/fr/datasets/diplomes-prepares-dans-les-etablissements-du-secondaire-et-formations-intermediaires/

----

Annuaire de l'éducation
https://www.data.gouv.fr/fr/datasets/annuaire-de-leducation/

Adresse et géolocalisation des établissements d'enseignement du premier et second degrés
https://www.data.gouv.fr/fr/datasets/adresse-et-geolocalisation-des-etablissements-denseignement-du-premier-et-second-degres-1/

Localisations des établissements scolaires dans OpenStreetMap ?
https://www.data.gouv.fr/fr/datasets/localisations-des-etablissements-scolaires-dans-openstreetmap/

Annuaire des bureaux des entreprises des lycées professionnels et polyvalents 
https://www.data.gouv.fr/fr/datasets/annuaire-des-bureaux-des-entreprises-des-lycees-professionnels-et-polyvalents/

Liste des diplômes professionnels de l’éducation nationale
https://www.data.gouv.fr/fr/datasets/liste-des-diplomes-professionnels-de-leducation-nationale/

Listes des centres de formation d'apprentis (adresse, nombre d'élèves, taux d'insertion, taux de rupture par spécialité)
https://www.data.gouv.fr/fr/datasets/listes-des-centres-de-formation-dapprentis-adresse-nombre-deleves-taux-dinsertion-taux-de-rupture-par-specialite/

'''

################################################################
# CONSTANTES :

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