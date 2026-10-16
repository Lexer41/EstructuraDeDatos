from tkinter import *
from tkinter import messagebox
import time

class principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("400x200")
        self.ventana.title("Practica 11")
        self.n = 0
        self.num = ""

    def agregar(self):
        print(self.lista.size())
        self.num = self.numero.get()

        if len(self.num) == 0:
            messagebox.showerror("Error", "Escribe un numero")
        else:
            if self.validar(self.num):
                self.n = int(self.num)

                self.lista.insert(0, self.n) #Primera parte del insert es para la posicion y la segunda es lo que se quiere agregar
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

    def vaciar1(self):
        #while(True):
        print(self.lista.get(0))
        self.lista.delete(0)
         #time.sleep(1)

        if self.lista.size() < 0:
            return

    def vaciar2(self):
        print(self.lista.get(self.lista.size()-1))
        self.lista.delete(self.lista.size()-1)
        #time.sleep(1)
        
        if self.lista.size() < 0:
            return
        


    def disenio(self):
        Label(self.ventana, text="Programa 11 Listas", font=("Times New Roman", 18, "bold")).place(x=100, y=5)
        Label(self.ventana, text="Escribe un numero").place(x=20, y=50)

        self.numero = Entry(self.ventana)
        self.numero.place(x=20, y=70)

        self.lista = Listbox(self.ventana, height=8, width=15, activestyle="dotbox")
        self.lista.place(x=250, y=50)

        Button(self.ventana, text="Agregar", command=self.agregar).place(x=20, y=100)
        Button(self.ventana, text="Vaciar lista como pila", command=self.vaciar1).place(x=20, y=130)
        Button(self.ventana, text="Vaciar lista como cola", command=self.vaciar2).place(x=20, y=160)
        self.ventana.mainloop()

if __name__=='__main__':
    app = principal()
    app.disenio()