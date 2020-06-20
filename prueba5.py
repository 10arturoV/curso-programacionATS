cantidad_total = 0
if __name__ == '__main__':
	while True:
		print(("El monto de la venta es: "))
		monto_venta = float(input())
		iva = (monto_venta*.16)
		print(("El IVA es: "),iva)
		total_pagar = (monto_venta+iva)
		print(("El total a pagar es: "),total_pagar)
		print(("Ingresa el pago del cliente: "))
		pago_cliente = float(input())
		cambio = (pago_cliente-total_pagar)
		print(("El cambio es: "),cambio)
		cantidad_total = (cantidad_total+total_pagar)
		while True:# no hay 'repetir' en python
			print(("¿Capturar nueva compra? (S/N):"))
			tecla_repetir = input()
			if tecla_repetir=="s" or tecla_repetir=="n" or tecla_repetir=="S" or tecla_repetir=="N": break
		if tecla_repetir=="n" or tecla_repetir=="N": break
	print("La cantidad total de dinero en la caja es: ",cantidad_total)
