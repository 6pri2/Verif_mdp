def PresenceChiffre(text): #def recherchant la présence d'un chiffre dans un text
    lst = ['0','1','2','3','4','5','6','7','8','9'] #liste des chiffres pris en compte
    nb = 0 #variable comptant le nbr de chiffre présent dans le texte
    for i in text: # on prend chaque caractère un par un dans la liste de caractère
        if i in lst: #si le caractère selectioné est dans la liste de chiffre
            nb = nb +1 #alors on ajoute 1 au compteur
    if nb > 0: # si le compteur est supérieur à zéro, cela signifie qu'il y a un chiffre de présent dans le texte
        return True #donc on retourne vrai
    else: #sinon si il n'y a pas présence de chiffre
        return False #alors on retourne faux

def Presence3ChiffresMin(text): #def vérifiant la présence de 3 chiffres minimum, sur le même principe que la def "PresenceChiffre"
    lst = ['0','1','2','3','4','5','6','7','8','9'] #on crée la liste des chiffres pris en compte
    nb = 0 #variable comptant e nbr de chiffre présent dans le texte
    for i in text: # on prend chaque caractère un par un dans la liste de caractère
        if i in lst: #si le caractère selectioné est dans la liste de chiffre
            nb = nb +1 #alors on ajoute 1 au compteur
    if nb >= 3: #si il y la présence de 3 chiffres ou plus...
        return True #on retourne vrai
    else: #sinon, il y a donc moins de trois chiffres
        return False #on retourne faux

def Presence4Chiffres(text): #def vérifiant la présence de exactement 4 chiffres lors du test de la date de naissance, elle utilise le même principe que la def "PresenceChiffre" et de la def "Presence3ChiffresMin"
    lst = ['0','1','2','3','4','5','6','7','8','9'] #on crée la liste des chiffres pris en compte
    nb = 0 #variable comptant e nbr de chiffre présent dans le texte
    for i in text: # on prend chaque caractère un par un dans la liste de caractère
        if i in lst: #si le caractère selectioné est dans la liste de chiffre
            nb = nb +1 #alors on ajoute 1 au compteur
    if nb == 4: #si le compteur est exactement à 4 comme l'année de naissance alors...
        return True #on retourne vrai
    else: #sinon si il a plus ou moins de 4 chiffres donc ce n'est pas une année de naissance
        return False #on renvoie faux

