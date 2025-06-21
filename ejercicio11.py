monto = int(input("Ingrese el monto preupuestal destinado al hospital: "))

ginecología = monto * 0.40
traumatología = monto * 0.30
pediatría = monto * 0.30

print("----------------------------------------")
print("Distribución del presupuesto:")
print("ginecología: $", ginecología)
print("pediatría: $", pediatría)
print("traumatología: $", traumatología)