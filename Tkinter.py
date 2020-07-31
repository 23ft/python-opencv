from tkinter import *


raiz = Tk()
raiz.title("Opencv")
#raiz.iconbitmap("logo.ico")


frame1 = Frame(raiz)
frame1.config(width=500, height=500,bd = 40)
frame1.pack()


Label(frame1, text= "Opencv-Client",justify="center").grid(row= 0, 
                                                           column= 1, 
                                                           padx=30, 
                                                           pady=10)        


LabelNombre = Label(frame1, text= "Name:", font= (30))
LabelNombre.grid(row = 1, column = 0)
CuadroNombre = Entry(frame1)
CuadroNombre.grid(row = 1, column = 1, padx= 10)


Label(frame1, text="Password:", font= (30)).grid(row= 2, column= 0)
Entry(frame1, show="*").grid(row= 2, column= 1,padx= 10)


#Funcion para cada boton!
def UbiImage():
    valor = CuadroNombre.get()
    valor2 = int(valor)
    print(type(valor2))

button = Button(raiz, text="Obtener texto",
    command=UbiImage)
button.pack()


#Bucle Infinito
raiz.mainloop()




