from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
import cv2

#24-py the serie.

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
###Esta funcion ejecuta la imagen para poderla visualizar como el "bonus"
def bonus():
    img = cv2.imread("5257613_300x300.jpeg")
    cv2.imshow("Bonus", img)
    showinfo(title= "Bienvenida", message="Acabas de abrir la pista #1, guardalas!")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#---------------------------------------------------------------------------
###Se encarga de destruir la ventana "madre" y lanza error.       
def Cerrar():
    madre.destroy()
    showerror(title="Adios", 
              message="Adios, para siempre...")
#---------------------------------------------------------------------------
###Selecciona la respuesta y la condiciona, abriendo en dado caso la ventana o el error.
def Seleccion_datos():
    
    global seleccion
    
    def Accion_boton():
        global dato
        
        dato= seleccion.get()
        if dato == ("Si"):
            import webbrowser
            madre4.destroy()
            webbrowser.open("https://docs.google.com/forms/d/e/1FAIpQLSda3JgeMtKc30gEbOdS0V4aDgUpvhGUMRUgH7LoBBPxPUHqTA/viewform?usp=sf_link")
            
        else:
            madre4.destroy()
            showerror(title= "Adios", message="Gracias por abrir la aplicacion, adios")
            
    madre2.destroy()
    
    madre4 = Tk()
    madre4.title("Envia tu seleccion")
    madre4.geometry("600x150")
    madre4.resizable(0,0)
    madre4.config(bg = "gray",
                  bd= 30,
                  relief= "ridge")
    
    Label(madre4, text= "Envia 'Si' si quieres ser parte, 'No' si no quieres ser parte!", font="console 10").place(x= 10,y=10)

    
    seleccion= Entry(madre4, width= 10)
    seleccion.place(x= 80, y= 50)
    
    boton_final= Button(madre4, text= "Enviar", command= Accion_boton)
    boton_final.place(x= 200, y= 50)
    
    madre4.mainloop()
#---------------------------------------------------------------------------
###Continua con la rutina remplazando mensajes y contenido dentro de los text, añadiendo uno nuevo.      
def Continuacion():
    texto_mostrar.delete('1.0', END)
    texto_mostrar.insert(INSERT, "MENSAJE BORRADO\n\nRecuperando mensaje de RIESGO\n\nMensaje: Estamos en tus manos!")
    texto_mostrar2 = Text(frame2, 
                         width= 45, 
                         height= 10,
                         font="console 9 bold",
                         bg= "black",
                         foreground= "white",
                         state= NORMAL,
                         bd= 5,
                         relief= "sunken")
    texto_mostrar2.place(x=20, y=210)
    texto_mostrar2.insert(INSERT,"Hola Nathalia soy yo rover, paso algo...\nSimplemente ya no me llames asi, llamame Bibi.\n\nTodo se destruyo,debemos volver a construir todo ese imperio,con los mismos codigos de encriptacion!\nSolo responde \n\nDandole al boton de abajo,si aceptas seras parte de nuestro nuevo ejercito '0042'!\n\nEs lo mas pronto posible!")
    
    boton2= Button(frame2, text= "Enviar Seleccion")
    boton2.config(relief="flat", 
                      bd= 5, 
                      command= Seleccion_datos, 
                      fg="red", 
                      bg= "black",
                      activeforeground= "black",
                      activebackground= "green")
    boton2.place(x= 40, y= 375)
#---------------------------------------------------------------------------
###Crea la nueva ventana de interaccion con usuario. 
def Inicio():
    global frame2, texto_mostrar, madre2
    
    madre.destroy()
    
    #Ventana raiz 2.
    madre2 = Tk()
    madre2.title("Bienvenida")
    madre2.geometry("500x500")
    madre2.resizable(0,0)
    madre2.config(bg = "gray",
                  bd= 30,
                  relief= "ridge")
    
    #Deco1
    frame2 = Frame(madre2)
    frame2.config(bg="white", 
                  width= 420, 
                  height= 420)
    frame2.grid(row= 3, 
                column=1, 
                padx=10, 
                pady=10)
    
    #Deco2
    frame3 = Frame(frame2)
    
    #frame3.geometry("200x400")
    frame3.config(bg="gray",
                  width= 400,
                  height= 200,
                  bd= 5,
                  relief="ridge")
    frame3.place(x= 10, 
                y= 20)
    #frame3.resizable(0,0)
    
    texto_mostrar = Text(frame3, 
                         width= 45, 
                         height= 10,
                         font="console 9 bold",
                         bg= "black",
                         foreground= "white",
                         state= NORMAL)
    texto_mostrar.config(bd= 5,
                         relief="ridge")
    texto_mostrar.grid(padx= 5, 
                       pady= 5)
    texto_mostrar.insert(INSERT, "Bienvenida Nathalia!\n[------------------------------------------------------]\nEsta es el mensaje de recuperacion de la mision:\n(200000FFx10)\n[------------------------------------------------------]\n\nEste mensaje es decodificado una vez el otro mensa-je se comprueba que su estado es \nnulo_______ERROR....\n")
    
    #Boton Continuacion
    boton_cont= Button(frame2, text= "Go!")
    
    boton_cont.config(relief="flat", 
                      bd= 5, 
                      command= Continuacion, 
                      fg="red", 
                      bg= "black",
                      activeforeground= "black",
                      activebackground= "green")
    boton_cont.place(x= 190, y=250)
    
    
    showinfo(title= "24", 
             message="Gracias por continuar :) Se abrira la nueva ventana.")      
    madre2.mainloop()
    
 
#Inicio programa principal.
##Ventana Raiz.
madre = Tk()
madre.title("Mensaje De Recuperacion")
madre.geometry("700x500")
madre.resizable(0,0)
#Coniguracion Ventana.
madre.config(bg= "black", bd= 20, relief= "sunken")

wid1 = Frame(madre)
wid1.place(x= 250, y= 200 )
wid1.config(width= 100, height= 100, bg= "white", bd= 5, relief= "flat")

boton_finalxd= Button(madre,
                  text= "Pista", 
                  command= bonus,
                  activeforeground= "red",
                  bd= 5,
                  relief="flat",
                  overrelief="raised").place(x= 400, y= 400)

botonini = Button(wid1,
                  text= "¿Quieres Iniciar?", 
                  command= Inicio,
                  activeforeground= "red",
                  bd= 5,
                  relief="ridge",
                  overrelief="raised",
                  cursor="heart").grid(row= 0, column= 0)

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
                 overrelief="raised",
                 cursor= "pirate").place(x= 550, y= 400)
                                         
madre.mainloop()

