

class Anatt:
    Nombre = " "
    Lugar = " "
    def Hola(hora, x, y):
        print(f"Hola Soy La Clase Pass, es la hora {hora}")
        print(" ")
        print(f"La suma es igual a {x + y}")
    
    def Adios(Mess):
        print(" ")
        print(f"Adios {Mess}")
        
        
print(" ")
Anatt.Hola("5:50",2,3)
Anatt.Adios("buen hombre")
Anatt.Lugar = "Madrid, Spain"
Anatt.Nombre = "Juan Jose"
print(" ")
print(Anatt.Lugar)
print(" ")
print(Anatt.Nombre)

