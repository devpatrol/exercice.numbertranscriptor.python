from operations import operation
from number_to_words import *

def translate_number(number):
        words = ""     
        longueur = len(number)
        if longueur==1:
            words = translate_1(number)
        elif longueur==2:
            words = translate_2(number)
        elif longueur==3:
            words = translate_3(number)
        elif longueur==4:
            words = translate_4(number)
        elif longueur==5:
            words = translate_5(number)
        elif longueur==6:
            words = translate_6(number)
        elif longueur==7:
            words = translate_7(number)
        return words
            

def solution(expression):
    forme = well_written(expression)
    if forme == True:
        final = ''
        number = ''
        for e in expression:
            if e in("0123456789"):
                    number += e
            if e == "(":
                final += translate_number(number)
                number = ''
                final += " factor "
            if e == ")":
                final += translate_number(number)
                number = ''
            elif e in ("/*-+.%="):
                if number !='':
                    final += translate_number(number)
                    number = ''
                final += operation(e)
        final += translate_number(number)
        return final
    
T = int(input("NUMER OF TEST "))            
for t in range(T):
    expression = input("EXPRESSION \t ")
    smile = solution(expression)
    print(smile)
    print('\t')