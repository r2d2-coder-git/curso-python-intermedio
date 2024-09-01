from datetime import datetime, timedelta, date

# Obtener la fecha y hora actuales
ahora = datetime.now()
print("Fecha y hora actuales:", ahora)

# Formatear la fecha y la hora en un formato específico
fecha_formateada = ahora.strftime("%d/%m/%Y %H:%M:%S")
print("Fecha y hora formateadas:", fecha_formateada)

# Parsear una cadena a un objeto datetime
fecha_str = "01/09/2024 15:30:00"
fecha_parsed = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M:%S")
print("Fecha parseada:", fecha_parsed)

# Realizar operaciones con fechas
# Agregar 7 días a la fecha actual
nueva_fecha = ahora + timedelta(days=7)
print("Fecha dentro de 7 días:", nueva_fecha)

# Restar 3 días a la fecha actual
fecha_menos_dias = ahora - timedelta(days=3)
print("Fecha hace 3 días:", fecha_menos_dias)

# Calcular la diferencia entre dos fechas
diferencia = nueva_fecha - fecha_menos_dias
print("Diferencia entre fechas:", diferencia)

# Crear una fecha específica
fecha_especifica = datetime(2024, 9, 1, 15, 30, 0)
print("Fecha específica:", fecha_especifica)

# Obtener solo la fecha actual (sin hora)
fecha_solo = date.today()
print("Fecha actual (solo fecha):", fecha_solo)

# Obtener el primer y último día del mes actual
primer_dia_del_mes = fecha_solo.replace(day=1)
ultimo_dia_del_mes = (primer_dia_del_mes + timedelta(days=31)).replace(day=1) - timedelta(days=1)
print("Primer día del mes:", primer_dia_del_mes)
print("Último día del mes:", ultimo_dia_del_mes)

# Encontrar el día de la semana
dia_de_la_semana = ahora.strftime("%A")
print("Día de la semana:", dia_de_la_semana)

# Determinar si un año es bisiesto
def es_bisiesto(año):
    return (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0))

año_actual = ahora.year
print(f"¿El año {año_actual} es bisiesto?", es_bisiesto(año_actual))

# Convertir un objeto datetime a un timestamp (segundos desde Epoch)
timestamp = ahora.timestamp()
print("Timestamp (segundos desde Epoch):", timestamp)

# Convertir un timestamp a un objeto datetime
fecha_desde_timestamp = datetime.fromtimestamp(timestamp)
print("Fecha desde timestamp:", fecha_desde_timestamp)

# Comparar dos fechas
fecha1 = datetime(2024, 1, 1)
fecha2 = datetime(2024, 12, 31)
if fecha1 < fecha2:
    print("La fecha1 es anterior a la fecha2")
else:
    print("La fecha1 es posterior o igual a la fecha2")

# Calcular la edad en años dada una fecha de nacimiento
fecha_nacimiento = datetime(1990, 5, 15)
edad = ahora.year - fecha_nacimiento.year - ((ahora.month, ahora.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
print(f"Edad calculada con la fecha de nacimiento {fecha_nacimiento.date()}: {edad} años")
