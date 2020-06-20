print("ingresa 1er digito")
num1 = int(input())
print("ingresa 2do digito")
num2 = int(input())
print("ingresa 3er digito")
num3 = int(input())

if num1 > num2:
    if num1 > num3:
        if num2 > num3:
            Mediana = num2
        else:
            Mediana = num3
    else:
        Mediana = num1
else:
    if num1 > num3:
        Mediana = num1
    else:
        if num2 > num3:
            Mediana = num3
        else:
            Mediana = num2

print(f"La mediana es {Mediana} ")
