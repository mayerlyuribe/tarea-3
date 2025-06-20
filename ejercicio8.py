volumen = float((input("introduce el volumen (ft²): ")))
presion = float(input("introduce la presión (psi): "))
temperatura = float(input("introduce la temperatura (°F):  "))

masa = (presion * volumen) / (0.37 * (temperatura + 460))

print("la masa es:", masa, "lb")