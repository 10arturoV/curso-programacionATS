a = int(input("ingresa 1er numero "))
b = int(input("ingresa 2do numero "))
c = int(input("ingresa 3er numero "))

if a >= b and a >= c:
    print("el numero "+str(a)+" es mayor")
elif b >= a and b >= c:
    print("el numero "+str(b)+" es mayor")
elif c >= a and c >= b:
    print("el numero " + str(c) + " es mayor")

