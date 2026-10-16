# Hacer un programa que lea el nombre, edad y peso de una persona, el programa validara los datos mediante metodos
# recursivos y ademas mostrara la conversion del peso de kilos a libras donde libra son 2.5 kg.
# EL programa no termina hasta que todos los datos sean correctos

class programa():
    def __init__(self):
        self.nom = ""
        self.eda = ""
        self.pes = ""

    def nombre(self):
        self.nom = input('Escribe un nombre\n')
        c = 0
        c2 = 0
        
        for i in self.nom:
            if (ord(i) >= 97 and ord(i) <= 122) or ord(i) == 32: #32 es el espacio
                    c += 1
            if ord(i) >= 65 and ord(i) <= 90:
                c2 += 1
        
        if c + c2 == len(self.nom):
            return self.edad()
        else:
            print('Nombre no valido')
            return self.nombre()

    def edad(self):
        self.eda = input('Escribe la edad\n')
        a = 0
        
        try:
            a = int(self.eda)
            return self.peso()
        except ValueError:
            print("Edad no valida")
            return self.edad()

    def peso(self):
        self.pes = input('Escribe el peso\n')
        i = self.pes.find('.')
        
        if i == -1:
            print('peso no valido')
            return self.peso()
        else:
            try:
                v = float(self.pes)
                print(f'El peso en libras son {v * 2.5}')
            except ValueError:
                print('peso no valido')
                return self.peso()

if __name__=='__main__':
    app = programa()
    app.nombre()