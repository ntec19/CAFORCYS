#!/usr/bin/env python3
#
# script build.py
# v20230916


# import du module 'setup', contenant les constantes et fonctions communes
from config_caforcys import *


################################################################
# CONSTANTES SPECIFIQUES :


################################################################
# TÉLÉCHARGEMENT DES FICHIERS DE DONNÉES :

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