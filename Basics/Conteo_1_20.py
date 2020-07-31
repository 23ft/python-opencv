#Pruebas 1
b = 0
a = int(input("Seleccione: "))
print(" ")

while a == 1:
    
    b+=1
    c = hex(b)
    print(c)
    
    if b == 20:
        print("\nrompiendo...\n")
        break
print("---------------------------------------------------------------")
print(f"Hola el numero que ingreso es {a} y el resultado {b}\n")
print("Finalizado Conteo")
print("---------------------------------------------------------------")

