for i in range(1, 11):
    name = input("ingresa el nombre del artículo: ")
    while True:
        clave = input("ingresa la clave del artículo: ")
        if clave != "01" and clave!= "02":
            print("Clave inválida. Debe ser '01' o '02'.")
        else:
            break
    
    precio = int(input("ingresa el precio original del artículo: "))

    if clave == "01":
        total = precio * 0.90
    elif clave == "02":
        total = precio * 0.85
    
    print("------------------")
    print("artículo: ",name, "\nclave: ",clave, "\nprecio original: $", precio, "\ncon descuento tiene un valor de: $", total)