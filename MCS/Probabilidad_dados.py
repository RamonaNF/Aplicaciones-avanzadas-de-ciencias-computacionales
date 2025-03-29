import random.randint as randint
import matplotlib.pyplot as plt

print("ACTIVIDAD: Simulando el lanzamiento de un dado\nRamona Najera, A01423596")
cara = [i for i in range(1, 7)]

print("\nPARTE 1: Probabilidad equitativa")
"""
Realiza un programa que simule el lanzamiento de un dado, 1000 veces.
Muestra el histograma de las frecuencias de las veces que salió cada cara (es decir, la cara del dado vs. las veces que salió).
Además muestra el promedio de las caras que salieron.
"""
# 1. Simular lanzamiento de dado 1000 veces
dado = [randint(1, 6) for i in range(0, 1000)]
#print(dado)

# 2. Determinar frecuencia individual y promedio de caras
datos = {}
freq = []

for val in dado:
  if val in datos:
    datos[val] += 1
  else:
    datos[val] = 1

for val in sorted(datos):
  #print(f'{val}: freq({datos[val]})')
  freq.append(datos[val])

print(f'Promedio de caras: {sum(dado)/1000}')

# 3. Graficar frecuencia
plt.bar(cara, freq)
plt.title('Tirando un dado 1000 veces')
plt.xlabel('Cara del dado')
plt.ylabel('Frecuencia')
plt.show()

print("\nPARTE 2: Probabilidad desigual")
"""
Realiza un programa que simule el lanzamiento de un dado, 1000 veces de tal forma que haya una probabilidad del 50% de que salga el 6, y el resto de los números el otro 50% de manera equitativa.
Muestra en una tabla las veces que salió cada número y aparte muéstralo como porcentaje.
"""

# 1. Aumentar la probabilidad de que salga 6
peso = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]

# 2. Generar números aleatorios con las nuevas probabilidades
dado2 = [random.choices(cara, peso, k=1)[0] for i in range(0, 1000)]
#print(dado2)

# 3. Determinar frecuencia y porcentaje de aparición de cada cara
datos2 = {}
freq2 = []

for val in dado2:
  if val in datos2:
    datos2[val] += 1
  else:
    datos2[val] = 1

for val in sorted(datos2):
  print(f'{val}: freq({datos2[val]}) percentage({datos2[val]/10}%)')
  freq2.append(datos2[val])

plt.bar(cara, freq2)
plt.title('Con 6 con mayor probabilidad')
plt.xlabel('Cara del dado')
plt.ylabel('Frecuencia')
plt.show()