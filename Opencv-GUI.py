from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
import cv2
import numpy as np

#Def para cada boton.

def UbiImage():
    #Funcion mostrar la imagen con opencv
    global foto
    global size
    
    foto = cv2.imread(Ubicacion)
    cv2.imshow("Imagen", foto)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
def OpenFilesMenu():
    #Funcion menu desplegable
    from tkinter import filedialog
    global Ubicacion
    
    raiz_menux = filedialog.askopenfilename(initialdir = "/home",title = "Select file To Prepare",filetypes = (("all files","*.*"),("jpeg files","*.jpg")))
    print (raiz_menux)
    Ubicacion = raiz_menux
    
    foto = cv2.imread(Ubicacion)
    
    url.insert(0, Ubicacion)
    showinfo(title='OPencv Info', message=f'Se selecciono la imagen ubicada en: {Ubicacion} !')
    if raiz_menux == ():
        showerror(title="OPencv Error", message="No se selecciono ubicacion, volver a intentar!")
    
    size = foto.shape
    alto = size[0]
    ancho = size[1]
    
    print(f"El tamaño de la imagen es:{size}!")
    Label(frame1,text= f"El tamaño es: {alto}x{ancho}!").grid(row = 2, column = 1, sticky= "w")
   
def Mostrar():
    #Funcion para mostrar imagen en la ventana (lienzo)
    global imagen_file
    
    imagen_file = PhotoImage(file = Ubicacion)
    canvas_imagen.create_image(0, 0, image= imagen_file, anchor= "nw")
    print("Imagen Mostrando...")
              
#Inicio 
raiz = Tk()
raiz.title("Opencv")
raiz.geometry("1000x1000")
raiz.resizable(0,0)

#frame 1 integrado en la raiz "raiz"
frame1 = Frame(raiz)
frame1.config(width=500, height=500,bd = 40)
frame1.pack()


Label(frame1, text= "Open-cv",justify="center", font=("Bookman", 30)).grid(row= 0, column= 1, padx=30, pady=10)  


url = Entry(frame1, width = 60)
#Visualizador de la via de la imagen
url.grid(row = 1, column = 1)
    

SeleccionUbi = Button(frame1, text= "Seleccionar Ubicacion", font= (30), command = OpenFilesMenu)
#Boton de menu para seleccion de archivo
SeleccionUbi.grid(row = 1, column = 0, sticky= "nw")


button = Button(frame1, text= "Visualizar Imagen", command= UbiImage)
#Boton para vizualizar imagen con OPENCV
button.grid(row = 2, column = 0, sticky= "nw")


button2 = Button(frame1, text= "Ver Imagen", command = Mostrar)
#Boton para mostrar imagen enla ventana
button2.grid(row = 3, column = 0, sticky= "nw")


canvas_imagen = Canvas(raiz, width= 500, height= 500, bg= "black")
#Lienzo para visualizar imagen
canvas_imagen.place(x=360, y=180 )
#canvas_imagen.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)


#Bucle Infinito
raiz.mainloop()






