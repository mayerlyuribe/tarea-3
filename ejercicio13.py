while True:
    name1 = input("ingrese el nombre de la persona: ")
    inversión1 = int(input("ingrese la inversión que hizo: "))

    name2 = input("ingrese el nombre de la persona: ")
    inversión2 = int(input("ingrese la inversión que hizo: "))

    name3 = input("ingrese el nombre de la persona: ")
    inversión3 = int(input("ingrese la inversión que hizo: "))

    if inversión1 <= 0 or inversión2 <= 0 or inversión3 <= 0:
        print("La inversión no puede ser negativa. Intente de nuevo.")
        print("-----------------------------------------------------")
    else:
        break

total = inversión1 + inversión2 + inversión3
porcentaje1 = (inversión1 / (total)) * 100
porcentaje2 = (inversión2 / (total)) * 100
porcentaje3 = (inversión3 / (total)) * 100


print("-----------------------------------------------------")
print("El total de la inversión es: $", total)

print(name1, "tiene un porcentaje de inversión del", porcentaje1, "%")
print(name2, "tiene un porcentaje de inversión del", porcentaje2, "%")
print(name3, "tiene un porcentaje de inversión del", porcentaje3, "%")