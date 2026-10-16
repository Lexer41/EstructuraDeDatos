#Hacer un programa que mediante ventanas pida un nombre, solo un nombre sin apellidos, si el nombre comiensa con la primer letra en mayuscula
#se agregara a una lista para mostrarlo en una etiqueta o label, si el nombre contiene caracteres incorrectos o no comienza con mayuscula
#mostrara un mensaje de error y no se agregara a la lista

from tkinter import *
from tkinter import messagebox

class principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("400x200")
        self.ventana.title("Practica 10")
        self.lista = []

    def validar(self):
        nomb = self.nom.get()
        l = nomb[0]

        if nomb.isalpha(): #isalpha valida que tanga solo letras sin espacios
            if l.isupper():
                self.lista.append(nomb)
                self.mensaje.config(text=self.lista)
            else:
                messagebox.showerror("Error", "Nombre no valido (Mayuscula inicial)")
                self.nom.delete(0, END)
        else:
            messagebox.showerror("Error", "Nombre no valido (Caracteres)")
            self.nom.delete(0, END)

    def disenio(self):
            Label(self.ventana, text="Programa 10", font=("Times New Roman", 18, "bold")).grid(row=1, column=1, pady=2)
    
            Label(self.ventana, text="Nombre").grid(row=2, column=2, pady=10) #pady y padx, separar los componentes por pixels
            self.nom = Entry(self.ventana, fg="#0B2B30", bg="#B95440")
            self.nom.grid(row=2, column=3, pady=10)
    
            Button(self.ventana, text="Agregar", command=self.validar).grid(row=5, column=1)
    
            self.mensaje = Label(self.ventana, text="", font=("Times New Roman", 18, "bold"))
            self.mensaje.grid(row=7, column=1, pady=2)
    
            self.ventana.mainloop()

if __name__=='__main__':
    app = principal()
    app.disenio()