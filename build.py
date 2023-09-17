#!/usr/bin/env python3
#
# script build.py
# v20230916


# import du module 'setup', contenant les constantes et fonctions communes
from config_caforcys import *


################################################################
# CONSTANTES SPECIFIQUES :


url = 'https://www.python.org/static/img/python-logo@2x.png'
myfile = requests.get(url)
open('c:/users/LikeGeeks/downloads/PythonImage.png', 'wb').write(myfile.content)



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