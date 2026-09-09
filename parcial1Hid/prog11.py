from prog11Validaciones import validaciones

class programa():
    def __init__(self):
        self.val = validaciones()

    def pedirDatos(self):
        self.nombre = input("Escribe el nombre\n")
        self.edad = input("Escribe una edad\n")
        self.estatura = input('Escribe la estatura de la persona\n')

        if self.val.validarLetras(self.nombre):
            print('El nombre es correcto...')
        else:
            print('Error con el nombre')
        if self.val.validarNumeros(self.edad):
            print('La edad es correcta')
        else:
            print('Error con la edad')
        if self.val.validarNumerosConDecimales(self.estatura):
            print('La estatura es correcta')
        else:
            print('Error con la estatura')


if __name__=='__main__':
    while(True):
        app = programa()
        app.pedirDatos()

        res = input('Deseas intentar otra vez s/n\n')

        if res == 'N' or res == 'n':
            break