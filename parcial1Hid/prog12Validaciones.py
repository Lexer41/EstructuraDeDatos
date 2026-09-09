class validaciones():
    def __init__(self):
        pass

    def validarNombre(self, a):
        c = 0
        c2 = 0
     
        for i in a:
            if ((ord(i) >= 97 and ord(i) <= 122) or ord(i) == 32):
                c += 1
            if ord(i) >= 65 and ord(i) <= 90:
                c2 += 1
                
        if c + c2 == len(a):
            return True
        else:
            return False

    def validarFecha(self, a):
        pd = a.find('/')

        if pd == -1:
            return False
        elif pd == 0:
            return False
        elif pd == len(a)-1:
            return False
        else:
            na = a.replace('/','')
            try:
                fecha = int(na)
                return True
            except ValueError:
                return False

    def validarPrecio(self, a):
        i = a.find('.')
                
        if i == -1:
            return False
        else:
            try:
                v = float(a)
                return True
            except ValueError:
                return False