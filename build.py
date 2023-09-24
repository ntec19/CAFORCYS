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
message('i', f'Fin de la construction des dictionnaire \'dict_form_uai\' et \'dict_uai_form\' !')
touche()


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


################################################################
# contruction d'un (grand!) dictionnaires des établissements (annuaire)

directory = 'data-annuaire.csv'
key = 'identifiant_de_l_etablissement'
dict_directory = {}
with open(directory, 'r', newline='', encoding='utf-8-sig') as csv_file:
    lecteur_csv = csv.DictReader(csv_file, delimiter=';')
    for row in lecteur_csv:
        # Récupérez la valeur de la colonne 'identifiant_de_l_etablissement' comme clé du dictionnaire
        k = row[key]
        # Supprimez la colonne 'identifiant_de_l_etablissement' des données
        # del row[key] => non, car plus simple à récupérer ensuite
        # Utilisez la clé 'identifiant_de_l_etablissement' pour ajouter le dictionnaire de l'étab dans le dictionnaire
        dict_directory[k] = row
# pour des tests :
# print(dict_directory)
# print(sys.getsizeof(dict_directory))
# print(dict_directory['0921229L'])


################################################################
# contruction d'un dictionnaires étab+formation pour le scope

list_etablCourse = []  # liste de dictionnaires

# définition manuelle de 'header_uai' car de nombreux champs en sont pas pertinents :
header_etab = ["identifiant_de_l_etablissement", "nom_etablissement", "adresse_1", "adresse_2", "adresse_3", "code_postal", "nom_commune", "libelle_departement", "libelle_academie", "fiche_onisep", "type_etablissement", "statut_public_prive", "libelle_nature", "telephone", "mail", "web", "latitude", "longitude"]

# je récupère les clés utilisés dans les formations du dict DICT_SCOPE_FORMATIONS :
header_course = list(DICT_SCOPE_FORMATIONS[next(iter(DICT_SCOPE_FORMATIONS))].keys())
# donne : ['univers', 'niveau', 'formTypeSigle', 'formTypeLib', 'formLib', 'formSigle', 'rncp', 'codeSco', 'urlOnisep']

# je construis le ligne d'entêtes en préfixant par 'etab_' et 'course_' :
header = [ 'etab_'+i for i in header_etab ] + [ 'course_'+i for i in header_course ]

# je construis 'list_etablCourse' en itérant par uai, puis par formation :
for uai in dict_uai_form.keys():
    for course in dict_uai_form[uai]:
        print("----------------\n", uai, course)
        dict_row = {}
        for champ_etab in header_etab:
            try:
                value = dict_directory[uai][champ_etab]
            except KeyError:
                value = None
            dict_row['etab_'+champ_etab] = value
        for champ_course in header_course:
            try:
                value = DICT_SCOPE_FORMATIONS[course][champ_course]
            except KeyError:
                value = None
            dict_row['course_'+champ_course] = value
        list_etablCourse.append(dict_row)
#print(list_etablCourse)


################################################################
# Écriture du fichier CSV pour stocker toutes les données de 'list_etablCourse' :

with open(SYNTHETIC_CSV_FILE, 'w', newline='', encoding='utf-8-sig') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()
    writer.writerows(list_etablCourse)

print("Done!")





# fin