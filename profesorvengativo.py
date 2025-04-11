import numpy as np

# Arreglo de puntajes de los estudiantes
puntajes = np.array([75, 45, 82, 55, 90, 40, 60, 30, 80, 50])

# Contador de reemplazos
reemplazos = 0

# Reemplazar los primeros 3 puntajes menores a 60 por cero
for i in range(len(puntajes)):
    if puntajes[i] < 60 and reemplazos < 3:
        puntajes[i] = 0
        reemplazos += 1

# Mostrar el resultado
print("Puntajes después de aplicar la lección vengativa:")
print(puntajes)
