import math

numero = int(input("ingresa un numero "))
while numero < 0:
    print("ingresa un numero valido")
    numero = int(input("ingresa un numero "))
print(f"la raiz cuadrada es {math.sqrt(numero):.2f}")