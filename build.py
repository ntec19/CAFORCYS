#!/usr/bin/env python3
#
# script build.py
# v20230916


# import du module 'setup', contenant les constantes et fonctions communes
from config_caforcys import *


################################################################
# CONSTANTES SPECIFIQUES :

uai = "0920138A"
url = "https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-annuaire-education/records?where=identifiant_de_l_etablissement=\""+uai+"\""

response = requests.get(url)
payload = response.json()
print(response)
print(payload)
