from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
from PIL import Image, ImageTk
import cv2
import numpy as np

##---------------------------------------------------------------------------##

#global foto, alto, ancho, size, Ubicacion

##---------------------------------------------------------------------------##
def UbiImage(): # Funcion mostrar la imagen con opencv
    
    cv2.imshow("Imagen", foto)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
##---------------------------------------------------------------------------##
def OpenFilesMenu(): # Funcion menu desplegable

    from tkinter import filedialog
    global Ubicacion, size, foto

    raiz_menux = filedialog.askopenfilename(initialdir = "/home",title = "Select file To Prepare",filetypes = (("all files","*.*"),("jpeg files","*.jpg")))
    print (raiz_menux)
    Ubicacion = raiz_menux

    foto = cv2.imread(Ubicacion)

    url.insert(0, Ubicacion)
    showinfo(title='OPencv Info', message=f"Se selecciono la imagen ubicada en: {Ubicacion}")
    if raiz_menux == ():
        showerror(title="OPencv Error", message="No se selecciono ubicacion, volver a intentar!")

    size = foto.shape
    alto = size[0]
    ancho = size[1]
    
    print(f"El tamaño de la imagen es:{size}!")
    Label(frame1,text= f"El tamaño es: {alto}x{ancho}!").grid(row = 2, column = 1, sticky= "w")
    
#---------------------------------------------------------------------------#
def Mostrar(): # Funcion mostrar imagen en GUI
    global im, lectura
    
    #Funcion para mostrar imagen en la ventana (lienzo)
    #global imagen_file    
    #size2 = size
    #alto2 = size2[0]
    #ancho2 = size2[1]
    #canvas_imagen = Canvas(raiz, width= ancho2, height= alto2)
    #Lienzo para visualizar imagen
    #canvas_imagen.place(x=360, y=180)
    #imagen_file = PhotoImage(file = Ubicacion)
    #canvas_imagen.create_image(0, 0, image= imagen_file, anchor= "nw")
    #print("Imagen Mostrando...")
    
    lectura = Image.open(Ubicacion)
    img = lectura.resize((200,200))
    im = ImageTk.PhotoImage(img)
    label_image = Label(frame1, image= im)
    label_image.grid(row= 3, column= 1)
    
#---------------------------------------------------------------------------#
#Inicio

raiz = Tk()
raiz.config(bg= "black")
raiz.title("Opencv")
raiz.geometry("1000x800")
raiz.resizable(1,1)


frame1 = Frame(raiz)
frame1.config(width=500, 
              height=500,
              bd = 40)
frame1.pack() # frame 1 integrado en la raiz "raiz"


Label(frame1, 
      text= "Open-cv",
      justify="center", 
      font=("Bookman", 30)).grid(row= 0, 
                                 column= 1, 
                                 padx=30, 
                                 pady=10) # Title "Open-cv"

                                 
url = Entry(frame1, 
            width = 60)
url.grid(row = 1, 
         column = 1) # Visualizador de la via de la imagen


SeleccionUbi = Button(frame1, 
                      text= "Seleccionar Ubicacion", 
                      font= (30), 
                      command = OpenFilesMenu)
SeleccionUbi.grid(row = 1, 
                  column = 0, 
                  sticky= "nw") # Boton de menu para seleccion de archivo


button = Button(frame1, 
                text= "Visualizar Imagen", 
                command= UbiImage)
button.grid(row = 2, 
            column = 0, 
            sticky= "nw") # Boton para vizualizar imagen con OPENCV


button2 = Button(frame1, 
                 text= "Ver Imagen", 
                 command = Mostrar) 
button2.grid(row = 3, column = 0, sticky= "nw") # Boton para mostrar imagen enla ventana


raiz.mainloop() # Bucle Infinito
