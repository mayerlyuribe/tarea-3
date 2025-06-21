alumnos = int(input("Ingrese el número de alumnos: "))
aprobados = 0
reprobados = 0
for i in range(alumnos):
    print("---------------------------------")
    print("alumno", i + 1)
    name = input("Ingrese el nombre del alumno: ")

    while True:
        nota1 = float(input("ingrese la nota 1: "))
        if  nota1 >= 0.0 and nota1 <= 5.0:
            break
        else:
            print("debe ingresar una nota válida, en el rango de (0.0 a 5.0)")

    while True:
        nota2 = float(input("ingrese la nota 2: "))
        if  nota2 >= 0.0 and nota2 <= 5.0:
            break
        else:
            print("debe ingresar una nota válida, en el rango de (0.0 a 5.0)")
    
    while True:
        nota3 = float(input("ingrese la nota 3: "))
        if  nota3 >= 0.0 and nota3 <= 5.0:
            break
        else:
            print("debe ingresar una nota válida, en el rango de (0.0 a 5.0)")

    promedio = (nota1 + nota2 + nota3) / 3
    print("alumn@", name, "su promedio es:", promedio)

    if promedio >= 3.5:
        print("aprobado")
        aprobados += 1
    else:
        print("reprobado")
        reprobados += 1
porcentajeReprobados = (reprobados / alumnos) * 100

print("---------------------------------------------")
print("Total de alumnos aprobados:", aprobados)
print("el porcentaje de alumnos reprobados es:", porcentajeReprobados, "%")