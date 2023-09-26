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

# print("dict_form_uai :\n", dict_form_uai)
# print("dict_uai_form :\n",dict_uai_form, "\n")
message('i', f'Fin de la construction des dictionnaire \'dict_form_uai\' et \'dict_uai_form\' !')
touche()

'''
Pour mes tests, jeu de données réduits :
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
# pour mes tests :
# print(dict_directory)
# print(sys.getsizeof(dict_directory))
# print(dict_directory['0921229L'])


################################################################
# contruction d'une liste de dictionnaires étab+formation pour le scope

list_etablCourse = []  # liste de dictionnaires

# définition manuelle de 'header_uai' car de nombreux champs en sont pas pertinents :
header_etab = ["identifiant_de_l_etablissement", "nom_etablissement", "adresse_1", "adresse_2", "adresse_3", "code_postal", "nom_commune", "libelle_departement", "libelle_academie", "fiche_onisep", "type_etablissement", "statut_public_prive", "libelle_nature", "telephone", "mail", "web", "latitude", "longitude"]

# je récupère les clés utilisés dans les formations du dict DICT_SCOPE_FORMATIONS :
header_course = list(DICT_SCOPE_FORMATIONS[next(iter(DICT_SCOPE_FORMATIONS))].keys())
# donne : ['code', 'univers', 'niveau', 'formTypeSigle', 'formTypeLib', 'formLib', 'formSigle', 'rncp', 'codeSco', 'urlOnisep']

# je construis le ligne d'entêtes en préfixant par 'etab_' et 'course_' :
header = [ 'etab_'+i for i in header_etab ] + [ 'course_'+i for i in header_course ]

# je construis 'list_etablCourse' en itérant par uai, puis par formation :
for uai in dict_uai_form.keys():
    if uai == "" or uai == None:
        continue
    for course in dict_uai_form[uai]:
        #print("----------------\n", uai, course)
        dict_row = {}
        error = False
        for champ_etab in header_etab:
            try:
                value = dict_directory[uai][champ_etab]
            except KeyError:
                value = None
                error = True
            dict_row['etab_'+champ_etab] = value
        for champ_course in header_course:
            try:
                value = DICT_SCOPE_FORMATIONS[course][champ_course]
            except KeyError:
                value = None
                error = True
            dict_row['course_'+champ_course] = value
        if not error:
            list_etablCourse.append(dict_row)
#print(list_etablCourse)


################################################################
# Écriture du fichier CSV pour stocker toutes les données de 'list_etablCourse' :

with open(SYNTHETIC_CSV_FILE, 'w', newline='', encoding='utf-8-sig') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=header, delimiter =';')
    writer.writeheader()
    writer.writerows(list_etablCourse)

message('i', f"Fichier de synthèse '{SYNTHETIC_CSV_FILE}' créé !")
touche()


################################################################
# Création du fichier UMAP pour la carte

listFeaturesCyber =[]
listFeaturesSecu =[]

# Ouverture du fichier CSV de synthèse précédemment créé:
with open(SYNTHETIC_CSV_FILE, 'r', newline='', encoding='utf-8-sig') as csv_file: 
    reader = csv.reader(csv_file, delimiter =';')
    next(reader)  # pour faire sauter la première ligne qui contient les descripteurs
    for row in reader:
        #print(row)
        try:
            point = geojson.Point((float(row[17]), float(row[16])))
        except:
            continue
        name = row[23]
        description         =  '**' + row[1] + '**\n'
        if row[2] != '':
            description     += row[2] + '\n'
        if row[3] != '':
            description     += row[3] + '\n'
        if row[4] != '':
            description     += row[4] + '\n'
        description         += row[5] + ' **' + row[6] + '** (' + row[7] + ')\n'
        description         += 'académie : ' + row[8] + '\n'
        description         += 'téléphone : ' + row[13] + '\n'
        description         += 'courriel : [[' + row[14] + ']]\n'
        description         += 'infos établissement : [[' + row[15] + '|site web]] - [[' + row[9] + '|fiche Onisep]]\n'
        description         += '\n'
        description         += 'formation de niveau : **' + row[20] + '** *(' + row[21] + ')*\n'
        description         += '[[' + row[27] + '|fiche Oniwep]] - [[https://www.francecompetences.fr/recherche/rncp/' + row[25] + '/|fiche RNCP]]\n'
        properties = { "_umap_options": { "color": row[28], "iconClass": "Drop", "showLabel": None, }, "name": name, "description": description }
        feature = geojson.Feature(geometry=point, properties=properties)
        #print('\n\nfeature :\n', feature,'\n')
        #touche()
        if row[19] == 'cyber':
            listFeaturesCyber.append(feature)
        if row[19] == 'sécu':
            listFeaturesSecu.append(feature)
        #print('listFeaturesCyber :\n', listFeaturesCyber,'\n')
        #print('listFeaturesSecu :\n', listFeaturesCyber,'\n')

with open(UMAP_TEMPLATE, 'r', encoding="utf-8") as f:
    umapString = f.read()

umapString  = umapString.replace('to_be_replaced_secu',str(listFeaturesSecu)).replace('to_be_replaced_cyber',str(listFeaturesCyber))

with open(UMAP_TARGET, 'w', encoding="utf-8") as f:
    f.write(umapString)

with open('secu.geojson', 'w', encoding="utf-8") as f:
    f.write(str(listFeaturesSecu))
with open('cyber.geojson', 'w', encoding="utf-8") as f:
    f.write(str(listFeaturesCyber))


'''
row :
0                                           1                                       2                               3                   4                   5                       6                       7                               8                           9                                                                       10                          11                                  12                          13                              14                              15                              16                      17                          18                  19                      20                  21                          22                                      23                                                  24                          25                  26                  27                                                                  28
['etab_identifiant_de_l_etablissement',     'etab_nom_etablissement',               'etab_adresse_1',               'etab_adresse_2',   'etab_adresse_3',   'etab_code_postal',     'etab_nom_commune',     'etab_libelle_departement',     'etab_libelle_academie',    'etab_fiche_onisep',                                                    'etab_type_etablissement',  'etab_statut_public_prive',         'etab_libelle_nature',      'etab_telephone',               'etab_mail',                    'etab_web',                     'etab_latitude',        'etab_longitude',           'course_code',      'course_univers',       'course_niveau',    'course_formTypeSigle',     'course_formTypeLib',                   'course_formLib',                                   'course_formSigle',         'course_rncp',      'course_codeSco',   'course_urlOnisep',                                                 'course_color']
['0850028U',                                'Lycée professionnel Edouard Branly',   '5 boulevard Edouard Branly',   'BP 259',           '',                 '85006',                'La Roche-sur-Yon',     'Vendée',                       'Nantes',                   'https://www.onisep.fr/http/redirection/etablissement/slug/ENS.3241',   'Lycée',                    'Public',                           'LYCEE PROFESSIONNEL',      '02 51 24 06 06',               'ce.0850028u@ac-nantes.fr',     'http://branly.e-lyco.fr/',     '46.67421847152482',    '-1.4419439014403423',      'FOR.3732',         'sécu',                 '5',                'BTS',                      'brevet de technicien supérieur',       'BTS Management opérationnel de la sécurité',       'MOS',                      '35393',            '32034401',         'http://www.onisep.fr/http/redirection/formation/slug/FOR.3732',    '#33ff33']
'''




'''
to be continued :

à partir de ce très beau fichier synthèse.csv,
créer un encore plus beau fichier UMAP en utilisant la bibliothèque geojson
Deux calques : cyber et sécu


'''



# fin