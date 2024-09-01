# Las listas de comprensión y los diccionarios de comprensión son características poderosas en Python que te permiten 
# crear listas y diccionarios de manera más concisa y legible.
# Con las listas de comprensión, puedes aplicar una expresión a cada elemento de una secuencia y generar una nueva lista basada en los resultados.
# Los diccionarios de comprensión funcionan de manera similar, pero permiten crear diccionarios directamente.

# Ventajas:

# 1. Código más conciso y legible
# 2. Mejor rendimiento (Python lo optimiza super bien)
# 3. Menos propenso a errores


############################# LISTAS DE COMPRENSIÓN #####################################

# Crear una lista de números al cuadrado usando un bucle for
numeros = [1, 2, 3, 4, 5]
cuadrados = []
for n in numeros:
    cuadrados.append(n**2)
print(f"Lista de cuadrados usando bucle for: {cuadrados}")

# Crear una lista de números al cuadrado usando una lista de comprensión
cuadrados_comp = [n**2 for n in numeros]
print(f"Lista de cuadrados usando lista de comprensión: {cuadrados_comp}")

# Filtrar números pares y elevarlos al cuadrado
pares_cuadrados = [n**2 for n in numeros if n % 2 == 0]
print(f"Números pares elevados al cuadrado usando lista de comprensión: {pares_cuadrados}")

############################# DICCIONARIOS DE COMPRENSIÓN #####################################

# Crear un diccionario con números y sus cuadrados usando un bucle for
cuadrados_dict = {}
for n in numeros:
    cuadrados_dict[n] = n**2
print(f"Diccionario de cuadrados usando bucle for: {cuadrados_dict}")

# Crear un diccionario con números y sus cuadrados usando un diccionario de comprensión
cuadrados_dict_comp = {n: n**2 for n in numeros}
print(f"Diccionario de cuadrados usando diccionario de comprensión: {cuadrados_dict_comp}")

# Filtrar números pares y crear un diccionario con su valor original y su cuadrado
pares_cuadrados_dict = {n: n**2 for n in numeros if n % 2 == 0}
print(f"Diccionario de números pares y sus cuadrados usando diccionario de comprensión: {pares_cuadrados_dict}")

############################# LISTAS DE COMPRENSIÓN CON ANIDADAS #####################################

# Crear una lista de pares (x, y) donde x e y sean elementos de dos listas diferentes
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
pares = [(x, y) for x in lista_1 for y in lista_2]
print(f"Pares combinados de dos listas: {pares}")

# Filtrar y crear una lista de pares solo si la suma de x e y es mayor que 5
pares_filtrados = [(x, y) for x in lista_1 for y in lista_2 if x + y > 5]
print(f"Pares con suma mayor que 5: {pares_filtrados}")

############################# DICCIONARIOS DE COMPRENSIÓN CON ANIDADAS #####################################

# Crear un diccionario con claves de lista_1 y valores como listas de elementos de lista_2
dict_anidado = {x: [y for y in lista_2] for x in lista_1}
print(f"Diccionario con listas anidadas como valores: {dict_anidado}")

# Crear un diccionario con claves de lista_1 y valores como listas filtradas de elementos de lista_2
dict_anidado_filtrado = {x: [y for y in lista_2 if y > 4] for x in lista_1}
print(f"Diccionario con listas filtradas anidadas como valores: {dict_anidado_filtrado}")

############################# CONVERSIÓN DE LISTA A DICCIONARIO Y VICEVERSA #####################################

# Convertir una lista de tuplas en un diccionario
lista_de_tuplas = [('a', 1), ('b', 2), ('c', 3)]
dict_from_list = {k: v for k, v in lista_de_tuplas}
print(f"Convertir lista de tuplas a diccionario: {dict_from_list}")

# Convertir un diccionario en una lista de claves
lista_de_claves = [k for k in dict_from_list]
print(f"Lista de claves desde un diccionario: {lista_de_claves}")

# Convertir un diccionario en una lista de valores
lista_de_valores = [v for v in dict_from_list.values()]
print(f"Lista de valores desde un diccionario: {lista_de_valores}")

# Convertir un diccionario en una lista de tuplas
lista_de_tuplas_de_dict = [(k, v) for k, v in dict_from_list.items()]
print(f"Convertir diccionario a lista de tuplas: {lista_de_tuplas_de_dict}")

############################# MEDICIÓN DE RENDIMIENTO #####################################

import time

# Usando lista de comprensión
start = time.time()
[n**2 for n in range(10000000)]
print("Tiempo con lista de comprensión:", time.time() - start)

# Usando bucle for
start = time.time()
cuadrados = []
for n in range(10000000):
    cuadrados.append(n**2)
print("Tiempo con bucle for:", time.time() - start)
