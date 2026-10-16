#Hacer un programa que lea un numero que puede ser positivo o negativo, debe de haber dos listas, una para numeros negativos y otra para mostrar
#numeros positivos. Dependiendo del valor que se intrdusca se mostrara en su lista correspondiente.
#Abajo de cada lista aparecera un boton para vaciarlas de la siguiente manera:
#Los numeros negativos se vaciara en forma de pilas, mientras que los positivos se vaciara en forma de cola

from tkinter import *
from tkinter import messagebox
import time

class principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("400x200")
        self.ventana.title("Practica 12")
        self.n = 0
        self.num = ""

    def agregar(self):
        self.num = self.numero.get()

        if len(self.num) == 0:
            messagebox.showerror("Error", "Escribe un numero")
        else:
            if self.validar(self.num):
                self.n = int(self.num)

                if self.n >= 0:
                    self.lisNumPos.insert(0, self.n)
                    self.numero.delete(0, END)
                else:
                    self.lisNumNeg.insert(0, self.n)
                    self.numero.delete(0, END)

    def validar(self, a):
        nn = 0
        
        try:
            nn = int(a)
            return True
        except ValueError:
            messagebox.showerror("Error", "No es un numero")
            self.numero.delete(0, END)
            return False

    def elimNumPos(self):
        while(True):
            self.lisNumPos.delete(self.lisNumPos.size()-1)
            self.lisNumPos.update()
            time.sleep(0.5)
        
            if self.lisNumPos.size() <= 0:
                break
        return

    def elimNumNeg(self):
        while(True):
            self.lisNumNeg.delete(0)
            self.lisNumNeg.update()
            time.sleep(0.5)
                
            if self.lisNumNeg.size() <= 0:
                break
        return

    def disenio(self):
        Label(self.ventana, text="Programa 12", font=("Times New Roman", 18, "bold")).place(x=100, y=5)
        Label(self.ventana, text="Escribe un numero").place(x=20, y=50)
        
        self.numero = Entry(self.ventana)
        self.numero.place(x=20, y=70)
        
        self.lisNumNeg = Listbox(self.ventana, height=8, width=15, activestyle="dotbox")
        self.lisNumNeg.place(x=150, y=50)

        self.lisNumPos = Listbox(self.ventana, height=8, width=15, activestyle="dotbox")
        self.lisNumPos.place(x=250, y=50)

        Button(self.ventana, text="Elimiar numeros negativos", command=self.elimNumNeg).place(x=110, y=150)
        Button(self.ventana, text="Elimiar numeros positivos", command=self.elimNumPos).place(x=250, y=150)
        
        Button(self.ventana, text="Agregar", command=self.agregar).place(x=20, y=100)

        self.ventana.mainloop()

if __name__=='__main__':
    app = principal()
    app.disenio()