operacion = input("que operacion desea realizar? ")

if operacion == "S" or operacion == "s":
    a = float(input("ingrese primer digito "))
    b = float(input("ingrese primer digito "))
    c = a + b
    print("la suma es "+str(c))
elif operacion == "R" or operacion == "r":
    a = float(input("ingrese primer digito "))
    b = float(input("ingrese primer digito "))
    c = a - b
    print("la resta es "+str(c))
elif operacion == "M" or operacion == "m":
    a = float(input("ingrese primer digito "))
    b = float(input("ingrese primer digito "))
    c = a * b
    print("la multiplicacion es "+str(c))
elif operacion == "D" or operacion == "d":
    a = float(input("ingrese primer digito "))
    b = float(input("ingrese primer digito "))
    c = a / b
    print("la division es "+str(c))
else:
    print("letra no valida")
