from tkinter import *
from tkinter import messagebox

class principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title('Programa 1 con ventanas') # Titulo
        self.ventana.geometry("400x200") # Tamaño
        # self.ventana.mainloop()

    def mostrar(self):
        print('Hola mundo')
        messagebox.showinfo("Ventana", "Hola mundo") # Lo primero es el titulo de la ventana, y lo segundo es el contenido

    def disenio(self):
        self.boton1 = Button(self.ventana, text="Aceptar", command=self.mostrar)
        self.boton1.pack()
        self.ventana.mainloop() # Se debe de poner al final

if __name__=='__main__':
    app = principal()
    app.disenio()