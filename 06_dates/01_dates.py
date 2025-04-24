# Trabajando con fechas y horas en python

from os import system

if system("clear") != 0:
    system("cls")

from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_TIME, "es_AR.UTF-8")

# 1. obtener fecha y hora acutal
now = datetime.now()
print(f"Fecha y hora actual {now}")

# 2. Crear fecha y hora específica
specific_date = datetime(2025, 10, 14)
print(f"Fecha y hora específica {specific_date}")

# 3. Formatear fechas
# stringftime()

format_date = now.strftime("%d-%m-%y")
print(format_date)

format_date = now.strftime("%A %d-%m-%y")
print(format_date)

# 4. Operaciones con fechas

yesterday = datetime.now() - timedelta(days=1)
print(yesterday)

# 5. Obtener componentes de una fecha

year = now.year
month = now.month

print(year, month)

# 6. Calcular diferencia entre fechas

date1 = datetime.now()
date2 = datetime(2025, 10, 1)

difference = date2 - date1

print(difference)
