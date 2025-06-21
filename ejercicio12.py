artículos = int(input("Ingrese el número de artículos: "))
compra = int(input("Ia cuánto compra cada artículo:  "))

ganancia_total = 0

for i in range(artículos):
    ganancia = compra * 0.30
    precio = compra + ganancia

    ganancia_total += ganancia

print("El precio en el que debe vender cada artículo es: ", precio)
print("La ganancia total por los ",artículos,"artículos es: $", ganancia_total)