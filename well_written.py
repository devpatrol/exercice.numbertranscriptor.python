

def well_written(expression):
    acceptable = "0123456789/*-+%.()="
    bf = True
    nombre_parenthese_ouvrante = expression.count("(")
    nombre_parenthese_fermante = expression.count(")")
    for caractere in expression:
        if caractere not in acceptable:
            print("Mal forme: Caractere intrus")
            bf = False
            break

    if (nombre_parenthese_fermante != nombre_parenthese_ouvrante) or ("()" in expression):
        print("Mal forme: (")
        bf = False
    if (expression.count("=") > 1) or ("()" in expression):
        print("Mal forme: =")
        bf = False

    return bf