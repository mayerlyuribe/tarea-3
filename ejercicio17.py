obreros = int(input("ingrese la cantidad de obreros que va a registrar: "))

nomina = 0

for i in range(obreros):
    print("obrero", i + 1)
    name = input("ingrese el nombre del obrero: ")
    horas = int(input("ingrese la cantidad de horas trabajadas en la semana: "))

    if horas <= 40 :
        pago = horas * 16000
    else:
        pago = (40 * 16000) + ((horas - 40) * 20000)
    
    mensual = pago * 4
    nomina += mensual
    print("-----------------------------------------------------")
    print("el obrero", name, "\ntiene un pago semanal de: $", pago,"\ny un pago mensual de: $", mensual)
    print("-----------------------------------------------------")

print("el total de la nomina es: $", nomina)