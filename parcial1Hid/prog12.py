# Hacer un programa que lea nombre de un product, fecha de caducidad que solo contendra
# mes y año y su respectivo precio.
# una vez validado los datos el programa mostrara un mensaje indicando si decean otro producto,
# si es asi vuelve a hacer el mismo proceso de lo contrario mostrara el total de los precios,
# la cantidad de productos y el total con IVA
from prog12Validaciones import validaciones

class programa():
    def __init__(self):
        self.val = validaciones()
        
    
    def datos(self):
        self.nombre = input('Escribe el nombre del producto\n')

        while(True):
            if(self.val.validarNombre(self.nombre)):
                break
            else:
                self.nombre = input('Nombre no valido haslo otra vez\n')

        self.fecha = input('Escribe la fecha del producto(MM/DD)\n')

        while(True):
            if(self.val.validarFecha(self.fecha)):
                break
            else:
                self.fecha = input('Fecha no valida haslo otra vez\n')

        self.precio = input('Escribe el precio del producto\n')

        while(True):
            if(self.val.validarPrecio(self.precio)):
                break
            else:
                self.precio = input('Precio no valido haslo otra vez\n')
            

if __name__=='__main__':
    cantPres = 0.0
    cantProd = 0

    while(True):
        app = programa()
        app.datos()
        
        precio = float(app.precio)

        cantPres += precio
        cantProd += 1
        
        r = input('Queres otro producto(s/n)\n')

        if r == 'N' or r == 'n':
            break

    print(f'La cantidad de todos los productos es {cantPres}\nLa cantidad de productos son {cantProd}\nEl total con el IVA es {cantPres * 1.16}')