class validar():
    def __init__(self):
        pass

    def validarNombre(self, n): # Aqui se puede poner tanto letras como numeros, caracteres especiales no
        c = 0

        for i in n:
            if ord(i) >= 48 and ord(i) <= 57:
                c += 1
            if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122) or (ord(i) == 32):
                c += 1

        if c == len(n):
            return True
        else:
            return False

    def validarCantidades(self, c):
        ca = 0

        try:
            ca = int(c)
            return True
        except ValueError:
            return False

    def validarPrecio(self, c):
            ca = 0.0
    
            try:
                ca = float(c)
                return True
            except ValueError:
                return False