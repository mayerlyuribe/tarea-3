personas = int(input("¿Cuántas personas quieres ingresar? "))

monto = 0
for i in range(personas):

    print("persona", i + 1)
    compra = int(input("Ingrese el valor de la compra: "))
    if compra > 100000:
        descuento = compra * 0.20
        total = compra - descuento
        print("el total a pagar, aplicando el descuento del 20% es:", total)
        monto += descuento
    else:
        print("El total a pagar es:", compra)
    print("--------------------------------------")

print("El monto total de las compras es:", monto)