import os
from FonctionsProjet import *
if __name__ == '__main__':
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    print(files_names)
    #print(convertirMin(files_names)) # Crée 8 nouveaux fichiers avec texte minuscule
    #print(Ponctuation(files_names))
    #print(matriceTFIDF('cleaned'))
    #print(calculIDF('cleaned'))
    #print(motnonimportant('cleaned'))
    print(moteleve('cleaned'))
    print(mot_utilise('cleaned',"nation"))
    print(nom_fichier('cleaned','Chirac'))
    print(mot_repete('cleaned','Chirac'))
    #print(mot_hormis_nonimportant('cleaned'))

