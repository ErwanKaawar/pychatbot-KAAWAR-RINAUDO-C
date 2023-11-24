import math
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
def Ponctuation(listeFichierCleaned):
    ponctuations = ['!', '"', '#', '$', '%', '&','(', ')', '*', '+', ',', '.', '/', ':', ';', '<', '=', '>',
                    '?', '@', '[', ']', '^', '{', '|', '}', '~']
    ponctuationsspéciaux=["'",'','`','-','_']
    for i in listeFichierCleaned:   #On va parcourir Chaque fichier
        fichier_Courant='cleaned/'+str(i)
        texteNoPonct=''
        with open(fichier_Courant, "r") as fc:
            contenu=fc.readlines()
            for ligne in contenu: # On va lire le fichier ligne par ligne
                for j in ligne:
                    if j in ponctuationsspéciaux or j=='\n': #j==\n pour eviter la concaténation de 2 mots lorsqu'un saut de ligne les separe
                        texteNoPonct += ' '
                    elif j in ponctuations:
                        texteNoPonct += ''
                    else:
                        texteNoPonct += j.rstrip('\n') #rstrip('\n') va permettre de supprimer les \n s'il y en a à la fin d'un mot
        fc.close()
        textefinal = ""   #On a un texte avec des espaces en trop on va donc les enlever
        espace_en_trop = False
        for caractere in texteNoPonct:
            if caractere == ' ':
                if not espace_en_trop:
                    textefinal += caractere
                    espace_en_trop = True
            else:
                textefinal += caractere
                espace_en_trop = False
        FichierDestinationCleaned='cleaned/'+str(i)
        with open(FichierDestinationCleaned, "w") as fd:
            fd.write(textefinal)
            fd.close()

def DictNbrMot(texte):
    dicoTF={}
    mot=""
    for i in texte:
        if i==" ":
            if mot not in dicoTF:
                dicoTF[mot]=1
            else:
                dicoTF[mot]+=1
            mot=""
        else:
            mot+=i
    if mot not in dicoTF: #Pour le dernier mot vu qu'il n'y a pas d'espace à la fin
        dicoTF[mot] = 1
    else:
        dicoTF[mot] += 1
    return dicoTF

def calculTF(dossier,fichier):
    texte=""
    fichier_Courant = dossier + '/' + str(fichier)
    with open(fichier_Courant, "r") as fc:
        contenu = fc.readlines()
        for ligne in contenu:
            texte += ligne
        fc.close()
    return DictNbrMot(texte)

def calculIDF(dossier): #On entre en paramètre le dossier où se trouve l'ensemble des fichiers
    dicoIDF={}
    ListeFichier=list_of_files(dossier, "txt")
    nbrFichier=len(ListeFichier)
    for k in ListeFichier:#On va parcourir Chaque fichier
        texte=""
        fichier_Courant=dossier+'/'+str(k)
        with open(fichier_Courant, "r") as fc:
            contenu=fc.readlines()
            for ligne in contenu:
                texte+=ligne
        dico=DictNbrMot(texte)
        if '' in dico.keys():
            del dico[''] #enlever les espaces contenu comme clé dans dico
        for key in dico.keys(): #Va prendre chaque mot et le mettre dans le dicoIDF UNE FOIS par document
            if key in dicoIDF:
                dicoIDF[key]+=1
            else:
                dicoIDF[key]=1
    for key,valeurs in dicoIDF.items():
        dicoIDF[key]=round(math.log((1/(valeurs/nbrFichier))+1,10),3) #ON va arrondir à 3 chiffres pour soucis de lisibilité
    return dicoIDF

def matriceTFIDF(dossier):
    ListeFichier=list_of_files(dossier, "txt")
    col=len(ListeFichier)
    x=calculIDF(dossier)
    ligne=len(x)
    listecle = []
    for key in x.keys():
        listecle.append(key)
    matrice=[]
    for i in range(ligne):
        L=[]
        L.append(listecle[i])
        for j in range(col):
            dicoTF= calculTF(dossier, ListeFichier[j])
            if listecle[i] not in dicoTF or listecle[i] not in x:
                L.append(0)
            else:
                L.append((dicoTF[listecle[i]])*x[listecle[i]])
        matrice.append(L)
    return matrice


