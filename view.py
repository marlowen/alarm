from tkinter import Label, StringVar, IntVar
from tkinter import Button
from tkinter import Frame
from tkinter import Toplevel
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import threading
from tkinter.font import Font
from model import dia, Alarmamodel
from datetime import datetime
import time


class AlarmaView:

    """Clase encargada de generar la ventana"""

    def __init__(
        self, ventana
    ):
        self.window = ventana
        self.window.title("Alarma")

        self.frame = Frame()
        self.frame.pack()

        global _alarmahora
        global _alarmahora3
        global texto_boton_alarma1
        global texto_boton_alarma2
        global hora
        hora = StringVar()
        global fecha
        fecha = StringVar()

        _alarmahora = StringVar()
        _alarmahora3 = StringVar()
        texto_boton_alarma1 = StringVar()
        texto_boton_alarma2 = StringVar()
        _alarmahora.set("Alarma 1 desactivada")
        _alarmahora3.set("Alarma 2 desactivada")
        texto_boton_alarma1.set("Activar alarma 1")
        texto_boton_alarma2.set("Activar alarma 2")

        self.horaactual = Label(self.frame, textvariable=hora, font=("digitalk", 100), bd=3)
        self.horaactual.pack(anchor="center")

        self.fecha = Label(self.frame, textvariable=fecha, font=("digitalk", 30))
        self.fecha.pack(anchor="center")
        self.alarmahora = Label(self.frame, textvariable=_alarmahora, font=("digitalk", 15))
        self.alarmahora.pack(anchor="center")
        self.alarmahora3 = Label(self.frame, textvariable=_alarmahora3, font=("digitalk", 15))
        self.alarmahora3.pack(anchor="center")
        
        self.boton_alarma = Button(self.frame, textvariable=texto_boton_alarma1 , font=("digitalk", 20), command=self.alarma_lanzar2)
        self.boton_alarma.pack(anchor="center", side="right", padx=15, pady=15)

        self.boton_alarma2 = Button(self.frame, textvariable=texto_boton_alarma2 , font=("digitalk", 20), command=self.alarma_lanzar3)
        self.boton_alarma2.pack(anchor="center", side="right", padx=15, pady=15)
        
        self.boton_cerrar = Button(self.frame, text="Cerrar" , font=("digitalk", 20), command=self.close)
        self.boton_cerrar.pack(anchor="center", side="bottom", padx=15, pady=15)

    def hora_hilo(self,):
        while True:
            self.horaminutos = datetime.now()
            self.horaminutos = self.horaminutos.strftime("%H:%M:%S")
            hora.set(self.horaminutos)
            self.fechahoy = datetime.now()
            self.fechahoy = self.fechahoy.strftime("%A, %d/%m/%Y")
            fecha.set(self.fechahoy)
            time.sleep(0.5)
        
    def alarma_lanzar(self,):
        lanzar_hilo = threading.Thread(target=self.hora_hilo)
        lanzar_hilo.start()
    
    def alarma_lanzar2(self,):
        texto_boton_alarma1.set("Desactivar alarma 1")
        self.boton_alarma.configure(command=self.alarma_desactivar2)
        self.Alarmainstacia2 = Alarmamodel()
        self.Alarmainstacia2.alarma_activa()
        _alarmahora.set(self.Alarmainstacia2.alarmahora)
    
    def alarma_desactivar2(self,):
        texto_boton_alarma1.set("Activar alarma 1")
        self.boton_alarma.configure(command=self.alarma_lanzar2)
        _alarmahora.set("Alarma 1 desactivada")
        self.Alarmainstacia2.alarma_desactivar()

    def alarma_lanzar3(self,):
        texto_boton_alarma2.set("Desactivar alarma 2")
        self.boton_alarma2.configure(command=self.alarma_desactivar3)
        self.Alarmainstacia3 = Alarmamodel()
        self.Alarmainstacia3.alarma_activa()
        _alarmahora3.set(self.Alarmainstacia3.alarmahora)
    
    def alarma_desactivar3(self,):
        texto_boton_alarma2.set("Activar alarma 2")
        self.boton_alarma2.configure(command=self.alarma_lanzar3)
        _alarmahora3.set("Alarma 2 desactivada")
        self.Alarmainstacia3.alarma_desactivar()
    
    def close(self,):
        if texto_boton_alarma1.get() == "Desactivar alarma 1":
            self.Alarmainstacia2.alarma_desactivar()
        if texto_boton_alarma2.get() == "Desactivar alarma 2":
            self.Alarmainstacia3.alarma_desactivar()
        self.window.destroy()