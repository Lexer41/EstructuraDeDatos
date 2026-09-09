class validaciones():
    def __init__(self):
        pass

    def valNombre(self, a):
        c = 0
        c2 = 0
             
        for i in a:
            if ((ord(i) >= 97 and ord(i) <= 122) or ord(i) == 32):
                c += 1
            if ord(i) >= 65 and ord(i) <= 90:
                c2 += 1
                        
        if c + c2 == len(a):
            esp = a.split(' ') # Separa la cadena por espacios

            if len(esp) == 3: # Cantidad de cadenas
                ns = esp[0]
                if ns[0] == ns[0].upper():
                    ap = esp[1]

                    if ap[0] == ap[0].upper():
                        am = esp[2]

                        if am[0] == am[0].upper():
                            return True
                        else:
                            return False

                    else:
                        return False
                    
                else:
                    return False
                
            else:
                return False
        else:
            return False

    def valCorreo(self, a):
        ar = a.replace(' ', '')

        com = ar[len(ar)-4: ]
        arr = ar.find('@')
        noArr = ar[len(ar) - 5]

        if com == '.com':
            if arr > -1:
                if noArr != '@':
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def valNumero(self, a):
        x = 0
                
        try:
            x = int(a)
            if len(a) == 10:
                return True
            else:
                return False
        except ValueError:
            return False