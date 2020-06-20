saldoInicial = 1000

print("bienvenido a cajeros atm")
opcion = int(input("que operacion desea realizar? "))

if opcion == 1:
    print(f"su saldo disponible es {saldoInicial}")
elif opcion == 2:
    retiro = float(input("ingrese la cantidad que desea retirar "))
    if retiro > saldoInicial:
        print("no cuenta con saldo suficiente")
    else:
        retiro = saldoInicial - retiro
        print(f"su saldo disponible es {retiro}")
elif opcion == 3:
    deposito = float(input("ingrese la cantidad a depositar "))
    deposito += saldoInicial
    print(f"su saldo disponible es {deposito}")
elif opcion == 4:
    print("vuelva pronto")
else:
    print("error . opcion no valida")

