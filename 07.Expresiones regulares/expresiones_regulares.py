# Expresiones Regulares en Python

"""
Las expresiones regulares son secuencias de caracteres que forman un patrón de búsqueda. Son útiles para encontrar, manipular, o validar texto.
Python utiliza el módulo 're' para trabajar con expresiones regulares.

Documentación oficial: https://docs.python.org/3/library/re.html
"""

import re

################### 1. INTRODUCCIÓN #####################

"""
Las expresiones regulares permiten buscar patrones dentro de cadenas de texto. Estos patrones pueden incluir caracteres especiales que tienen significados específicos. 
Algunos de los caracteres y sus significados son los siguientes:

- '.' : Cualquier carácter, excepto nueva línea.
- '^' : Inicio de la cadena.
- '$' : Fin de la cadena.
- '*' : Cero o más repeticiones.
- '+' : Una o más repeticiones.
- '?' : Cero o una repetición.
- '{n}' : Exactamente n repeticiones.
- '{n,m}' : Entre n y m repeticiones.
- '[abc]' : Cualquier carácter a, b o c.
- '[^abc]' : Cualquier carácter que no sea a, b o c.
- '\d' : Cualquier dígito.
- '\D' : Cualquier carácter que no sea un dígito.
- '\w' : Cualquier carácter alfanumérico.
- '\W' : Cualquier carácter no alfanumérico.
- '\s' : Cualquier espacio en blanco.
- '\S' : Cualquier carácter que no sea un espacio en blanco.
"""

################### 2. FUNCIONES BÁSICAS #####################

"""
Python provee varias funciones en el módulo 're' para trabajar con expresiones regulares:

- re.match() : Busca un patrón al inicio de la cadena.
- re.search() : Busca el patrón en toda la cadena (no solo al inicio).
- re.findall() : Devuelve todas las coincidencias en una lista.
- re.sub() : Reemplaza el patrón por otro.
"""

# Ejemplo 1: Uso básico de re.match y re.search

texto = "Hola, bienvenido a la guía de expresiones regulares en Python"

# Verifica si la cadena empieza con "Hola"
if re.match(r"Hola", texto):
    print("La cadena empieza con 'Hola'.")

# Busca "Python" en cualquier parte del texto
if re.search(r"Python", texto):
    print("Se encontró la palabra 'Python' en el texto.")

################### 3. GRUPOS Y CAPTURAS #####################

"""
Las expresiones regulares permiten capturar partes específicas del texto usando paréntesis ().
Esto es útil cuando queremos extraer datos específicos de una cadena.
"""

# Ejemplo 2: Captura de grupos

texto = "El precio es 45.50 USD"

# Queremos capturar el precio en una variable
patron = r"(\d+\.\d+) USD"  # Busca un número con decimales seguido de 'USD'
resultado = re.search(patron, texto)

if resultado:
    precio = resultado.group(1)  # group(1) devuelve el primer grupo capturado
    print(f"El precio encontrado es: {precio}")

################### 4. CARACTERES ESPECIALES #####################

"""
Algunos caracteres tienen significados especiales en las expresiones regulares, como el punto (.), asterisco (*), más (+), etc. Si queremos buscar estos caracteres literalmente, 
debemos escaparlos usando la barra invertida (\).
"""

# Ejemplo 3: Buscar una dirección web

texto = "Visita https://www.python.org para más información"
patron = r"https://www\.[a-z]+\.[a-z]+"  # Busca una URL sencilla
resultado = re.search(patron, texto)

if resultado:
    print(f"Se encontró la URL: {resultado.group()}")

################### 5. USO DE re.findall() #####################

"""
La función re.findall() devuelve todas las coincidencias de un patrón en una lista.
"""

# Ejemplo 4: Encontrar todas las palabras que empiezan con una vocal

texto = "El agua es esencial para la vida en la Tierra"
patron = r"\b[aeiouAEIOU]\w+"  # Palabras que empiezan con vocal

vocales = re.findall(patron, texto)
print("Palabras que empiezan con vocal:", vocales)

################### 6. REEMPLAZO CON re.sub() #####################

"""
La función re.sub() se utiliza para reemplazar partes de una cadena que coincidan con un patrón.
"""

# Ejemplo 5: Reemplazar números por la palabra "[número]"

texto = "En el año 2024 habrán varios eventos importantes."
patron = r"\d+"
nuevo_texto = re.sub(patron, "[número]", texto)
print("Texto modificado:", nuevo_texto)

################### 7. EJERCICIOS PRÁCTICOS #####################

# 1. Extraer todas las direcciones de correo electrónico de un texto.
texto = "Contacta con nosotros: info@empresa.com, soporte@ayuda.org"
patron_email = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
correos = re.findall(patron_email, texto)
print("Correos encontrados:", correos)

# 2. Validar si una cadena es un número de teléfono en formato (XXX) XXX-XXXX.
telefono = "(123) 456-7890"
patron_telefono = r"\(\d{3}\) \d{3}-\d{4}"
if re.match(patron_telefono, telefono):
    print("Número de teléfono válido.")

# 3. Reemplazar todas las secuencias de múltiples espacios por un único espacio.
texto_con_espacios = "Este  texto    tiene   demasiados   espacios."
texto_limpio = re.sub(r"\s+", " ", texto_con_espacios)
print("Texto con espacios corregidos:", texto_limpio)

################### 8. RESUMEN #####################

"""
Las expresiones regulares son una herramienta poderosa para trabajar con texto. Son muy flexibles y se pueden utilizar en muchas tareas como:
- Validación de datos (números de teléfono, correos electrónicos).
- Extracción de información.
- Búsquedas y reemplazos.

Sin embargo, las expresiones regulares pueden ser complejas y es fácil cometer errores si no se usan correctamente. Es importante probar bien las expresiones para asegurarse de que funcionan como se espera.
"""

