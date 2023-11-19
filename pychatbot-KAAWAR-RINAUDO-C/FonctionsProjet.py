
from math import *
import os
def noms_president(nom_fichier): #Extraire les noms des présidents à partir des noms des fichiers texte fournis
    nom=""
    Trouve=True
    i=0
    while Trouve:
        i+=1
        if nom_fichier[i]=='_':
            nom_fichier=nom_fichier[i+1:len(nom_fichier)]
            Trouve=False
    #Dans le code ci-dessus on a enlevé tout ce qui se trouvait avant le Nom
    i=0
    while 65<=ord(nom_fichier[i])<=90 or 97<=ord(nom_fichier[i])<=122:
        nom = nom + nom_fichier[i]
        i+=1
    return nom
    #Et Dans celui-ci on a enlevé tout ce qui se trouvait après le nom c'est à dire tout les termes non alphabétiques

def prenoms(nom_president): #Ce code va permettre de récuperer le prénom d'un président à l'aide de son nom
    dico_prenom_nom={"Chirac":"Jacques","Giscrad d’Estaing":"Valéry","Mitterrand":"François","Macron":"Emmanuel","Sarkozy":"Nicolas"}
    for cle,valeurs in dico_prenom_nom.items():
        if nom_president==cle:
            return valeurs
def list_of_files(directory, extension): #Fonction disponible sur Moodle, Il permet de créer une liste de tous les fichier txt qui sont dans un même dossier
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def convertirMin(listeFichier):
    for i in listeFichier:   #On va parcourir Chaque fichier
        fichier_Courant='speeches/'+str(i)
        TexteMin=''   #Cette variable sera le nouveau texte convertit en minuscule
        with open(fichier_Courant, "r") as fc:
            contenu=fc.readlines()
            for ligne in contenu: # On va lire le fichier ligne par ligne
                for j in ligne: # Dans chaque ligne on va voir regarder si chaque caractère est en majuscule si oui : on le mets en minuscule
                    if 65<=ord(j)<=90:
                        TexteMin+=chr(ord(j)+32)
                    else:
                        TexteMin+=j
            fc.close()
        FichierDestination='cleaned/'+str(i)
        with open(FichierDestination, "w") as fd:  #On va mettre TexteMin dans le répertoire cleaned dans un fichier ayant le meme nom que l'original
            fd.write(TexteMin)
            fd.close()
    # La fonction peut prendre un certains temps (10-15s)
def Ponctuation(listedeFichiers):
    ponctuation = '.;:!,?"()-'
    for i in listedeFichiers:  # On va parcourir Chaque fichier
        fichier_Courant = 'cleaned/' + str(i)
        NouveauTexte = ''  # Cette variable sera le nouveau texte dénué de tout caractère de ponctuation
        with open(fichier_Courant, "r") as fc:
            contenu = fc.readlines()
            for ligne in contenu:  # On va lire le fichier ligne par ligne
                indice = 0  # On incrémente un compteur qui va donnner l'indice du caractère auquel j se trouve
                for j in ligne:  # On parcours chaque ligne
                    if j in ponctuation:  # et on va regarder s'il y a la présence de caractères de ponctuation, si oui, chacun d'eux sera supprimé
                        if str(ligne[indice-1]) != " " and str(ligne[indice+1]) != " ": #  ou remplacés par un espace
                            ligne[indice] = " "
                        else:
                            del ligne[indice]
                    indice += 1
            fc.close()
        with open(fichier_Courant, "w") as fd:  # On va coller le nouveau texte dans le meme fichier
            fd.write(NouveauTexte)
            fd.close()

def DictNbrMot(texte):
    dico={}
    mot=""
    for i in texte:
        if i==" ":
            if mot not in dico:
                dico[mot]=1
            else:
                dico[mot]+=1
            mot=""
        else:
            mot+=i
    if mot not in dico: #Pour le dernier mot vu qu'il n'y a pas d'espace à la fin
        dico[mot] = 1
    else:
        dico[mot] += 1
    print(dico)





















