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
    return files_names #Liste des fichiers txt


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
    DicoIDF=calculIDF(dossier) #On crée le DicoIDF  avec comme clé chaque mot et comme valeur son score IDF
    ligne=len(DicoIDF)
    listecle = []
    for key in DicoIDF.keys():
        listecle.append(key) #On récupère chaque mot contenu dans DicoIDF pour faire une liste de mot
    matrice=[]
    for i in range(ligne):
        L=[]
        L.append(listecle[i]) #On ajoute le mot en 1er
        for j in range(col):
            dicoTF= calculTF(dossier, ListeFichier[j]) #Dico de chaque mot avec son ScoreTF du fichier d'indice j dans listeFichier
            if listecle[i] not in dicoTF or listecle[i] not in DicoIDF: #Si le mot n'est pas dans DicoTF ou il est pas dans DICOIDF alors son score sera de 0
                L.append(0)
            else:
                L.append((dicoTF[listecle[i]])*DicoIDF[listecle[i]]) #ScoreTFIDF=ScoreTF * ScoreIDF POUR CHAQUE mot dans chaque Document
        matrice.append(L)
    return matrice
#Dans la fonction ci-dessus, on aura une matrice sous la forme [[mot1,scoreDoc1,scoreDoc2,scoreDoc3,...,ScoreDocNumeroDernierDoc],[mot2,....]...]]


def motnonimportant(dossier):
    matrice=matriceTFIDF(dossier)#On crée la matrice avec chaque mot qui a son score TFIDF de chaque document
    L=[]
    ListeFichier=list_of_files(dossier, "txt")
    nbrFichier=len(ListeFichier)
    for i in range(len(matrice)):
        somme = 0
        for j in range(1,len(matrice[0])): #On commence à l'indice 1 car l'indice 0 équivaut au mot, les indices suivant sont les score TF-IDF du mot
            somme+=matrice[i][j]        # On fait la somme de tous les score TF-IDF du mot
        if (somme/nbrFichier)<=1/8:     #On fait la moyenne de tous les TF-IDF est on prend ceux qui sont proches de 0
            L.append(matrice[i][0])     # On divise par 1/8  pour avoir un nombre proche de 0
    return L

def mot_score_TFIDF_max(dossier):
    matrice = matriceTFIDF(dossier) #On crée la matrice avec chaque mot qui a son score TFIDF de chaque document
    max=0
    L=[]
    ListeFichier=list_of_files(dossier, "txt")
    nbrFichier=len(ListeFichier)
    for i in range(len(matrice)):
        somme = 0
        for j in range(1,len(matrice[0])):#On commence à l'indice 1 car l'indice 0 équivaut au mot, les indices suivant sont les score TF-IDF du mot
            somme+=matrice[i][j]  # On fait la somme de tous les score TF-IDF du mot
        if (somme/nbrFichier)>max: #On fait la moyenne de tous les TF-IDF du MOT et s'il est plus grand que max, il devient max
            L=[]
            L.append(matrice[i][0]) #On ajoute le mot qui a ce score TF-IDF
            L.append(somme/nbrFichier) #On ajoute son score moyen TF-IDF
            max=somme/nbrFichier # On assigne le nouveau max
        elif (somme/nbrFichier)==max: #Si 2 mots ou plus ont le même score moyen TF IDF et que c'est le max
            L.append(matrice[i][0]) # Alors on ajoute le mot
            L.append(somme/nbrFichier) # Et son score TF IDF
    return L #On affiche le ou les mots les plus importants avec leur score TF-IDF

def mot_utilise(dossier,mot):
    presidentmax=[]
    max=0
    L=[]
    ListeFichier=list_of_files(dossier, "txt")
    for k in ListeFichier:#On va parcourir Chaque fichier
        fichier_Courant=str(k)
        scoreTF=calculTF(dossier,fichier_Courant)  #Dictionnaire de chaque mot associé à son score TF
        if mot in scoreTF: #Si le mot est dans le dictionnaire ALORS le président l'aura prononcé
            nom=noms_president(k) #On convertit le nom du fichier en le nom du président grace à la fonction noms_president
            if nom not in L: #Pour éviter les doublons
                L.append(nom)
            if scoreTF[mot]>max: #On cherche le président qui a le plus prononcé le mot
                presidentmax=[]  # On réinitialise la liste car max a été battu
                max=scoreTF[mot]
                presidentmax.append(nom)
            elif scoreTF[mot]==max:  #Si deux présidents ou plus ont prononcé le meme nombre de fois et que c'est le max alors on ajoute à la liste de présidents
                presidentmax.append(nom)
    print("Liste des présidents ayant prononcé le mot",mot,L,"Le président ayant le plus prononcé ce mot",presidentmax)

def nom_fichier(dossier,president): #Ce code va nous permettre de récupérer les noms des fichiers à l'aide du nom d'un président
    ListeFichier=list_of_files(dossier, "txt")
    L=[]
    for k in ListeFichier:#On va parcourir Chaque fichier
        fichier_Courant=str(k)
        if president in fichier_Courant:
            L.append(fichier_Courant)
    return L  #Liste de fichiers d'un président


def mot_repete(dossier,president):
    L=[]
    max=0
    fichiers_president=nom_fichier(dossier,president) #On va récupérer l'ensemble des fichiers d'allocutions du président
    if len(fichiers_president)>1:  #Si un president a deux ou plus allocutions on va combiné les textes de ses allocutions
        texte = ""
        for i in fichiers_president:
            fichier_Courant= str(dossier) + '/' + str(i)
            with open(fichier_Courant, "r") as fc:
                contenu = fc.readlines()
                for ligne in contenu:
                    texte += ligne
            fc.close()
    else:     #Si un président n'a qu'une allocution on va simplement récupérer le texte de son allocution
        texte=""
        fichier_Courant = str(dossier) + '/' + str(fichiers_president[0])
        with open(fichier_Courant, "r") as fc:
            contenu = fc.readlines()
            for ligne in contenu:
                texte += ligne
        fc.close()
    Dico=DictNbrMot(texte) #Dictionnaire avec comme clé chaque mot et valeur son nombre d'occurrence
    for key,valeur in Dico.items():  #Lorsqu'on a le texte On va récupérer le mot qui a le nombre d'occurrences le plus élevé
        if valeur>max:
            L=[]  #Réinitialisation de la liste, on va remplacer l'ancienne valeur par la nouvelle
            max=valeur
            L.append((key,max))
        elif valeur==max:  # SI deux mots ont le meme nombre d'apparitions dans le document
            L.append((key,max)) # Alors on ajoute la clé avec sa valeur DONC max
    return L

def mot_hormis_nonimportant(dossier):
    listemot=[]
    non_important=motnonimportant(dossier) #Liste des mots non important grace à la fonction motnonimportant
    ListeFichier=list_of_files(dossier, "txt")
    col=len(ListeFichier)
    DicoIDF=calculIDF(dossier) #Dictionnaire de tous les mots avec leur score IDF
    ligne=len(DicoIDF)
    listecle = []
    for key in DicoIDF.keys(): #On va ici récupérer seulement les clés Pour faire une liste de tous les mots existants
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
            if matrice[i][j]==0: #Si un scoreTF d'un mot parmi tout ses scores TF équivaut à 0 ALORS un président ne l'aura pas évoqué DONC evoque=False
                evoque=False
        if evoque and matrice[i][0] not in non_important:
            listemot.append(matrice[i][0]) #On va récupérer les mots qui ne sont pas dans non_important et que TOUS
                                            #Les présidents ont évoque
    return listemot




































