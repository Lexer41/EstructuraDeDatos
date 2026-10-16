from tkinter import *
from tkinter import messagebox

class principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title('Programa 1 con ventanas') # Titulo
        self.ventana.geometry("400x200") # Tamaño
        # self.ventana.mainloop()
        self.num1 = ""
        self.num2 = ""
        self.a = 0
        self.b = 0
        self.suma = 0

    def validarnumeros(self, valor):
        try:
            self.a = int(valor)
            return True
        except ValueError:
            return False


    def mostrar(self):
        # print('Hola mundo')
        # messagebox.showinfo("Ventana", "Hola mundo") # Lo primero es el titulo de la ventana, y lo segundo es el contenido
        self.num1 = self.n1.get()
        self.num2 = self.n2.get() # Obtener lo de la caja de texto

        if self.validarnumeros(self.num1) and self.validarnumeros(self.num2):
            self.a = int(self.num1)
            self.b = int(self.num2)
            self.suma = self.a + self.b
            messagebox.showinfo("Suma", f"El resultado de la suma es {self.suma}")
            self.n1.delete(0, END)
            self.n2.delete(0, END)
        else:
            messagebox.showerror("Error", "No no son numeros")
            self.n1.delete(0, END) # Borrar el contenido de la caja de texto
            self.n2.delete(0, END)

    def disenio(self):
        Label(self.ventana, text="Escribe un numero").pack()
        self.n1 = Entry(self.ventana)
        self.n1.pack()

        Label(self.ventana, text="Escribe un numero").pack()
        self.n2 = Entry(self.ventana)
        self.n2.pack()

        self.boton1 = Button(self.ventana, text="Suma", command=self.mostrar) # command= La accion que se quiere hacer
        self.boton1.pack()
        
        self.ventana.mainloop() # Se debe de poner al final

if __name__=='__main__':
    app = principal()
    app.disenio()