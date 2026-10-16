from tkinter import *
from tkinter import messagebox
import time
from validarProg13 import validar

class principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("400x200")
        self.ventana.title("Practica 13")
        self.dato = ""
        self.objeto = validar()
    
    def agregar(self):
        if self.objeto.validarNombre(self.producto.get()):
            if self.objeto.validarPrecio(self.precio.get()):
                if self.objeto.validarCantidades(self.cantidad.get()):
                    self.dato = self.producto.get() + " _ " + self.precio.get() + " _ " + self.cantidad.get() + " _ " + (str(float(self.precio.get()) * float(self.cantidad.get())))
                    self.lista.insert(self.lista.size()+1, self.dato)

                    self.producto.delete(0, END)
                    self.precio.delete(0, END)
                    self.cantidad.delete(0, END)

                    messagebox.showinfo("Correcto", "El producto se ha agregado")
                else:
                    messagebox.showerror("Error", "El dato es incorrecto")
                    self.cantidad.delete(0, END)
            else:
                messagebox.showerror("Error", "El dato es incorrecto")
                self.precio.delete(0, END)
        else:
            messagebox.showerror("Error", "El dato es incorrecto")
            self.producto.delete(0, END)

    def elegir(self):
        seleccion = self.lista.curselection() #Agarra lo que se tiene seleccionado en la lista

        if not seleccion: # cuando no hay nada seleccionado
            messagebox.showerror("Error", "Primero elige un elemento")
        else:
            renglon = self.lista.get(seleccion[0])
            print(renglon)
            r = renglon.split(" _ ")
            messagebox.showinfo("Ventana", f"El producto es: {r[0]} \nEl precio es: {r[1]} \nLa cantidad: {r[2]} \nEl total: {r[3]}")

    def eliminar(self):
        seleccion = self.lista.curselection()
        
        if not seleccion:
            messagebox.showerror("Error", "Primero elige un elemento")
        else:
            indice = seleccion[0]
            self.lista.delete(indice)
            messagebox.showinfo("Eliminar", "El dato a sido eliminado")

    def disenio(self):
        Label(self.ventana, text="Programa 13", font=("Times New Roman", 18, "bold")).place(x=100, y=5)

        Label(self.ventana, text="Escribe un producto").place(x=20, y=50)        
        self.producto = Entry(self.ventana)
        self.producto.place(x=20, y=70)

        Label(self.ventana, text="Escribe un precio").place(x=20, y=95)        
        self.precio = Entry(self.ventana)
        self.precio.place(x=20, y=115)

        Label(self.ventana, text="Escribe una cantidad de productos").place(x=20, y=140)        
        self.cantidad = Entry(self.ventana)
        self.cantidad.place(x=20, y=165)

        self.lista = Listbox(self.ventana, height=8, width=25, activestyle="dotbox")
        self.lista.place(x=240, y=50)

        Button(self.ventana, text="Agregar", command=self.agregar).place(x=160, y=70)
        Button(self.ventana, text="Seleccionar", command=self.elegir).place(x=160, y=100)
        Button(self.ventana, text="Eliminar", command=self.eliminar).place(x=160, y=130)

        self.ventana.mainloop()

if __name__=='__main__':
    app = principal()
    app.disenio()