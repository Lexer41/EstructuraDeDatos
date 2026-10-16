import time

class principal():
    def __init__(self):
        self.numeros = [0,0,0,0,0,0,0,0,0,0]

    def llenarArreglo(self):
        for i in range(0, 10):
            self.numeros[i] = int(input(f'Escribe un numero en la posicion {i}\n'))

    def mostrarArreglo(self):
        print('Mostrar Arreglo')
        for i in self.numeros:
            print(f'{ i }')

    def pilas(self):
        print('PILAS')
        pos = len(self.numeros)-1
        while(pos >= 0):
            print(f'EL arreglo {self.numeros[pos]}')
            self.numeros[pos] = 0
            time.sleep(1)
            print(f'EL arreglo actualizado {self.numeros[pos]}')
            pos -= 1

    def colas(self):
        print('COLA')
        for i in range(0, len(self.numeros)-1):
            print(f'EL arreglo {self.numeros[i]}')
            self.numeros[i] = 0
            time.sleep(1)
            print(f'EL arreglo actualizado {self.numeros[i]}')

if __name__=='__main__':
    clase = principal()
    clase.llenarArreglo()
    #clase.pilas()
    clase.colas()
    #clase.mostrarArreglo()