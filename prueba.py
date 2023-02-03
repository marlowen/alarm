from datetime import datetime

hora = int(datetime.now().hour)
minutos = int(datetime.now().minute)
print(hora)
print(minutos)
if hora == 11 and minutos == 12:
    print(hora + ":" + minutos)