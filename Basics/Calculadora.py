print(" ")
print("-------------------------------------------------------------------")
print("Calculadora Made For Deaza ")
print("-------------------------------------------------------------------")
print(" ")
print(" ")
print("Bienvenidos A La Calculadora\n")
while True:
    print("-------------------------------------------------------------------")
    print("+ Para sumar escriba 'S'!")
    print("- Para restar escriba 'R'!")
    print("* Para Multiplicar escriba 'M'!")
    print("/ Para dividir escriba 'D'!")
    print(":( 'Q' para salir!")
    print("-------------------------------------------------------------------")
    seleccion = input("Escriba Su Selecion: ")
    
    #Suma
    if seleccion == ("S"): 
        print(" ")
        print("Bienvenido A La Suma")
        valorsuma = int(input("Numero De Datos A Sumar: "))
        listaxd = []
        suma = 0
        for i in range(valorsuma):
             valor = int(input(f"Su valor {i+1} es:" ))
             listaxd.insert(i, valor)
        for f in range(0,valorsuma):
            suma = (listaxd[f]) + suma
        print(" ")
        print("-------------------------------------------------------------------")
        print(f"Valor de la suma es: {suma}")
        print("-------------------------------------------------------------------")
        valorfinalsuma = input("Desea continuar? 'S' si SI, 'N' si NO: ")
        if valorfinalsuma == 'S':
            print(" ")
            print("-------------------------------------------------------------------")
            print("Selecciona De Nuevo!")
            print("-------------------------------------------------------------------")
            continue
        elif valorfinalsuma == 'N':
            print(" ")
            print(" ")
            print("-------------------------------------------------------------------")
            print("Apagando Calculadora...")
            print("-------------------------------------------------------------------")
            break
        
    elif seleccion == ('M'):
        print("Mañana multiplicacion")
        break
       
        
            
            
             
    elif seleccion == ('Quit') or ('q') or ('Q'):
        print("Apagando Calculadora...")
        break
    
        
            
        
        
    
    