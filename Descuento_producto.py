print("Valor Descuento\n")

descuento = int(input("Introduzca el porcentaje de descuento (%): "))
valor = int(input("Valor orginal del producto ($): "))

print("\nProcesando Datos...\n")

valor_a_descontar = ((descuento * valor)/100)
print(f"\nSu valor a descontar es: ${valor_a_descontar}\n")

valorfinal= valor - valor_a_descontar

print(f"\nEl valor a pagar es: ${valorfinal}")



