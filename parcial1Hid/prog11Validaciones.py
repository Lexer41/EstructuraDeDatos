class validaciones():
    def __init__(self):
        pass

    def validarLetras(self, a):
        c = 0
        c2 = 0
        
        for i in a:
            if (ord(i) >= 97 and ord(i) <= 122) or ord(i) == 32: #32 es el espacio
                    c += 1
            if ord(i) >= 65 and ord(i) <= 90:
                c2 += 1
        
        if c + c2 == len(a):
            return True
        else:
            return False

    def validarNumeros(self, x):
        a = 0
        
        try:
            a = int(x)
            return True
        except ValueError:
            print("No son numeros enteros")
            return False

    def validarNumerosConDecimales(self, a):
        i = a.find('.')
        
        if i == -1:
            return False
        else:
            try:
                v = float(a)
                return True
            except ValueError:
                return False