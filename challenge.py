

from unittest import result


def bien_forme(expression):
    acceptable = "0123456789/*-+%."
    bf = True
    nombre_parenthese_ouvrante = expression.count("(")
    nombre_parenthese_fermante = expression.count(")")
    for caractere in expression:
        if caractere not in acceptable:
            print("Mal forme: Caractere non mathematique trouve")
            bf = False
            break

    if (nombre_parenthese_fermante != nombre_parenthese_ouvrante) or ("()" in expression):
        print("Mal forme: (")
        bf = False

    return bf

def translate_1(chaine):   
    valeurs = ['zero','one','two','three','four','five','six','seven','eight','nine']
    indexe = int(chaine)
    resultat = valeurs[indexe]
    return resultat

def translate_2(chaine):
    if chaine[0] == "0":
        return translate_1(chaine[1])
    elif chaine[0] == "1":
        valeurs = ['ten','eleven' ,'twelve' ,'thirteen' ,'fourteen' ,'fifteen' ,'sixteen' ,'seventeen' ,'eighteen' ,'nineteen' ,'twenty']
        indexe = int(chaine[1])
        return valeurs[indexe]
    elif chaine[1] == "0":
        valeurs = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        indexe = int(chaine[0])-2
        return valeurs[indexe]
    else:
        valeurs = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        unite = chaine[0]
        indice_dizaine = int(unite)-2
        dizaine = valeurs[indice_dizaine]
        unite_traduit = translate_1(unite)
        resultat =  dizaine + "-" + unite_traduit
        return resultat

def translate_3(chaine):
    if chaine[0]  == "0":
        return translate_2(chaine[1:])
    elif chaine[1] == "0" and chaine[2]=="0":
        valeurs = ['one hundred','two hundred','three hundred','four hundred','five hundred','six hundred','seven hundred','eight hundred','nine hundred']
        indexe = int(chaine[0])-1
        return valeurs[indexe]
    else:
        valeurs = ['one hundred','two hundred','three hundred','four hundred','five hundred','six hundred','seven hundred','eight hundred','nine hundred']
        reste = chaine[0]
        indice_premier = int(reste)-1
        premier = valeurs[indice_premier]
        reste_traduit = translate_2(chaine[1:])
        resultat =  premier + " and " + reste_traduit
        return resultat

def translate_4(chaine):
    if chaine[0]  == "0":
        return translate_3(chaine[1:])
    elif chaine[1] == "0" and chaine[2]=="0" and chaine[3]=="0":
        valeurs = ['one thousand','two thousand','three thousand','four thousand','five thousand','six thousand','seven thousand','eight thousand','nine thousand']
        indexe = int(chaine[0])-1
        return valeurs[indexe]
    else:
        valeurs = ['one thousand','two thousand','three thousand','four thousand','five thousand','six thousand','seven thousand','eight thousand','nine thousand']
        reste = chaine[0]
        indice_premier = int(reste)-1
        premier = valeurs[indice_premier]
        reste_traduit = translate_3(chaine[1:])
        resultat =  premier + " and " + reste_traduit
        return resultat

def translate_5(chaine):
    if chaine[0]  == "0":
        return translate_4(chaine[1:])
    elif chaine[1] == "0" and chaine[2]=="0" and chaine[3]=="0" and chaine[4]=="0":
        valeurs = ['ten thousand','twenty thousand','thrity thousand','forty thousand','fifty thousand','sixty thousand','seventy thousand','eighty thousand','ninety thousand']
        indexe = int(chaine[0])-1
        return valeurs[indexe]

    elif chaine[0] == "1" and chaine[2]=="0" and chaine[3]=="0" and chaine[4]=="0":
        valeurs = ['eleven thousand','twelve thousand','thirteen thousand','fourteen thousand','fifteen thousand','sixteen thousand','seventeen thousand','eighteen thousand','nineteen thousand']
        indexe = int(chaine[1])-1
        return valeurs[indexe]

    elif chaine[0] == "1":
        valeurs = ['eleven thousand','twelve thousand','thirteen thousand','fourteen thousand','fifteen thousand','sixteen thousand','seventeen thousand','eighteen thousand','nineteen thousand']
        indice_premier = int(chaine[1])-1
        premier = valeurs[indice_premier]
        reste_traduit = translate_3(chaine[2:])
        resultat =  premier +" "+ reste_traduit
        return resultat
        
    else:
        valeurs = ["twenty thousand", "thirty thousand", "forty thousand", "fifty thousand", "sixty thousand", "seventy thousand", "eighty thousand", "ninety"]
        if chaine[1] == "0" and chaine[2]=="0" and chaine[3]=="0" and chaine[4]=="0":
            indexe = int(chaine[0])-2
            return valeurs[indexe]
        
        else:
            indice_premier = int(chaine[0])-2
            premier = valeurs[indice_premier]
            reste_traduit = translate_4(chaine[1:])
            resultat =  premier  +" "+ reste_traduit
            return resultat

def translate_6(chaine):
    if chaine[0]  == "0":
        return translate_5(chaine[1:])
    elif chaine[1] == "0" and chaine[2]=="0":
        valeurs = ['one hundred','two hundred','three hundred','four hundred','five hundred','six hundred','seven hundred','eight hundred','nine hundred']
        indexe = int(chaine[0])-1
        return valeurs[indexe]
    else:
        valeurs = ['one hundred','two hundred','three hundred','four hundred','five hundred','six hundred','seven hundred','eight hundred','nine hundred']
        reste = chaine[0]
        indice_premier = int(reste)-1
        premier = valeurs[indice_premier]
        reste_traduit = translate_5(chaine[1:])
        resultat =  premier + " " + reste_traduit
        return resultat

        
        












def solution(expression):
    longueurs = [1,2,3,4,5,6,7,8,9]
    forme = bien_forme(expression)
    if forme == True:
        longueur = len(expression)
        if longueur==1:
            print(translate_1(expression))
        if longueur==2:
            print(translate_2(expression))
        if longueur==3:
            print(translate_3(expression))
        if longueur==4:
            print(translate_4(expression))
        if longueur==5:
            print(translate_5(expression))
        if longueur==6:
            print(translate_6(expression))
        
        


expression = input("Entrer l'expression mathematique ")
solution(expression)
