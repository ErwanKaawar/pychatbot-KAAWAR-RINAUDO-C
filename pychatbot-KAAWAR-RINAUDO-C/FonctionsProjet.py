def noms_president(liste_nom_fichier): #Extraire les noms des présidents à partir des noms des fichiers texte fournis
    liste_noms=[]
    for k in liste_nom_fichier:
        nom=""
        Trouve=True
        i=0
        while Trouve:
            i+=1
            if k[i]=='_':
                k=k[i+1:len(k)]
                Trouve=False
    #Dans le code ci-dessus on a enlevé tout ce qui se trouvait avant le Nom
        i=0
        while 65<=ord(k[i])<=90 or 97<=ord(k[i])<=122:
            nom = nom + k[i]
            i+=1
        liste_noms.append(nom)
    return liste_noms
        #Et Dans celui-ci on a enlevé tout ce qui se trouvait après le nom c'est à dire tout les termes non alphabétiques

def prenoms(nom_president): #Ce code va permettre de récuperer le prénom d'un président à l'aide de son nom
    dico_prenom_nom={"Chirac":"Jacques","Giscrad d’Estaing":"Valéry","Mitterrand":"François","Macron":"Emmanuel","Sarkozy":"Nicolas"}
    for cle,valeurs in dico_prenom_nom.items():
        if nom_president==cle:
            return valeurs

def noms(liste_nomfichier):
    liste=noms_president(liste_nomfichier)
    return liste
nom_fichierr ='../Nomination_Chirac1.txt'
f=open(nom_fichierr,"w")
contenu=f.read()
print(contenu)
