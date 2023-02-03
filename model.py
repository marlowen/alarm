from datetime import datetime
import time
import webbrowser

class AlarmaModel:
    _hora = int(input("Hora de alarma: "))
    _minutos = int(input("Minutos de alarma: "))
    _posponer = input("Posponer alarma (Y/N): ").upper()

    while True:
        hora = int(datetime.now().hour)
        minutos = int(datetime.now().minute)

        if hora == _hora and minutos == _minutos:
            while _posponer == "Y":
                webbrowser.open_new('https://www.youtube.com/watch?v=x4ZEezBOC7g')
                _posponer = input("Posponer alarma (Y/N): ").upper()
                if _posponer == "Y":
                    time.sleep(300)
                else:
                    _posponer = "N"
