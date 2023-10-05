#!/usr/bin/env python3
#
# module config_caforcys.py 
# v20231005


################################################################
# CONSTANTES FONCTIONNELLES :

DICT_SRC = {
    
    # Annuaire de l'éducation
    # https://www.data.gouv.fr/fr/datasets/annuaire-de-leducation/
    # fr-en-annuaire-education.csv
    'annuaireEducation': {
        'name':     'Annuaire de l\'éducation',
        'what':     'Données sur les établissements publics et privés ouverts situés en France. Le jeu de données couvre le premier degré, le second degré, les Centre d Information et d Orientation ainsi que les établissements administratifs. Sources : données ONISEP et RAMSESE',
        'format':   'csv',
        'urlData':  'https://www.data.gouv.fr/fr/datasets/r/b22f04bf-64a8-495d-b8bb-d84dbc4c7983',
        'file':     'data-annuaire.csv' },
    
    # Idéo-Actions de formation initiale-Univers lycée
    # https://www.data.gouv.fr/fr/datasets/ideo-actions-de-formation-initiale-univers-lycee/
    # 605340ddc19a9.csv
    'actionsFormLycees': {
        'name':     'Idéo-Actions de formation initiale-Univers lycée',
        'what':     'La formation initiale, qu\'elle soit générale ou professionnelle, est le périmètre traditionnel de l\'Onisep, qui s\'adresse en priorité aux jeunes pour une phase de première orientation à différentes étapes de leur cursus scolaire et étudiant. Les grandes étapes en étant jusqu\'ici principalement, mais pas uniquement, l\'orientation en fin de 3e ou l\'orientation en fin de Terminale.\nUne « action de formation » (AF) au sens Onisep est la mise en œuvre, dans un établissement enregistré et localisé, d\'une formation. Cette notion rejoint souvent l\'expression d\' « offre de formation » parfois utilisée par d\'autres organismes.\nPérimètre de ce jeu : les actions de formation initiale ainsi définies, et référencées par l\'Onisep pour le lycée (formations de niveau 2de, 1re, bac, CAP, CAP+1 ou équivalent…) et proposées principalement sous statut scolaire ou étudiant.\n\nAttention l\'Onisep ne diffuse plus sur ce site open data l\'offre de formation en apprentissage, dont il n\'assure pas la collecte exhaustive. Un décret confie désormais cette collecte aux Carif-Oref : http://opendata.onisep.fr/actualite/53/8-apprentissage-les-jeux-open-data-onisep-evoluent.htm',
        'format':   'csv',
        'urlData':  'https://www.data.gouv.fr/fr/datasets/r/c5a46b4e-f9ea-4d48-968c-3e201ae236f4',
        'file':     'data-lycees.csv' },
    
    # Idéo-Actions de formation initiale-Univers enseignement supérieur
    # https://www.data.gouv.fr/fr/datasets/ideo-actions-de-formation-initiale-univers-enseignement-superieur/
    # 605344579a7d7.csv
    'actionsFormSup': {
        'name':     'Idéo-Actions de formation initiale-Univers enseignement supérieur',
        'what':     'La formation initiale, qu\'elle soit générale ou professionnelle, est le périmètre traditionnel de l\'Onisep, qui s\'adresse en priorité aux jeunes pour une phase de première orientation à différentes étapes de leur cursus scolaire et étudiant. Les grandes étapes en étant jusqu\'ici principalement, mais pas uniquement, l\'orientation en fin de 3e ou l\'orientation en fin de Terminale.\nUne « action de formation » (AF) au sens Onisep est la mise en œuvre, dans un établissement enregistré et localisé, d\'une formation. Cette notion rejoint souvent l\'expression d\'« offre de formation » parfois utilisée par d\'autres organismes.\nPérimètre de ce jeu : les actions de formation initiale ainsi définies, et référencées par l\'Onisep pour l\'enseignement supérieur (formations post-baccalauréat) et proposées principalement sous statut scolaire ou étudiant.\n\nAttention l\'Onisep ne diffuse plus sur ce site open data l\'offre de formation en apprentissage, dont il n\'assure pas la collecte exhaustive. Un décret confie désormais cette collecte aux Carif-Oref : http://opendata.onisep.fr/actualite/53/8-apprentissage-les-jeux-open-data-onisep-evoluent.htm',
        'format':   'csv',
        'urlData':  'https://www.data.gouv.fr/fr/datasets/r/b9ed62e0-ad26-4a11-a1f1-162ae9d86161',
        'file':     'data-sup.csv' }

}

