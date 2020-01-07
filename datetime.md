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
>>> from datetime import datetime
>>> fn = datetime(1993, 04, 30)
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
1
# Regresa el número del día de la semana al que corresponde la fecha, siendo 1= lunes y así sucesivamente hasta 7= domingo.
```
