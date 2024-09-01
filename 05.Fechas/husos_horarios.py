from datetime import datetime, timedelta
import pytz

# Obtener la fecha y hora actuales en UTC
utc_now = datetime.now(pytz.utc)
print("Fecha y hora actuales en UTC:", utc_now)

# Definir la zona horaria para Nueva York y Tokio
tz_ny = pytz.timezone('America/New_York')
tz_tokyo = pytz.timezone('Asia/Tokyo')

# Convertir la hora actual en UTC a las zonas horarias especificadas
ny_time = utc_now.astimezone(tz_ny)
tokyo_time = utc_now.astimezone(tz_tokyo)
print("Hora en Nueva York:", ny_time)
print("Hora en Tokio:", tokyo_time)

# Crear un objeto datetime en una zona horaria específica
dt_ny = tz_ny.localize(datetime(2024, 9, 1, 15, 30, 0))
print("Fecha y hora en Nueva York:", dt_ny)

# Convertir una hora en una zona horaria específica a UTC
dt_ny_utc = dt_ny.astimezone(pytz.utc)
print("Fecha y hora en UTC desde Nueva York:", dt_ny_utc)

# Calcular la diferencia entre dos zonas horarias
diff = ny_time - tokyo_time
print("Diferencia entre Nueva York y Tokio:", diff)

# Obtener la información sobre la zona horaria actual
print("Información sobre la zona horaria en Nueva York:", tz_ny)
print("Información sobre la zona horaria en Tokio:", tz_tokyo)

# Manejar la conversión entre una hora en una zona horaria y otra
dt_tokyo_converted = dt_ny.astimezone(tz_tokyo)
print("Fecha y hora en Tokio convertida desde Nueva York:", dt_tokyo_converted)