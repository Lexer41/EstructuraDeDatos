# Hacer un programa que lea nombre, apellido paterno, y apellido materno dentro de una variable, a continuacion
# pedira correo electronico y telefono de la persona.
# Estos datos tienen que estar previamente validados de lo contrario se volveran a pedir.
# Las validaciones son las siguientes:
# 1. Solo puede tener un nombre y sus apellidos
# 2. Cada elemento del nombre debe comenzar con mayuscula
# 3. el correo electronico permite cualquier tipo de caracter pero obligatoriamente debe llevar una sola @ y terminar con .com
# 4. El telefono son unicamente numeros y obligatoriamente 10 digitos

from prog13Validaciones import validaciones

class programa():
    def __init__(self):
        self.val = validaciones()

    def datos(self):
        self.nombreCom = input('Escribe el nombre, apellido paterno y materno (con mayusculas las primeras letras)\n')
        while(True):
            if self.val.valNombre(self.nombreCom):
                break
            else:
                self.nombreCom = input('Nombre no valido, haslo otra vez\n')


        self.correo = input('Escribe el correo electronico\n')
        while(True):
            if self.val.valCorreo(self.correo):
                break
            else:
                self.correo = input('Correo no valido, haslo otra vez\n')

        self.telefono = input('Escribe el numero de telefono\n')
        while(True):
            if self.val.valNumero(self.telefono):
                break
            else:
                self.telefono = input('Telefono no valido, haslo otra vez\n')

if __name__=='__main__':
    app = programa()
    app.datos()

    corEsp = app.correo
    corEsp = corEsp.replace(' ', '')
    print(f'Nombre: {app.nombreCom}\nCorreo: {corEsp}\nTelefono: {app.telefono}')