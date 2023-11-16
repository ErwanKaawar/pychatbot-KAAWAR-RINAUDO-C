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