from tkinter import *
from tkinter import messagebox

class principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("400x200")
        self.ventana.title("Practica 8")
        self.ventana.configure(bg="#B95440") #Poner un color en el background
        self.lista = []
        #self.ventana.mainloop()

    def calcular(self):
        n1 = self.n1.get()
        n2 = self.n2.get()

        if (len(n1) == 0 or len(n2) == 0):
            messagebox.showerror("Error", "faltan datos")
        else:
            self.lista.append(n1 + " _ " + n2)
            self.mensaje.config(text= self.lista)
            self.n1.delete(0, END)
            self.n2.delete(0, END)


    def cerrar(self):
        print("Cerrar ventana")
        self.ventana.destroy() #Cerrar ventana

    def disenio(self):
        #font: para cambiar el tipo de letra, cambiar el tamaño y el bold es para las negritas
        Label(self.ventana, text="Practica 8", font=("Arial", 18, "bold"), fg="#0B2B30", bg="#B95440").place(x=100, y=10) #Colocarlo en coordenadas en ves de poner pack()

        Label(self.ventana, text="Escribe un numero", fg="#0B2B30", bg="#B95440").place(x=10, y=50) # fg color de letras, bg para el background
        self.n1 = Entry(self.ventana, fg="#0B2B30", bg="#B95440")
        self.n1.place(x=125, y=50)

        Label(self.ventana, text="Escribe otro numero", fg="#0B2B30", bg="#B95440").place(x=10, y=80)
        self.n2 = Entry(self.ventana, fg="#0B2B30", bg="#B95440")
        self.n2.place(x=125, y=80)

        # width: Tamaño de los botones
        Button(self.ventana, text="Calcular", command=self.calcular, fg="#0B2B30", bg="#B95440", width=10).place(x=130, y=120)

        Button(self.ventana, text="cerrar", command=self.cerrar, fg="#0B2B30", bg="#B95440", width=10).place(x=220, y=120)

        self.mensaje = Label(self.ventana, text="", font=("Arial", 18, "bold"), fg="#0B2B30", bg="#B95440")
        self.mensaje.place(x=100, y=150) #Si tiene el place no puedes modificar, asi que en este caso se hace por separado

        self.ventana.mainloop()

if __name__=='__main__':
    app = principal()
    app.disenio()