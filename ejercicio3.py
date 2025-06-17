clientes = int(input("cuantos clientes van a comprar?: "))

while clientes > 0:
    name = input("nombre del cliente: ")
    compra = int(input("cuánto es el total de su compra?: "))

    total = compra - (compra * 0.15)
    print("señor o señora: ", name)
    print("el total a pagar, aplicando el descuento del (15%), es: ", total)

    clientes -= 1

