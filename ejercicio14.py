alumnos = int(input("Ingrese el número de alumnos a registrar: "))

sumaGeneralMat = 0
sumaGeneralFis = 0
sumaGeneralQuim = 0

for i in range(alumnos):
    print("---------------------------------")
    print("alumno", i + 1)
    print("---------------------------------")
    print("notas del área de Matemáticas")

    while True:
        tareaMat1 = float(input("ingrese la nota de su primera tarea: "))
        if  tareaMat1 >= 0.0 and tareaMat1 <= 5.0:
            break
        else:
            print("debe ingresar una nota válida, en el rango de (0.0 a 5.0)")

    while True:
        tareaMat2 = float(input("ingrese la nota de su segunda tarea: "))
        if  tareaMat2 >= 0.0 and tareaMat2 <= 5.0:
            break
        else:
            print("debe ingresar una nota válida, en el rango de (0.0 a 5.0)")
    
    while True:
        tareaMat3 = float(input("ingrese la nota de su tercera tarea: "))
        if  tareaMat3 >= 0.0 and tareaMat3 <= 5.0:
            break
        else:
            print("debe ingresar una nota válida, en el rango de (0.0 a 5.0)")

    while True:
        examenMat = float(input("ingrese la nota de su examen: "))
        if  examenMat >= 0.0 and examenMat <= 5.0:
            break
        else:
            print("debe ingresar una nota válida, en el rango de (0.0 a 5.0)")
    
    promedioMat = (tareaMat1 + tareaMat2 + tareaMat3) / 3
    calificacionMat = (promedioMat * 0.10) + (examenMat * 0.90)

    sumaGeneralMat += calificacionMat

    print("---------------------------------")
    print("notas del área de Física")

    while True:
        tareaFis1 = float(input("ingrese la nota de su primera tarea: "))
        if  tareaFis1 >= 0.0 and tareaFis1 <= 5.0:
            break
        else:
            print("debe ingresar una nota válida, en el rango de (0.0 a 5.0)")

    while True:
        tareaFis2 = float(input("ingrese la nota de su segunda tarea: "))
        if  tareaFis2 >= 0.0 and tareaFis2 <= 5.0:
            break
        else:
            print("debe ingresar una nota válida, en el rango de (0.0 a 5.0)")

    while True:
        examenFis = float(input("ingrese la nota de su examen: "))
        if  examenFis >= 0.0 and examenFis <= 5.0:
            break
        else:
            print("debe ingresar una nota válida, en el rango de (0.0 a 5.0)")

    promedioFis = (tareaFis1 + tareaFis2) / 2
    calificacionFis = (promedioFis * 0.20) + (examenFis * 0.80)

    sumaGeneralFis += calificacionFis

    print("---------------------------------")
    print("notas del área de Química")
    while True:
        tareaQuim1 = float(input("ingrese la nota de su primera tarea: "))
        if  tareaQuim1 >= 0.0 and tareaQuim1 <= 5.0:
            break
        else:
            print("debe ingresar una nota válida, en el rango de (0.0 a 5.0)")

    while True:
        tareaQuim2 = float(input("ingrese la nota de su segunda tarea: "))
        if  tareaQuim2 >= 0.0 and tareaQuim2 <= 5.0:
            break
        else:
            print("debe ingresar una nota válida, en el rango de (0.0 a 5.0)")
    
    while True:
        tareaQuim3 = float(input("ingrese la nota de su tercera tarea: "))
        if  tareaQuim3 >= 0.0 and tareaQuim3 <= 5.0:
            break
        else:
            print("debe ingresar una nota válida, en el rango de (0.0 a 5.0)")

    while True:
        examenQuim = float(input("ingrese la nota de su examen: "))
        if  examenQuim >= 0.0 and examenQuim <= 5.0:
            break
        else:
            print("debe ingresar una nota válida, en el rango de (0.0 a 5.0)")
    
    promedioQuim = (tareaQuim1 + tareaQuim2 + tareaQuim3) / 3
    calificacionQuim = (promedioQuim * 0.15) + (examenQuim * 0.85)

    sumaGeneralQuim += calificacionQuim

    promedioGeneral = (calificacionMat + calificacionFis + calificacionQuim) / 3
    print("---------------------------------")
    print("calificación del área de Matemáticas:", calificacionMat)
    print("calificación del área de Física:", calificacionFis)
    print("calificación del área de Química:", calificacionQuim)
    print("---------------------------------")
    print("promedio general de las 3 areas:", promedioGeneral)

promedioGeneralMat = sumaGeneralMat / alumnos
promedioGeneralFis = sumaGeneralFis / alumnos
promedioGeneralQuim = sumaGeneralQuim / alumnos

print("---------------------------------------")
print("promedio general de las 3 asignaturas: ")
print("---------------------------------------")
print("promedio general del área de Matemáticas:", promedioGeneralMat)
print("promedio general del área de Física:", promedioGeneralFis)
print("promedio general del área de Química:", promedioGeneralQuim)
