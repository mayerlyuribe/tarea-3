vendedores = int(input("cuántos vendedores va a registrar?: "))
sueldo = int(input("cuál es el sueldo base de los vendedores?: "))

while vendedores > 0:
    nombre = input("nombre del vendedor: ")
    ventas = 3

    comisión_total = 0
    print("calculemos el valor de las ventas de", nombre)
    print("---------------------------------------------")
    for i in range(ventas):
        print("venta número", i + 1)
        valor_venta = int(input("valor de la venta: "))
        comisión = valor_venta*0.10
        comisión_total += comisión
    
    sueldo_total = sueldo + comisión_total
    print("---------------------------------------------")
    print("la comisión total de ", nombre, "es de:", comisión_total)
    print("el sueldo total de", nombre, "es de:", sueldo_total)

    print("---------------------------------------------")
    vendedores -=1