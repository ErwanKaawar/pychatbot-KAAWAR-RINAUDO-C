import fileinput
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













