sumagrupo = 0
mayorcalf = -1
menorcalf = 6

estudiantes = int(input("cuántos estudiantes va a registrar?:"))
if estudiantes <= 0:
    print("debes ingresar al menos un estudiante :(  ") 

for a in range(estudiantes):
    print("estudiante", a + 1)
    while True:

        nota1 = float(input("ingrese la nota de su primer parcial: "))
        if  nota1 >= 0.0 and nota1 <= 5.0:
            break
        else:
            print("debe ingresar una nota válida, en el rango de (0.0 a 5.0)")

    while True:
        nota2 = float(input("ingrese la nota de su segundo parcial:"))
        if  nota2 >= 0.0 and nota2 <= 5.0:
            break
        else:
            print("debe ingresar una nota válida, en el rango de (0.0 a 5.0)")

    while True:
        nota3 = float(input("ingrese la nota de su tercer parcial: "))
        if  nota3 >= 0.0 and nota3 <= 5.0:
            break
        else:
            print("debe ingresar una nota válida, en el rango de (0.0 a 5.0)")

    while True:
        exmFinal = float(input("ingrese la nota de su examen final: "))
        if  exmFinal >= 0.0 and exmFinal <= 5.0:
            break
        else:
            print("debe ingresar una nota válida, en el rango de (0.0 a 5.0)")

    while True:
        trabFinal = float(input("ingrese la nota de su trabajo final: "))
        if  trabFinal >= 0.0 and trabFinal <= 5.0:
            break
        else:
            print("debe ingresar una nota válida, en el rango de (0.0 a 5.0)")
    
    promedio =  (nota1 + nota2 + nota3)/3
    calificacion = (promedio * 0.55) + (exmFinal * 0.30) + (trabFinal * 0.15)
    print("su calficación es:", calificacion)
    print("---------------------------------")

    if calificacion > mayorcalf:
        mayorcalf = calificacion
    if calificacion < menorcalf:
        menorcalf = calificacion
    sumagrupo += calificacion

promediogrupo = sumagrupo /estudiantes
print("---------------------------------")
print("calificación más alta:", mayorcalf)
print("calificación más baja:", menorcalf)
print("el promedio del grupo es:", promediogrupo)
