sueldo = int(input("ingrese su sueldo "))
print("su sueldo es "+str(sueldo))

cat = int(input("ingresa tu categoria "))

if (cat == 1):
    cat1 = (sueldo*.15)
    print("el aumento es "+str(cat1))
    aumento = cat1+sueldo
    print("el total es " + str(aumento))
elif (cat == 2):
    cat2 = (sueldo * .10)
    print("el aumento es " + str(cat2))
    aumento = cat2 + sueldo
    print("el total es " + str(aumento))
elif (cat == 3):
    cat3 = (sueldo * .08)
    print("el aumento es " + str(cat3))
    aumento = cat3 + sueldo
    print("el total es " + str(aumento))
elif (cat == 4):
    cat4 = (sueldo * .07)
    print("el aumento es " + str(cat4))
    aumento = cat4 + sueldo
    print("el total es " + str(aumento))
else:
    print("ingresa una categoria valida")