def motnonimportant(dossier):
    matrice=matriceTFIDF(dossier)
    L=[]
    ListeFichier=list_of_files("cleaned", "txt")
    nbrFichier=len(ListeFichier)
    for i in range(len(matrice)):
        somme = 0
        for j in range(1,len(matrice[0])):
            somme+=matrice[i][j]
        if (somme/nbrFichier)<=1/8:     #On fait la moyenne de tous les TF-IDF est on prend ceux qui sont proches de 0
            L.append(matrice[i][0])
    return L

def moteleve(dossier):
    matrice = matriceTFIDF(dossier)
    max=0
    L=[]
    ListeFichier=list_of_files("cleaned", "txt")
    nbrFichier=len(ListeFichier)
    for i in range(len(matrice)):
        somme = 0
        for j in range(1,len(matrice[0])):
            somme+=matrice[i][j]
        if (somme/nbrFichier)>max: #On fait la moyenne de tous les TF-IDF est on prend ceux qui sont proches de 0
            L=[]
            L.append(matrice[i][0])
            L.append(somme/nbrFichier)
            max=somme/nbrFichier
        elif (somme/nbrFichier)==max:
            L.append(matrice[i][0])
            L.append(somme/nbrFichier)
    return L #On affiche le ou les mots les plus importants avec leur score TF-IDF

def mot_utilise(dossier,mot):
    presidentmax=[]
    max=0
    L=[]
    ListeFichier=list_of_files(dossier, "txt")
    for k in ListeFichier:#On va parcourir Chaque fichier
        fichier_Courant=str(k)
        scoreTF=calculTF(dossier,fichier_Courant)
        if mot in scoreTF:
            nom=noms_president(k)
            if nom not in L:
                L.append(nom)
            if scoreTF[mot]>max:
                presidentmax=[]
                max=scoreTF[mot]
                presidentmax.append(nom)
            elif scoreTF[mot]==max:
                presidentmax.append(nom)
    print("Liste des présidents ayant prononcé le mot",mot,L,"Le président ayant le plus prononcé ce mot",presidentmax)

def nom_fichier(dossier,president): #Ce code va nous permettre de récupérer les noms des fichiers à l'aide du nom d'un président
    ListeFichier=list_of_files(dossier, "txt")
    L=[]
    for k in ListeFichier:#On va parcourir Chaque fichier
        fichier_Courant=str(k)
        if president in fichier_Courant:
            L.append(fichier_Courant)
    return L


def mot_repete(dossier,president):
    L=[]
    max=0
    fichiers_president=nom_fichier(dossier,president)
    if len(fichiers_president)>1:  #Si un president a deux ou plus allocutions on va combiné les textes de ses allocutions
        texte = ""
        for i in fichiers_president:
            fichier_Courant= str(dossier) + '/' + str(i)
            with open(fichier_Courant, "r") as fc:
                contenu = fc.readlines()
                for ligne in contenu:
                    texte += ligne
            fc.close()
    else:
        texte=""
        fichier_Courant = str(dossier) + '/' + str(fichiers_president[0])
        with open(fichier_Courant, "r") as fc:
            contenu = fc.readlines()
            for ligne in contenu:
                texte += ligne
        fc.close()
    Dico=DictNbrMot(texte)
    for key,valeur in Dico.items():
        if valeur>max:
            L=[]
            max=valeur
            L.append((key,max))
        elif valeur==max:  # SI deux mots ont le meme nombre d'apparitions dans le document
            L.append((key,max))
    return L

def mot_hormis_nonimportant(dossier):
    listemot=[]
    non_important=motnonimportant(dossier)
    ListeFichier=list_of_files(dossier, "txt")
    col=len(ListeFichier)
    x=calculIDF(dossier)
    ligne=len(x)
    listecle = []
    for key in x.keys():
        listecle.append(key)
    matrice=[]
    for i in range(ligne):
        L=[]
        L.append(listecle[i])
        for j in range(col):
            dicoTF= calculTF(dossier, ListeFichier[j])
            if listecle[i] not in dicoTF:
                L.append(0)
            else:
                L.append((dicoTF[listecle[i]]))
        matrice.append(L) #Matrice des scoreTF de chaque mot dans chaque document
    for i in range(len(matrice)):
        evoque=True
        for j in range(1,len(matrice[0])):
            if matrice[i][j]==0:
                evoque=False
        if evoque and matrice[i][0] not in non_important:
            listemot.append(matrice[i][0])
    return listemot




