def PresenceMaj(text): #def recherchant la présence d'une majuscule dans un texte
    nb = 0 #on crée un compteur, comptant le nombre de majuscule dans le texte
    Maj_autorisee = ['A','B','C','D','E','F','G','H','I','J','K','L','M', #liste des majuscule autorisée
                     'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in text: # on prend chaque caractère un par un dans la liste de caractère
        if (i.upper() == i) and (i.upper() in Maj_autorisee): # si le caractère selectionné est égal au caractère en majuscule et qu'il est dans la liste
            nb = nb +1 #alors on ajoute 1 au compteur
    if nb > 0: #si le compteur est strictement supérieur 0, alors il y a donc la présence d'une majuscule
        return True #on retourne vrai
    else: # sinon cela veut dire qu'il n'y a pas de majuscule
        return False # donc on retourne faux

def PresenceMinus(text): #def recherchant la présence d'un minuscule dans un texte
    nb = 0 #on crée un compteur, comptant le nombre de minuscule dans le texte
    Minus_autorisee = ['a','b','c','d','e','f','g','h','i','j','k','l','m', #liste des minuscules autorisée
                     'n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in text: # on prend chaque caractère un par un dans la liste de caractère
        if (i.lower() == i) and (i.lower() in Minus_autorisee): # si le caractère est égal au caractère en minuscule et qu'il est dans la liste
            nb = nb +1 #alors on ajoute 1 au compteur
    if nb > 0: #si le compteur est strictement supérieur à 0, alors il y a donc la présence d'une minuscule
        return True #on retourne vrai
    else: #sinon, il n'y a donc pas de minuscule
        return False #on retourne faux

def PresenceCaractSpeciaux(text): #def recherchant la présence d'un caractère spécial
    lst = ['#','@','|','~','§','&','"','{','(','[','-','`','_','^',')','°',']','=','}','+','£','$','¤','µ','*','%','!',':',';',',','.'] #liste des carcatères spéciaux accepté
    nb = 0 #on crée un compteur, comptant le nombre de carcatères spéciaux
    for i in text: # on prend chaque caractère un par un dans la liste de caractère
        if i in lst: # si le caractère est dans la liste, cela signifie que c'est un caractère spécial
            nb = nb +1 #on ajoute donc un au compteur
    if nb>0 : # si le compteur est strictement supérieur à 0, alors il y a donc la présence d'un caractère spécial
        return True #on retourne vrai
    else : #sinon il y a donc pas de caractère spécial
        return False #on retourne donc faux

def Presence8CaractMin(text): #def vérifiant qu'il y est minimum 8 caractères
    if len(text) >= 8:#on regarde si la longueur du texte est supérieur ou égal à 8
        return True # si oui alors on renvoie vrai
    else: #sinon, le texte est plus petit
        return False #donc on retourne faux

def Presence25CaractMax(text): #def vérifiant que le texte est plus petit que 25 caractères
    if len(text) >25: # si la longueur du texte est strictement supérieur à 25 caractères :
        return False #alors on retourne faux
    else : #sinon, alors la longueur est inferieur à 25 caractère
        return True #on retourne vrai

def test_mdp(): #def qui test la sécurité d'un mot de passe
    while True: #on crée deux boucles, ici la première vérifie que toutes les conditions sont respectés lors de la saisie du nom par l'utilisateur
        while True : #on crée la seconde boucle, faisant fonctionner le try/except, celui ci servira lors de la saisi de son nom  par l'utilisateur pour qu'il ne puisse pas mettre en panne le script
            try : # on essaye la saisi du nom par l'utilisateur...
                nom=input(str(("Entrez votre nom : "))) #...en format str
                break #si il n'y a pas d'erreur on arrete la seconde boucle
            except ValueError: #si il y a une erreur
                print("Erreur dans votre nom") #on prévient l'utilisateur et la question va être reposé grâce à la seconde boucle
        if PresenceCaractSpeciaux(nom)==False and PresenceChiffre(nom)==False : #on vérifie qu'il n'y a pas de caractères spéciaux ou de chiffres dans le nom grace au def PresenceChiffre et a la def PresenceCaractereSpeciaux
            break#si c'est le cas on arrete la boucle 1
        else : #si il y a présence de caractères speciaux ou chiffres, le nom est donc mal saisie
            print("Une erreur est survenu, rentrer votre nom sans chiffre ni caractère spéciaux") #alors on prévient l'utilisateur et la boucle 1 va se relancer
    assert nom!="", "Erreur, vous n'avez pas rentré votre nom" #on met une assertion si l'utilisateur ne saisi aucune donnée car cette erreur ne sera pas détecter par les précedente vérification
    #on procede maintenant au vérification pour la saisie du prénom, celle ci son les mêmes que pour la saisie du nom
    while True: # on crée 2 boucles, ici la première vérifie que toutes les conditions sont respectés lors de la saisie du prenom par l'utilisateur
        while True : #on crée la seconde boucle, faisant fonctionner le try/except, celui ci servira lors de la saisi de son prenom  par l'utilisateur pour qu'il ne puisse pas mettre en panne le script
            try :# on essaye la saisi du nom par l'utilisateur...
                prenom=input(str(("Entrez votre prenom : "))) #...en format str
                break #si il n'y a pas d'erreur on arrete la seconde boucle
            except ValueError: #si il y a une erreur
                print("Erreur dans votre prenom") #on prévient l'utilisateur et la question va être reposé grâce à la seconde boucle
        if PresenceCaractSpeciaux(prenom)==False and PresenceChiffre(prenom)==False :  #on vérifie qu'il n'y a pas de caractères spéciaux ou de chiffres dans le prenom grace au def PresenceChiffre et a la def PresenceCaractereSpeciaux
            break#si c'est le cas on arrete la boucle 1
        else : #si il y a présence de caractères speciaux ou chiffres, le nom est donc mal saisie
            print("Une erreur est survenu, rentrer votre prénom sans chiffre ni caractères spéciaux") #alors on prévient l'utilisateur et la boucle 1 va se relancer
    assert prenom!="", "Erreur, vous n'avez pas rentré votre prenom" #on met une assertion si l'utilisateur ne saisi aucune donnée car cette erreur ne sera pas détecter par les précedente vérification
    #on procède ici à la vérification de l'année de naissance saisie par l'utilisateur
    while True :  # on crée 2 boucles, ici la première vérifie que toutes les conditions sont respectés lors de la saisie de l'année de naissance par l'utilisateur
        while True : #on crée la seconde boucle, faisant fonctionner le try/except, celui ci servira lors de la saisi de l'année de naissance par l'utilisateur pour qu'il ne puisse pas mettre en panne le script
            try : #on essaye la saisi de l'année de naissance par l'utilisateur ...
                date_naissance=int(input("Entrez votre année de naissance : ")) #...au format int pour les chiffres
                break #si il n'y a pas d'erreur on arrete la seconde boucle
            except ValueError: #si il y a une erreur
                print("Erreur dans votre année de naissance") #on prévient l'utilisateur et la question va être reposé grâce à la seconde boucle
        if date_naissance>=1900 and date_naissance<2023 and Presence4Chiffres(str(date_naissance))==True : #on vérifie ici que l'année de naissance soit compris entre 1900 (record de longévité de 122 ans soit
            #une naissance en 1900, la personne ne peut pas être nait après 2023 car cette année n'est pas commencé. On verifie aussi que l'utilisateur à saisi 4 chiffre, pas plus, pas moins soit une année.
            #on n'a pas besoin de vérifier qu'il n'y est pas de caractères spéciaux ou de lettre car c'est deux erreur dont déjà traité par le try/except
            break#si ces conditions sont respectés, on arrete la boucle 1
        else : #si les conditions évoqué précedement ne sont pas respecté...
            print("Veuiller rentrer une année de naissance correct : entre 1900 et 2022, avec seulement 4 chiffres !")#...on prévient l'utilisateur et le script se relance grâce à la boucle 1
    i=0 #compteur, comptant le nombre de points de sécurités respectés ...
    while i<9: #il y 9 points de sécurité, tant qu'il ne sont pas tous respecté la boucle recommence
        i=0 #on remets le compteur à 0, pour quand la boucle recommence
        while True : #on crée une boucle pour une saisi correcte du mot de passe
            try : #on essaye la saisi du mdp par l'utilisateur ...
                mdp=input(str(("Entrez votre mdp : "))) #...au format str
                break #si il n'y a pas d'erreur on arrete la boucle while true
            except ValueError: #si il y a des erreurs
                ("Erreur dans votre mdp  ") #on prévient l'utilisateur est celui ci devra resaisir son mdp grace à la boucle while true
        #1 sécurité : il ne faut pas qu'il y est le nom de la personne dans le mot de passe
        if nom in mdp or nom.upper() in mdp or nom.capitalize() in mdp or nom.lower() in mdp : #on teste donc la présence du nom tel qu'il la saisi, en majuscule, en minuscule, avec la première lettre
            # en majuscule.
            print("Merci de ne pas mettre votre nom dans le mot de passe !")# si le nom est présent alors on prévient l'utilisateur et la vérification s'arrete, l'utilisateur doit resaisir un nouveau mdp
        else : #sinon
            i=i+1 #on ajoute le point de sécurité au compteur
            #2 sécurité : il ne faut pas la présence du prénom dans le mdp
            if prenom in mdp or prenom.upper() in mdp or prenom.capitalize() in mdp or prenom.lower() in mdp : #on teste donc la présence du prénom tel que l'utilisateur la saisi, en majuscule, en minuscule
                # avec juste la première lettre en majuscule
                print("Merci de ne pas mettre votre prénom dans le mot de passe !") #si le prénom est détecté alors on prévient l'utilisateur, la vérification s'arrete, l'utilisateur doit resaisir un mdp
            else : #sinon
                i=i+1 #on ajoute le point de sécurité au compteur
                #3 sécurité : on vérifie l'absence de l'année de naissance dans le mdp
                if str(date_naissance) in mdp : #si la date de naissance est présente...
                    print("Merci de ne pas mettre votre année de naissance !") #... on prévient l'utilisateur et on ne met pas le points de vérification au compteur
                else : #sinon
                    i=i+1 #on ajoute le point de sécurité au compteur
                #4 sécurité : on vérifie que le mdp n'est pas trop long (plus grand que 25 caractère)
                if Presence25CaractMax(mdp)==False: #on teste cela grace à la def "Presence25CaractMax"
                    print("Votre mot de passe est trop long") #si c'est trop long, on prévient l'utilisateur et on ne met pas le points de vérification au compteur
                else : #sinon
                    i=i+1 #on ajoute le point de sécurité au compteur
                #5 sécurité : on vérifie que le mdp n'est pas trop petit
                if Presence8CaractMin(mdp)==False: #on teste cela grace à la def "Presence8CaractMin"
                    print("Mot de passe incomplet !") #si c'est trop petit, on prévient l'utilisateur et on ne met pas le points de vérification au compteur
                else : #sinon
                    i=i+1 #on ajoute le point de sécurité au compteur
                #6 sécurité : on vérifie la présence d'une majuscule
                if PresenceMaj(mdp)==False: #on teste cela grace à la def "PresenceMaj"
                    print("Il manque une majuscule !") #si il n'y a pas de majuscule,  on prévient l'utilisateur et on ne met pas le points de vérification au compteur
                else : #sinon
                    i=i+1 #on ajoute le point de sécurité au compteur
                #7 sécurité : on vérifie la présence d'une minuscule
                if PresenceMinus(mdp)==False: #on teste grâce à la def "PresenceMinus"
                    print("Il manque un caractère minuscule !") #si il n'y a pas de minuscule,  on prévient l'utilisateur et on ne met pas le points de vérification au compteur
                else : #sinon
                    i=i+1 #on ajoute le point de sécurité au compteur
                #8 sécurité : on vérifie la présence d'un caractère spéciale
                if PresenceCaractSpeciaux(mdp)==False: #on teste grâce à la def "PresenceCarcatSpeciaux"
                    print("Il manque un caractère spécial !") #si il n'y a pas de caractère spécial, on prévient l'utilisateur et on ne met pas le points de vérification au compteur
                else : #sinon
                    i=i+1 #on ajoute le point de sécurité au compteur
                #9 sécurité : on vérifie la présence de 3 chiffres minimum
                if Presence3ChiffresMin(mdp)==False: #on teste grâce à la def "Presence3ChiffresMin"
                    print("Il faut 3 chiffres minimum !") #si il n'y a pas 3 chiffre minimum, on prévient l'utilisateur et on ne met pas le points de vérification au compteur
                else : #sinon
                    i=i+1 #on ajoute le point de sécurité au compteur
                if i<9 : #si tous les points de sécurités ne son pas validés
                    print("Veuillez recommencer ! Seulement",i,"points de sécurités sur 9 !") #on prévient l'utilisateur avec son total de points, et la boucle recommencera, l'utilisateur devra resaisir un mdp
    print("Votre mot de passe est sécurisé !") #arriver ici cela signifie que tous les points de sécurités sont validés, on prévient donc l'utilisateur


test_mdp()