personas = int(input("cuántas personas va a registrar?: "))

while personas > 0:
    print("ingrese la fecha de hoy:")
    año_hoy = int(input("año: "))
    mes_hoy = int(input("mes: "))
    while True:
        if mes_hoy < 1 or mes_hoy > 12:
            print("El mes debe estar entre 1 y 12.")
            mes_hoy = int(input("mes: "))
        else:
            break
    dia_hoy = int(input("día: "))
    while True:
        if dia_hoy < 1 or dia_hoy > 31:
            print("El día debe estar entre 1 y 31.")
            dia_hoy = int(input("día: "))
        else:
            break

    print("--------------------------------------")
    print("a continuación ingresa tu fecha de nacimiento: ")

    año = int(input("año: "))
    while True:
        if año > año_hoy:
            print("El año no puede ser mayor a", año_hoy)
            año = int(input("año: "))
        else: 
            break
    mes = int(input("mes: "))  
    while True:
        if mes < 1 or mes > 12:
            print("El mes debe estar entre 1 y 12.")
            mes = int(input("mes: "))
        else:
            break
    dia = int(input("día: "))
    while True:
        if dia < 1 or dia > 31:
            print("El día debe estar entre 1 y 31.")
            dia = int(input("día: "))
        else:
            break
    print("--------------------------------------")
    if mes < mes_hoy:
        if dia < dia_hoy:
            cumplido = True
        elif dia == dia_hoy:
            cumplido = True
        else:
            cumplido = False
    else:
        cumplido = False
    
    if cumplido == True:
        edad = año_hoy - año
    elif cumplido == False:
        edad = (año_hoy - año) - 1

    print("tu edad es:", edad)
    print("--------------------------------------")

    personas -= 1