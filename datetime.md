### Epoch
Los sistemas Linux/UNIX tiene un contador de tiempo que inidica su inicio la medianoche (12:00 AM) del jueves 1 de enero de 1970 a esta fecha se le conoce como "epoch".

### La tupla de fecha y hora.
(<Año en cuatro cifras>, <número de mesde 1 a 12>, <número de día del mes de 0 a 31>, <hora del día de 0 a 23>,  <minutos de 0 a 60>, <segundos de 0 a 61>, <dia de la semana de 0(lunes) a 6(domingo>, <día del año de 1 a 366>, <valor entero de -1 a 1 para indicar si se apega a un esquema de ahorro de energía>)

### Módulo time
Este módulo permite realizar algunas operaciones básicas de fecha y hora.
```python
import time

time.time()
# Regresa el número de segundos transcurridos desde "epoch".

time.sleep(5)
# Permite detener la ejecución de un script durante un tiempo defindo en segundos.
```

## datetime
Permite crear objetos de fecha y hora, ingresando una sucesión de datos en forma de una tupla de tiempo.
```python
>>> from datetime import datetime, timedelta, date
>>> fn = datetime(1993, 4, 30)
>>> datetime.datetime(1993, 4, 30, 0, 0)
>>> fn.month
4
>>> fn.year
1993
>>> fn.date()
datetime.date(1993, 4, 30)
>>> datetime.now()
datetime.datetime(2020, 1, 6, 23, 22, 51, 363383)
>>> datetime.isoweekday(datetime.now())
# Regresa el número del día de la semana al que corresponde la fecha, siendo 1= lunes y así sucesivamente hasta 7= domingo.
1
```

#### Mostrar fecha y hora
```
ahora = datetime.now()  # Obtiene fecha y hora actual
ahora.utcnow()  # Muestra fecha/hora UTC
ahora.day  # Muestra día
ahora.month  # Muestra mes
ahora.year  # Muestra año
ahora.hour  # Muestra hora
ahora.minute  # Muestra minuto
ahora.second  # Muestra segundo
ahora.microsecond  # Muestra microsegundo
```

#### Comparando fechas y horas
```python
fecha1 = date.today()  # Asigna fecha actual
fecha2 = date.today() + timedelta(days=2)
fecha1 > fecha2  # False
```

#### Aplicando formatos a fechas y horas
```python
%a 	Nombre local abreviado de día de semana
%A 	Nombre local completo de día de semana
%b 	Nombre local abreviado de mes
%B 	Nombre local completo de mes
%d 	Día de mes [01,31]
%H 	Hora (horario 24 horas) [00,23]
%I 	Hora (horario 12 horas) [01,12]
%j 	Número de día del año [001,366]
%m 	Mes [01,12]
%M 	Minuto [00,59]
%p 	Etiqueta AM o PM
%S 	Segundo
%U 	Nº semana del año. Se considera al Domingo como primer día de semana [00,53]
%w 	Establece el primer día de semana [0(Domingo),1(Lunes)... 6].
%W 	Nº semana del año (Se considera al Lunes como primer día de semana) [00,53]
%y 	Año en formato corto [00,99]
%Y 	Año en formato largo
%Z 	Nombre de Zona Horaria
```
##### Ejemplos
```python
>>> formato1 = "%a %b %d %H:%M:%S %Y"
>>> formato2 = "%d-%m-%y %I:%m %p"
>>> hoy = datetime.today()  # Asigna fecha-hora en formato ISO 8601
>>> hoy.strftime(formato1)
'Mon Jan 06 23:38:45 2020'
>>> hoy.strftime(formato2)  
'06-01-20 11:01 PM'
```

### Convertir una cadena a objeto datetime
```python
>>> cadena1 = hoy.strftime(formato1)
>>> datetime.strptime(cadena1, formato1)
datetime.datetime(2020, 1, 6, 23, 38, 45)
```

### Operaciones con fechas y horas
```python
ayer = hoy – timedelta(days=1)  # Resta a fecha actual 1 día
mañana = hoy + timedelta(days=1)  # Suma a fecha actual 1 día
diferencia_en_dias = mañana – hoy  # Resta las dos fechas
```
