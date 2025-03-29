import math
import matplotlib.pyplot as plt

print("ACTIVIDAD: Tablas de frecuencias e histogramas\nRamona Najera, A01423596")

data = []
decimales = int(input("\nDecimales esperados: "))

with open("./Tabla_de_frecuencias/data03.txt", 'r') as dataset:
    for line in dataset:
        data.append(float(line))

data.sort()
#print("Data array:", data)

# 1. Sacar número de datos
N = len(data)
print("\nN:", N)

# 2. Sacar número de clases
C = math.ceil(1 + 3.3 * math.log(N, 10))
print("C:", C)

# 3. Sacar ancho del intervalo
last = round(data[len(data) - 1], decimales)
first = round(data[0], decimales)

print("max:", last)
print("min:", first)

W = (last - first) / C
add = 1/10**(decimales)
W += add
print("W:", round(W, decimales))

# 4. Generar intervalos
intervalos = []
prev = first

for i in range(C):
    new = prev + W
    intervalos.append([prev, new])
    prev = new

# 5. Calcular frecuencia (imprimir tabla y suma total)
compare = 0
freq = [0] * C

for i in range(N):
    while data[i] > intervalos[compare][1]:
        compare += 1
    freq[compare] += 1

print("\nIntervalos y frecuencias")
tag = []

for i in range(C):
    tag.append(f'[{round(intervalos[i][0], decimales)}, {round(intervalos[i][1], decimales)})')
    print(f'{tag[i]} {freq[i]}')

print("\n Suma de frecuencias", sum(freq))

# 6. Graficar frecuencias
plt.bar(tag, freq)
plt.xticks(rotation=90)

plt.title('Frecuencia por intervalos')
plt.xlabel('Intervalos')
plt.ylabel('Frecuencias')

plt.tight_layout()
plt.show()