import numpy as np

# Posiciones a las que se moverán los 10 peces (arreglo 2D)
locs = np.array([
    [0, 0, 0],
    [1, 1, 2],
    [0, 0, 0],
    [2, 1, 3],
    [5, 5, 4],
    [5, 0, 0],
    [5, 0, 0],
    [0, 0, 0],
    [2, 1, 3],
    [1, 3, 1]
])

# Generador de pesos/tamaños de los peces
generator = np.random.default_rng(1010)
weights = generator.normal(size=10)
print("Pesos de los peces:")
print(weights)

# Diccionario para almacenar qué pez sobrevive en cada celda
# clave: posición (i,j,k), valor: (índice del pez, peso)
ocupadas = {}

# Evaluamos cada pez
for idx, pos in enumerate(map(tuple, locs)):
    peso = weights[idx]
    
    if pos not in ocupadas:
        # Nadie está aquí todavía
        ocupadas[pos] = (idx, peso)
    else:
        # Hay competencia: gana el más pesado
        idx_actual, peso_actual = ocupadas[pos]
        if peso > peso_actual:
            ocupadas[pos] = (idx, peso)  # reemplaza al pez anterior

# Índices de los peces que sobreviven
sobreviven = sorted([idx for idx, _ in ocupadas.values()])

print("\n🐠 Peces que sobreviven (índices):", sobreviven)
print("Tamaños de los peces que sobreviven:")
for idx in sobreviven:
    print(f"Pez {idx}: peso = {weights[idx]:.3f}")
