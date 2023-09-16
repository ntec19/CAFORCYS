#!/usr/bin/env python3
#
# script build.py
# v20230916


# import du module 'setup', contenant les constantes et fonctions communes
from config_caforcys import *


################################################################
# CONSTANTES SPECIFIQUES :


url = "https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-annuaire-education/records?where=identifiant_de_l_etablissement%3D%220920158X%22&limit=20"

response = requests.get(url)
print(response)
