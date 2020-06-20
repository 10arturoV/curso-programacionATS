
producto = int(input("cuantos articulos va a llevar "))

contador = 0
cuentaTo = 0

while contador < producto:
        contador = contador + 1
        costo = int(input("ingrese el costo del producto "))
        captura = costo * .16
        total = captura + costo
        print("costo del articulo con iva " + str(total))
        cuentaTo = cuentaTo + total
        print("el total es "+ str(cuentaTo))
        break
        pago = float(input("ingrese el pago del cliente "))
        cambio = pago - cuentaTo
        print("su cambio es de "+ str(cambio))
        while True:
            print(("¿Capturar nueva compra? (S/N):"))
            tecla_repetir = input()
            if tecla_repetir == "s" or tecla_repetir == "n" or tecla_repetir == "S" or tecla_repetir == "N": break
        if tecla_repetir == "n" or tecla_repetir == "N": break
print("La cantidad total de dinero en la caja es: ", cuentaTo)






