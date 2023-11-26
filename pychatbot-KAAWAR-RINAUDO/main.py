import os
from FonctionsProjet import *
if __name__ == '__main__':
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    print(files_names)

    def fonction_Noms_president():
        nom_fichier=input("Merci de rentrer le nom du fichier:")
        print(noms_president(nom_fichier))
    def fonction_prenoms():
        nom=input("Merci de rentrer le nom du president:")
        print(prenoms(nom))
    def fonction_ConvertirMin():
        print(convertirMin(files_names))
        print("La fonction a bien été exécuté, cela peut prendre un certains temps")

    def fonction_Ponctuation():
        print(Ponctuation(files_names))
        print("La fonction a bien été exécuté, cela peut prendre un certains temps")

    def fonction_calculTF():
        fichier=input("Entrer le nom du fichier texte voulu:")
        print(calculTF("cleaned",fichier))
    def fonction_calculIDF():
        print(calculIDF("cleaned"))
    def fonction_matriceTFIDF():
        print(matriceTFIDF("cleaned"))
    def fonction_motnonimportant():
        print(motnonimportant("cleaned"))
    def fonction_motscoreTFIDFMAX():
        print(mot_score_TFIDF_max("cleaned"))
    def fonction_mot_utilise():
        mot=input("Merci de rentrer un mot:")
        print(mot_utilise("cleaned",mot))
    def fonction_mot_repete():
        president=input("Merci de rentrer le nom du president")
        print(mot_repete("cleaned",president))

    def fonction_ecologie_climat():
        liste_president=["Chirac","Mitterrand","Macron","Giscard dEstaing","Hollande","Sarkozy"]
        print(ecologie_climat(liste_president))

    def fonction_mot_hormis_non_important():
        print(mot_hormis_nonimportant("cleaned"))




    print("Menu :")
    print("Taper 1: Noms_president : Cette fonction va vous permettre d'extraire le nom du président avec le nom du fichier fourni")
    print("Taper 2: prenoms : cela va permettre de rentrer le nom d'un president et d'obtenir son prénom")
    print("Taper 3: ConvertirMin : Cette fonction va convertir toutes les majuscules d'une liste de fichiers en minuscule et va les insérer dans de nouveaux documents dans le dossier cleaned")
    print("Taper 4: Ponctuation : Cette fonction va supprimer toutes les ponctuations dans une liste de fichier, merci d'exécuté la fonction ConvertirMin avant celle-là")
    print("Taper 5 : Calcul TF : Cette fonction va calculer le score TF de chaque mot dans un document")
    print("Taper 6 : Calcul IDF : Cette fonction va calculer le score IDF de chaque mot dans le corpus de documents")
    print("Taper 7 : Matrice TF IDF : Cette fonction va calculer le score TF IDF de chaque mot dans chaque document, la compréhension de la lecture de cette matrice est disponible dans la notice d'utilisation")
    print("Taper 8 : mot non important : Cette fonction va retourner une liste de tous les mots non important")
    print("Taper 9 : mot score TF IDF MAX : cette fonction va retourner une liste du mot ou des mots ayant le plus grand score TF IDF")
    print("Taper 10 : mot utilisé : Cette fonction va vous retourner les noms des présidents utilisant le mot demandé")
    print("Taper 11 : mot repete : cette fonction va retourner la liste des ou du mot le plus répété par un president et le nombre de fois qu'il l'a répété ")
    print("Taper 12 : climat ecologie : cette fonction va indiquer le premier président à parler du climat et/ou de l’écologie ")
    print("Taper 13 : mot hormis non important : Cette fonction va indiquer tous les mots que les présidents ont prononcé hormis les mots non importants")

    print("0. Quitter")


    fonction_choisie=int(input("Merci de rentrer le numéro de la fonction que vous souhaitez utiliser:"))
    if fonction_choisie==1:
        fonction_Noms_president()
    elif fonction_choisie==2:
        fonction_prenoms()
    elif fonction_choisie==3:
        fonction_ConvertirMin()
    elif fonction_choisie==4:
        fonction_Ponctuation()
    elif fonction_choisie==5:
        fonction_calculTF()
    elif fonction_choisie==6:
        fonction_calculIDF()
    elif fonction_choisie==7:
        fonction_matriceTFIDF()
    elif fonction_choisie==8:
        fonction_motnonimportant()
    elif fonction_choisie==9:
        fonction_motscoreTFIDFMAX()
    elif fonction_choisie==10:
        fonction_mot_utilise()
    elif fonction_choisie==11:
        fonction_mot_repete()
    elif fonction_choisie==12:
        fonction_ecologie_climat()
    elif fonction_choisie==13:
        fonction_mot_hormis_non_important()




