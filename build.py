#!/usr/bin/env python3
#
# script build.py
# v20230917


# import du module 'setup', contenant les constantes et fonctions communes
from config_caforcys import *
clear()


################################################################
# CONSTANTES SPECIFIQUES :

# ...


################################################################
# TÉLÉCHARGEMENT DES FICHIERS DE DONNÉES :

"""
for source in DICT_SRC.keys():
    url         = DICT_SRC[source]['urlData']
    fileName    = DICT_SRC[source]['file']
    name        = DICT_SRC[source]['name']
    try:
        r   = requests.get(url)
    except:
        message('e', f'Erreur lors le téléchargement du fichier "{name}"')
        sys.exit(2)
    if r.status_code != 200:
        message('e', f'Erreur d\'accès au fichier "{name}"')
        sys.exit(2)
    with open(fileName, 'wb') as f:
        f.write(r.content)
    message('i', f'Fichier "{name}" correctement téléchargé -> {fileName}')
    touche()
"""
# 3 fichiers : data-annuaire.csv, data-lycees.csv, data-sup.csv


################################################################
# construction de la liste des formations recherchées

liste_formations    = []
for formation in DICT_SCOPE_FORMATIONS.keys():
    liste_formations.append(formation)
print(liste_formations)
touche()


################################################################
# contruction des dictionnaires de correspondance

DICT_FORM_UAI = {}
DICT_UAI_FORM = {}

# Analyse du fichier de données : data-lycees.csv ET data-sup.csv

list_files = ['data-lycees.csv', 'data-sup.csv']

for file in list_files:
    with open(file, 'r', newline='', encoding='utf-8-sig') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        next(reader) # pour virer la première ligne qui contient les descripteurs de champs
        for row in reader:
            try:
                formation = row[2][-8:]         # utile si format de champ non conforme
            except:
                formation = 'none'
            if formation in liste_formations:
                try:
                    uai = row[10]               # utile si format de champ non conforme
                except:
                    uai = '0000000A'
                    print(row)
                    touche()
                if not uai_check(uai):
                    uai = '0000000A'
                    print(row)
                    touche()
                # ajout à DICT_FORM_UAI
                if formation in DICT_FORM_UAI.keys():
                    DICT_FORM_UAI[formation].append(uai)
                else:
                    DICT_FORM_UAI[formation] = [uai]
                
                # ajout à DICT_UAI_FORM
                if uai in DICT_UAI_FORM.keys():
                    DICT_UAI_FORM[uai].append(formation)
                else:
                    DICT_UAI_FORM[uai] = [formation]


print("DICT_FORM_UAI", DICT_FORM_UAI)
print("DICT_UAI_FORM",DICT_UAI_FORM, "\n")
touche()

# Analyse du fichier de données : data-lycees.csv



















# Tests divers

'''
Test de l'API "Annuaire éducation"
uai = "0920138A"
url = "https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-annuaire-education/records?where=identifiant_de_l_etablissement=\""+uai+"\""
response = requests.get(url)
payload = response.json()
print(response)
print(payload)
'''

# fin