'''
💡 sources des données pour DICT_SCOPE_FORMATIONS :

Table de passage codes certifications et formations
https://www.data.gouv.fr/fr/datasets/table-de-passage-codes-certifications-et-formations/
6152ccdf850ef.csv
champs :
"Certif Info (CI) Identifiant";"CI Niveau européen";"CI Intitulé type diplôme";"CI Intitulé";"CI Certifiant";"CI Code RNCP";"CI Code Scolarité";"RNCP Intitulé";"RNCP Type enregistrement";"V_Formation_Diplôme Libellé long";"Idéo Identifiant formation";"Idéo Libellé complet formation";Statut
exemple :
82781;4;"Baccalauréat professionnel";"Bac pro métiers de la sécurité";Oui;19114;40034403;"BAC PRO - Métiers de la sécurité";"Enregistrement de droit";"METIERS DE LA SECURITE (BAC PRO)";FOR.3651;"bac pro Métiers de la sécurité";identique

Idéo-Formations initiales en France
https://www.data.gouv.fr/fr/datasets/ideo-formations-initiales-en-france/
5fa591127f501.csv
champs :
"code NSF";"sigle type formation";"libellé type formation";"libellé formation principal";"sigle formation";durée;"niveau de sortie indicatif";"code RNCP";"niveau de certification";"libellé niveau de certification";tutelle;"URL et ID Onisep";domaine/sous-domaine
exemple :
344;;"baccalauréat professionnel";"bac pro Métiers de la sécurité";;"3 ans";"Bac ou équivalent";19114;4;"niveau 4 (bac ou équivalent)";"Ministère chargé de l'Éducation nationale et de la Jeunesse";http://www.onisep.fr/http/redirection/formation/slug/FOR.3651;"armée, sécurité/sécurité, prévention"

Idéo-Fiches formations
https://www.data.gouv.fr/fr/datasets/ideo-fiches-formations/
5fe07a9ecc960.zip Onisep_Ideo_Fiches_Formations_26062023.xml
XML complet avec descriptif, poursuites d'études, métiers, etc.
'''
DICT_SCOPE_FORMATIONS = {
    
    # cyber     color ffxxxx   calque ffe0e0    cap ffb8b8      bp ff8f8f       mc ff6666       bts ff3d3d

    'FOR.8727': {
        'code':             'FOR.8727',
        'univers':          'cyber',
        'niveau':           '4',
        'formTypeSigle':    'bac pro',
        'formTypeLib':      'baccalauréat professionnel',
        'formLib' :         'bac pro cybersécurité, informatique et réseaux, électronique',
        'formSigle':        'CIEL',
        'rncp':             '37489',
        'codeSco':          '40025519',
        'urlOnisep':        'http://www.onisep.fr/http/redirection/formation/slug/FOR.8727',
        'color':            '#ff8f8f' },
    
    'FOR.8513': {
        'code':             'FOR.8513',
        'univers':          'cyber',
        'niveau':           '4',
        'formTypeSigle':    'MC',
        'formTypeLib':      'mention complémentaire',
        'formLib' :         'MC cybersécurité',
        'formSigle':        'cybersécurité',
        'rncp':             '37488',
        'codeSco':          '01025509',
        'urlOnisep':        'http://www.onisep.fr/http/redirection/formation/slug/FOR.8513',
        'color':            '#ff6666'  },
    
    'FOR.8472': {
        'code':             'FOR.8472',
        'univers':          'cyber',
        'niveau':           '5',
        'formTypeSigle':    'BTS',
        'formTypeLib':      'brevet de technicien supérieur',
        'formLib' :         'BTS cybersécurité, informatique et réseaux, électronique option A informatique et réseaux',
        'formSigle':        'CIEL IR',
        'rncp':             '37391',
        'codeSco':          '32020116',
        'urlOnisep':        'http://www.onisep.fr/http/redirection/formation/slug/FOR.8472',
        'color':            '#ff3d3d'  },
    
    'FOR.8473': {
        'code':             'FOR.8473',
        'univers':          'cyber',
        'niveau':           '5',
        'formTypeSigle':    'BTS',
        'formTypeLib':      'brevet de technicien supérieur',
        'formLib' :         'BTS cybersécurité, informatique et réseaux, électronique option B électronique et réseaux',
        'formSigle':        'CIEL ER',
        'rncp':             '37391',
        'codeSco':          '32025521',
        'urlOnisep':        'http://www.onisep.fr/http/redirection/formation/slug/FOR.8473',
        'color':            '#ff3d3d'  },
    
    'FOR.5987': {
        'code':             'FOR.5987',
        'univers':          'cyber',
        'niveau':           '5',
        'formTypeSigle':    'BTS',
        'formTypeLib':      'brevet de technicien supérieur',
        'formLib' :         'BTS services informatiques aux organisations option A : solutions d\'infrastructure, systèmes et réseaux',
        'formSigle':        'BTS SIO SISR',
        'rncp':             '35340',
        'codeSco':          '32032613',
        'urlOnisep':        'http://www.onisep.fr/http/redirection/formation/slug/FOR.5987',
        'color':            '#ff3d3d'  },
    
    'FOR.5337': {
        'code':             'FOR.5337',
        'univers':          'cyber',
        'niveau':           '5',
        'formTypeSigle':    'BTS',
        'formTypeLib':      'brevet de technicien supérieur',
        'formLib' :         'BTS services informatiques aux organisations option B : solutions logicielles et applications métiers',
        'formSigle':        'BTS SIO SLAM',
        'rncp':             '35340',
        'codeSco':          '32032614',
        'urlOnisep':        'http://www.onisep.fr/http/redirection/formation/slug/FOR.',
        'color':            '#ff3d3d'  },
    
    # sécu     color xxffxx   calque e0ffe0    cap b8ffb8      bp 8fff8f       mc 66ff66       bts 3dff3d
    
    'FOR.847': {
        'code':             'FOR.847',
        'univers':          'sécu',
        'niveau':           '3',
        'formTypeSigle':    'CAP',
        'formTypeLib':      'certificat d\'aptitude professionnelle',
        'formLib' :         'CAP agent de sécurité',
        'formSigle':        'AS',
        'rncp':             '18620',
        'codeSco':          '50034405',
        'urlOnisep':        'http://www.onisep.fr/http/redirection/formation/slug/FOR.847',
        'color':            '#b8ffb8'  },
    
    'FOR.3651': {
        'code':             'FOR.3651',
        'univers':          'sécu',
        'niveau':           '4',
        'formTypeSigle':    'bac pro',
        'formTypeLib':      'baccalauréat professionnel',
        'formLib' :         'bac pro Métiers de la sécurité',
        'formSigle':        '',
        'rncp':             '19114',
        'codeSco':          '40034403',
        'urlOnisep':        'http://www.onisep.fr/http/redirection/formation/slug/FOR.3651',
        'color':            '#8fff8f'  },
    
    'FOR.3732': {
        'code':             'FOR.3732',
        'univers':          'sécu',
        'niveau':           '5',
        'formTypeSigle':    'BTS',
        'formTypeLib':      'brevet de technicien supérieur',
        'formLib' :         'BTS Management opérationnel de la sécurité',
        'formSigle':        'MOS',
        'rncp':             '35393',
        'codeSco':          '32034401',
        'urlOnisep':        'http://www.onisep.fr/http/redirection/formation/slug/FOR.3732',
        'color':            '#3dff3d'  }

}

