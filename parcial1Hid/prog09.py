import sys

def validarNumerosEnteros(x):
    a = 0

    try:
        a = int(x)
        return True
    except ValueError:
        print("No son numeros enteros")
        return False

def validarNumerosDecimales(x):
    a = 0
    
    try:
        a = float(x)
        return True
    except ValueError:
        print("No son numeros decimales")
        return False

def validarLetras(x):
    if x.isupper():
        print("Son mayusculas")
        return True
    elif x.islower():
        print("Son minusculas")
        return True
    else:
        return False

def inicio():
    a = input("Ecribe un dato ")

    if validarLetras(a):
        print("Son letras")
    elif validarNumerosEnteros(a):
        print("Son numeros enteros")
    elif validarNumerosDecimales(a):
        print("Son numeros con decimales")
    else:
        print("Son tipos de datos distintos a los anteriores")

    sys.exit()

if __name__=="__main__":
    inicio()