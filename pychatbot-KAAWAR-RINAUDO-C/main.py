import os
from FonctionsProjet import *
if __name__ == '__main__':
    phrase = "Vif juge trempez ce blond whisky aqueux"
    print(noms_president("Nomination_Sarkozy87.txt"))
    print(prenoms("Sarkozy"))
    print(prenoms("Sarkozy"))
    print(prenoms("Sarkozy"))
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    print(files_names)
    print(convertirMin(files_names)) # Crée 8 nouveaux fichiers avec texte minuscule