SYNTHETIC_CSV_FILE  = 'synthese.csv'
UMAP_TEMPLATE       = 'caforcys.umap.template'
UMAP_TARGET         = 'caforcys.umap'

LOCATION_FILTER     = True
LOCATION_LIST       = [ 'Paris', 'Créteil', 'Versailles' ]


################################################################
# CONSTANTES TECHNIQUES :

NSEP            = 32  # pour l'affichage des séparateurs
NEWLINE         = "\n"  # pour le saut de ligne dans le print de DOC


################################################################
# IMPORTS DES MODULES :

try:
    import sys
    import os
    import time
    #import shutil
    import csv
    import re
except:
    print("❌ Une des bibliothèques standards est manquante !\n")
    sys.exit(1)

try:
    import requests
except:
    print("❌ La bibliothèque \"request\" est manquante !\n")
    sys.exit(1)

try:
    import geojson
except:
    print("❌ La bibliothèque \"geojson\" est manquante !\n")
    sys.exit(1)


################################################################
# FONCTIONS :

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def stamp():
    now = time.localtime()
    res = time.strftime("%Y%m%d_%H%M%S", now)
    return res

def touche():
    input("-" * NSEP + "\n⌨️  Appuyez sur la touche 'Entrée' pour continuer.\n" + "-" * NSEP + "\n")

def message(type, string):
    if type == 'i':
        char = 'ℹ️'
    elif type == 'w':
        char = '⚠️'
    elif type == 'e':
        char = '❌'
    else:
        char = ' '
    print(f"\n{'-'*NSEP}\n{char} : {string}\n{'-'*NSEP}\n")

def uai_check(uai):
    # renvoie True si l'argument passé est un UAI valide : 0921234A
    pattern = "^\d{7}[A-Z]$"
    return re.search(pattern, uai)



################################################################
# fin du module 'config_caforcys.py'