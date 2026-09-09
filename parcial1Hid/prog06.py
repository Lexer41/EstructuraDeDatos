# Hacer un programa que pida 10 veces una letra y muestre en pantalla todas esas letras en una sola linea

resultado = ""

for x in range(1, 11):
    a = input("Escribe una letra: ")
    resultado = resultado + a

print(f"Aqui estan las letras: {resultado} y la longitud es de {len(resultado)}")