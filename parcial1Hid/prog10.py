# Hacer un programa que pida una cantidad en pesos (numeros con decimales) el programa validara que sea un numero correcto
# y si el dato es correcto calculara y mostrara su equivalente en dolares y euros si el numero es incorrecto se volvera a pedir.
# El programa no termian hasta que muestre en pantalla los resultados solicitados

def validarNumEnt(n):
    a = 0

    try:
        a = int(n)
        return True
    except ValueError:
        return False

def validarNumDes(n):
    a = 0
    
    try:
        a = float(n)
        return True
    except ValueError:
        return False

def pesos():
    nv = False
    num = 0
    dol = 0
    eur = 0

    while(nv == False):
        num = input("Escribe una cantidad en pesos (Desimal)\n")

        if validarNumEnt(num):
            print("Respuesta no valida, vuelve a intentarlo")
            nv = False
        elif validarNumDes(num):
            num = float(num)

            dol = num / 17.01
            eur = num / 19.69
            nv = True
        else:
            print("Respuesta no valida, vuelve a intentarlo")
            nv = False

    print(f"La cantidad en pesos introducida fue de {num} \n La cantidad en dolares es {dol} \n La cantidad en euros es {eur}")

if __name__=="__main__":
    pesos()


# i = a.find('.') encontrar caracteres
# si es mayor a -1 encontro el punto en la cadena si es -1 significa es que no