from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror


def Cerrar():
    madre.destroy()
    showerror(title="Adios", 
              message="Adios, para siempre...")
    
def Inicio():
    madre.destroy()
    
    madre2 = Tk()
    madre2.title("Bienvenida")
    madre2.geometry("500x500")
    madre2.resizable(0,0)
    madre2.config(bg = "Black",
                  bd= 30,
                  relief= "ridge")

    showinfo(title= "Script 0X002_0x02", 
             message="Gracias por continuar :) Se abrira la nueva ventana. 20x020x00")
             
    madre2.mainloop()
    
 

#Ventana Raiz.
madre = Tk()
madre.title("Mensaje De Recuperacion")
madre.geometry("700x500")
madre.resizable(0,0)
#Coniguracion Ventana.
madre.config(bg= "black", bd= 20, relief= "sunken")

wid1 = Frame(madre)
wid1.place(x= 250, y= 200 )
wid1.config(width= 100, height= 100, bg= "white", bd= 5, relief= "raised")

botonini = Button(wid1,
                  text= "¿Quieres Iniciar?", 
                  command= Inicio,
                  activeforeground= "red",
                  relief="flat",
                  overrelief="raised").grid(row= 0, column= 0)

bottonf = Button(madre, 
                 text= "Salir? :c", 
                 command= Cerrar, 
                 padx= 5, 
                 pady= 5,  
                 font=("Console", 10), 
                 activebackground= "red",
                 activeforeground= "green",
                 bd= 6,
                 relief="flat",
                 overrelief="raised").place(x= 550, y= 400)





madre.mainloop()

