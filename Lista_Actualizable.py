#numbers = list(range(10, 23, 3))
#print(numbers)
#print(len(numbers))
#valor = int(input("Su valor es: "))

#_lista = numbers.append(valor)
#print(numbers)

Lista1 = []

while True:
    index = int(input("Posicion Lista: "))
    print(" ")
    print(f"Posicion: {index}")
    Elemento = input("Elemento a añadir a la lista [Lista 1]: ")
    print(f"El Elemento es: {Elemento}")
    Lista1.insert(index, Elemento)
    print(Lista1)
    
    if Elemento == "Q":
        print("Rompiendo..")
        break
    

print(Lista1)
for_ = input("Quiere usted repetir los numeros?: ")
if for_ == "Si":
    for lista in Lista1:
        print(lista)
        
  