camisas = int(input("ingrese la cantidad de camisas que va a comprar: "))
costo = int(input("ingrese el costo de cada camisa: "))

if camisas <= 3:
    total = (camisas * costo) * 0.90
elif camisas > 3:
    total = (camisas * costo) * 0.80

print("El total a pagar es: $", total)