grupo = int(input("cuántos estudiantes va a registrar?: "))

femenino = 0
masculino = 0


for i in range(grupo):
    print("---------------------------------")
    print("estudiante", i + 1)

    while True:
        print("ingrese (F), si es femenino\ningrese (M), si es masculino")
        genero = input("ingrese su genero: ")

        if genero != "F" and genero != "M":
            print("debe ingresar un género válido (F o M)\nEN MAYÚSCULAS")
        else:
            break
    if genero == "F":
        femenino += 1
    else:
        masculino += 1
    
print("---------------------------------")
promedio =(femenino / grupo) * 100
print("el porcentaje de estudiantes femeninos es:", promedio, "%")
promedio =(masculino / grupo) * 100  
print("el porcentaje de estudiantes masculinos es:", promedio, "%")

