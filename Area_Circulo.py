import math

print("          Area Y Longitud Circulo          ")
print("---------------------------------------------------")


radio = float(input("Ingrese el radio del circulo: "))


print(" ")
print("Procesando Datos...")

Area = (math.pi * (radio**2)) 

Longitud = 2*math.pi*radio

print(" ")
print(f"El area del circulo es: {Area:.3f}\nLa Longitud Del Circulo es: {Longitud:.1f}")
