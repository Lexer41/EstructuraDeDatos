from tkinter import *
from tkinter import messagebox

class principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("400x200")
        self.ventana.title("Practica 9")
        self.lista = []
        self.x1 = ""
        self.x2 = ""

    def validarNumeros(self, v):
        a = 0
        try:
            a = int(v)
            return True
        except ValueError:
            messagebox.showerror("Error", "no es un numero")
            return False

    def encontrarNumeros(self, w):
        print(int(w))

        if int(w) >= int(self.x2) - 1:
            print('Hola')
            return
        else:
            self.lista.append(int(w) + 1)
            return self.encontrarNumeros(int(w) + 1)

    def mostrarNumeros(self):
        n1 = self.n1.get()
        n2 = self.n2.get()

        if(self.validarNumeros(n1) or self.validarNumeros(n2)):
            if int(n1) < int(n2):
                self.x1 = n1
                self.x2 = n2
                self.encontrarNumeros(self.x1)
                #for i in range(int(n1), int(n2)):
                    #self.lista.append(i)
                self.mensaje.config(text=self.lista)
            else:
                messagebox.showerror("Error", "El primer numero debe ser menor al segundo")
                self.n1.delete(0, END)
                self.n2.delete(0, END)

    def disenio(self):
        Label(self.ventana, text="Programa 9", font=("Times New Roman", 18, "bold")).grid(row=1, column=1, pady=2)

        Label(self.ventana, text="Numero 1").grid(row=2, column=2, pady=10) #pady y padx, separar los componentes por pixels
        self.n1 = Entry(self.ventana, fg="#0B2B30", bg="#B95440")
        self.n1.grid(row=2, column=3, pady=10)

        Label(self.ventana, text="Numero 2").grid(row=3, column=2)
        self.n2 = Entry(self.ventana, fg="#0B2B30", bg="#B95440")
        self.n2.grid(row=3, column=3)

        Button(self.ventana, text="Mostrar", command=self.mostrarNumeros).grid(row=5, column=1)

        self.mensaje = Label(self.ventana, text="", font=("Times New Roman", 18, "bold"))
        self.mensaje.grid(row=7, column=1, pady=2)

        self.ventana.mainloop()

if __name__=='__main__':
    app = principal()
    app.disenio()