#!/usr/bin/env python3
#
# script build.py
# v20230924


# import du module 'setup', contenant les constantes et fonctions communes
from config_caforcys import *
clear()


################################################################
# CONSTANTES SPECIFIQUES :

# ...


################################################################
# TÉLÉCHARGEMENT DES FICHIERS DE DONNÉES :

choice = ''
while choice.lower() != 'o' and choice.lower() != 'n':
    print("Voulez-vous télécharger les données depuis Internet ? (o/n)")
    choice = input()

if choice.lower() == 'o':
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

validDataFiles = True
for s in DICT_SRC.keys():
    if not os.path.exists(DICT_SRC[s]['file']):
        message('e', f"Fichier {DICT_SRC[s]['file']} non trouvé !")
        validDataFiles = False
if not validDataFiles:
    message('e', f'Un problème est survenu : tous les fichiers de données nécessaires ne sont pas disponibles !')
    sys.exit(2)

# 3 fichiers désormais présents dans le répertoire courant : : data-annuaire.csv, data-lycees.csv, data-sup.csv


################################################################
# construction de la liste des formations recherchées

liste_formations    = []
for formation in DICT_SCOPE_FORMATIONS.keys():
    liste_formations.append(formation)
#print("Liste des formations :\n", liste_formations, "\n")
#touche()


################################################################
# contruction des dictionnaires de correspondance

dict_form_uai = {}
dict_uai_form = {}

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
                    #print('UAI invalide :\n', row, '\n')
                    #touche()
                if not uai_check(uai):
                    uai = '0000000A'
                    #print('UAI invalide :\n', row, '\n')
                    #touche()
                # ajout à dict_form_uai
                if formation in dict_form_uai.keys():
                    dict_form_uai[formation].append(uai)
                else:
                    dict_form_uai[formation] = [uai]
                
                # ajout à dict_uai_form
                if uai in dict_uai_form.keys():
                    dict_uai_form[uai].append(formation)
                else:
                    dict_uai_form[uai] = [formation]


#print("dict_form_uai :\n", dict_form_uai)
#print("dict_uai_form :\n",dict_uai_form, "\n")
#touche()

# pour mes tests :
dict_uai_form = {
    "0101015Z": [
        "FOR.8727"
    ],
    "0110008Z": [
        "FOR.3651",
        "FOR.8727"
    ],
    "0120096P": [
        "FOR.3651"
    ],
    "0121309H": [
        "FOR.8727",
        "FOR.8727"
    ],
    "0131436R": [
        "FOR.8727",
        "FOR.8473",
        "FOR.8472"
    ],
    "0131709M": [
        "FOR.8727"
    ],
}

'''
# Pour générer le fichier csv avec une ligne par formation
for uai in dict_uai_form.keys():
    for course in dict_uai_form[uai]:
        print(uai, course)
'''

message('i', '----')


################################################################
# contruction d'un (grand!) dictionnaires des établissements (annuaire)

directory = 'test.csv'
dict_annuaire = {}
key = 'id' #'identifiant_de_l_etablissement'
with open(directory, 'r', newline='', encoding='utf-8-sig') as csv_file:
    lecteur_csv = csv.DictReader(csv_file, delimiter=';')
    for row in lecteur_csv:
        # Récupérez la valeur de la colonne 'id' comme clé du dictionnaire
        k = row[key]
        # Supprimez la colonne 'id' des données
        del row[key]
        # Utilisez la clé 'id' pour ajouter les données restantes dans le dictionnaire
        dict_annuaire[k] = row
# Affichez le dictionnaire résultant
print(dict_annuaire)
print(sys.getsizeof(dict_annuaire))






# fin