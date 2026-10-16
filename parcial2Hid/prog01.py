class principal():
    def __init__(self):
        self.numero = 0

    def leer(self):
        a = input('Escribe un numero\n')
        try:
            self.numero = int(a)
            print('Si es un numero')
        except ValueError:
            print('Error no es un numero')
            return self.leer()
        
if __name__=='__main__':
    app = principal()
    app.leer()