obreros = int(input("cuántos obreros va a registrar?: "))
masde2_minimos = 0
for i in range (obreros):
    nombre = input("nombre del obrero: ")
    salarioant= int(input("de cuanto era su salario anterior?: "))
    salarionvo = salarioant + (salarioant * 0.25 )
    print("su nuevo salario es de:", salarionvo)
    print("-------------------------------------")

    if salarionvo > 2847000:
        masde2_minimos = masde2_minimos + 1 

print("la cantidad de obreros que ganan más de 2 salarios minimos es:", masde2_minimos)
print("-------------------------------------------------------------------")
