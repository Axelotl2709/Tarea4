import numpy as np

# Generar 10 puntajes aleatorios entre 0 y 100
puntajes_amor = np.random.uniform(low=0.0, high=100.0, size=10)

# Crear matriz de diferencias absolutas
diferencias = np.abs(puntajes_amor[:, np.newaxis] - puntajes_amor[np.newaxis, :])

# Evitar comparar una persona consigo misma
np.fill_diagonal(diferencias, np.inf)

# Obtener los mejores matches (pares con menor diferencia)
num_matches = 5  # Puedes cambiar esto si quieres más/menos matches
pares_indices = np.dstack(np.unravel_index(np.argsort(diferencias, axis=None), diferencias.shape))[0]

# Para evitar duplicados (ej. (i,j) y (j,i)), usamos un set
usados = set()
mejores_matches = []

for i, j in pares_indices:
    if (j, i) not in usados:
        usados.add((i, j))
        mejores_matches.append((i, j, diferencias[i, j]))
    if len(mejores_matches) >= num_matches:
        break

# Mostrar resultados
print("Puntajes del amor (0-100):")
for idx, score in enumerate(puntajes_amor):
    print(f"Persona {idx}: {score:.2f}")

print("\n❤️ Mejores Matches:")
for i, j, diff in mejores_matches:
    print(f"Persona {i} 💕 Persona {j} | Diferencia: {diff:.2f}")
