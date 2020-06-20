

cantidad_total = 0
contador = 0
cuentaTo = 0
if __name__ == '__main__':
     while True:
            producto = int(input("cuantos articulos va a llevar "))
            while contador < producto:
                contador = contador + 1
                costo = int(input("ingrese el costo del producto "))
                captura = costo * .16
                total = captura + costo
                print("costo del articulo con iva " + str(total))
                cuentaTo = cuentaTo + total
                print("el total es " + str(cuentaTo))

            print(("Ingresa el pago del cliente: "))
            pago_cliente = float(input())
            cambio = (pago_cliente - cuentaTo)
            print(("El cambio es: "), cambio)
            cantidad_total = (cantidad_total + cuentaTo)

     while True:  # no hay 'repetir' en python
         print(("¿Capturar nueva compra? (S/N):"))
         tecla_repetir = input()
     if tecla_repetir == "s" or tecla_repetir == "n" or tecla_repetir == "S" or tecla_repetir == "N": break
     if tecla_repetir == "n" or tecla_repetir == "N": break


print("La cantidad total de dinero en la caja es: ", cantidad_total)