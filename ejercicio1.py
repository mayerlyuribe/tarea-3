personas = int(input("¿cuántas personas va a registrar?: "))

while personas <= 0:
    print("El número de personas debe ser mayor que 0.")
    personas = int(input("¿cuántas personas va a registrar?: "))

interes_total = 0

for i in range(personas):
    nombre = input("nombre de la persona: ")
    capital = int(input("¿cuánto capital va a invertir?: "))
    while True:
        if capital < 0:
            print("El capital debe ser un número positivo.")
            capital = int(input("¿cuánto capital va a invertir?: "))
        else:
            break
    interes = capital * 0.02
    pago_persona = capital + interes
    
    print("el pago total de", nombre, ", después de un mes es de:", pago_persona)
    print("el interés generado por", nombre, "es de:", interes)

    interes_total += interes

print("el interés total de todas las personas es de:", interes_total)