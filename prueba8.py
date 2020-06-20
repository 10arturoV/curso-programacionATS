a = int(input("ingresa un numero "))
b = int(input("ingresa otro numero "))

if a%2 == 0 and b%2 == 0:
    print("los 2 numeros son pares")
elif a%2 == 0 and b%2!=0:
    print("el numero  "+str(a) + " es par y el numero "+str(b)+" no es par")
elif a%2!= 0 and b%2 == 0:
    print("el numero  "+str(b) + " es par y el numero "+str(a)+" no es par")
else:
    print("los numeros no son pares")

