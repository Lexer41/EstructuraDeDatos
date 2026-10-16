import time

class principal():
    def __init__(self):
        self.numeros = []

    def llenarLista(self):
        while(True):
            self.numeros.append(int(input(f'Escribe un numero\n')))
            print(f'La lista tine {len(self.numeros)} de elementos')
            res = input('Deseas otro numero s/n \n')

            if res == 'n' or res == 'N':
                break

    def mostrarLista(self):
        print('Mostrar Arreglo')
        print(self.numeros)

if __name__=='__main__':
    clase = principal()
    clase.llenarLista()
    clase.mostrarLista()