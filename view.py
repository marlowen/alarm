from tkinter import Label, StringVar, IntVar
from tkinter import Button
from tkinter import Frame
from tkinter import Toplevel
from tkinter import ttk
from tkinter import messagebox
from tkinter import Radiobutton
from tkinter import *
from datetime import datetime
import time
import threading
import webbrowser
from tkinter.font import Font
from model import dia


class AlarmaView:

    """Clase encargada de generar la ventana"""

    def __init__(
        self, ventana
    ):
        self.window = ventana
        self.window.title("Alarma")

        self.frame = Frame()
        self.frame.pack()

        global hora
        global fecha
        global _alarmahora
        global mensaje_boton_alarma
        self.alarmaactiva = False
        hora = StringVar()
        fecha = StringVar()
        _alarmahora = StringVar()
        mensaje_boton_alarma = StringVar()
        _alarmahora.set("Alarma desactivada")
        mensaje_boton_alarma.set("Activar alarma")

        self.horaactual = Label(self.frame, textvariable=hora, font=("digitalk", 100), bd=3)
        self.horaactual.pack(anchor="center")

        self.fecha = Label(self.frame, textvariable=fecha, font=("digitalk", 30))
        self.fecha.pack(anchor="center")
        self.alarmahora = Label(self.frame, textvariable=_alarmahora, font=("digitalk", 15))
        self.alarmahora.pack(anchor="center")
        self.boton_alarma = Button(self.frame, textvariable=mensaje_boton_alarma , font=("digitalk", 20) , command=self.alarma_activa)
        self.boton_alarma.pack(anchor="center", side="right", padx=15, pady=15)

    def hora_hilo(self,):
        while True:
            self.horaminutos = datetime.now()
            self.horaminutos = self.horaminutos.strftime("%H:%M:%S")
            hora.set(self.horaminutos)
            self.fechahoy = datetime.now()
            self.fechahoy = self.fechahoy.strftime("%A, %d/%m/%Y")
            fecha.set(self.fechahoy)
            time.sleep(1)

    def alarma_hilo(self,):
        self.alarma_hora = int(self.horaalarma.get())
        self.alarma_minutos = int(self.minutosalarma.get())
        self.top.destroy()
        self.alarmaactiva = True
        self.posponer = True
        self.coincide_dia = dia(self.CheckVar1.get(), self.CheckVar2.get(), self.CheckVar3.get(), self.CheckVar4.get(), self.CheckVar5.get(), self.CheckVar6.get(), self.CheckVar7.get())
        _alarmahora.set(f"La alarma sonara a las {self.alarma_hora}:{self.alarma_minutos}")
        while self.alarmaactiva:
            hora = int(datetime.now().hour)
            minutos = int(datetime.now().minute)
            if hora == self.alarma_hora and minutos == self.alarma_minutos and self.coincide_dia == True:   
                while self.posponer:
                    webbrowser.open_new('https://www.youtube.com/watch?v=x4ZEezBOC7g')
                    self.posponer = messagebox.askokcancel(message="¿Desea continuar?", title="Posponer")
                    time.sleep(300)
    
    def alarma_activa(self,):
        self._hora = []
        self._minutos = []
        self.rabo_hora = IntVar()
        self.CheckVar1 = IntVar()
        self.CheckVar2 = IntVar()
        self.CheckVar3 = IntVar()
        self.CheckVar4 = IntVar()
        self.CheckVar5 = IntVar()
        self.CheckVar6 = IntVar()
        self.CheckVar7 = IntVar()
        for x in range(0,24):
            self._hora.append(x)
        for x in range(0,60):
            self._minutos.append(x)

        if self.alarmaactiva == False:
            self.top = Toplevel()
            self.top.title("Definir Alarma")
            self.font = Font(family = "digitalk", size = 15)
            self.top.option_add("*TCombobox*Listbox*Font", self.font)
            
            self.horaalarmalabel = Label(self.top, text="Seleccionar hora", font=("digitalk", 15))
            self.horaalarmalabel.pack(anchor="center", padx=15, pady=15)
            self.horaalarma = ttk.Combobox(self.top, values=self._hora, font=("digitalk", 15))
            self.horaalarma.pack(anchor="center", padx=15, pady=15)
            self.horaalarma.current(0)
            
            self.minutosalarmalabel = Label(self.top, text="Seleccionar minuto", font=("digitalk", 15))
            self.minutosalarmalabel.pack(anchor="center", padx=15, pady=15)
            self.minutosalarma = ttk.Combobox(self.top, values=self._minutos, font=("digitalk", 15))
            self.minutosalarma.pack(anchor="center", padx=15, pady=15)
            self.minutosalarma.current(0)
            
            self.diaalarmalabel = Label(self.top, text="Seleccionar Dia", font=("digitalk", 15))
            self.diaalarmalabel.pack(anchor="center", padx=15, pady=15)
            
            self.diaD = Checkbutton(self.top, text="Domingo", variable=self.CheckVar1, font=("digitalk", 12)).pack(anchor=W)
            self.diaL = Checkbutton(self.top, text="Lunes", variable=self.CheckVar2, font=("digitalk", 12)).pack(anchor=W)
            self.diaM = Checkbutton(self.top, text="Martes", variable=self.CheckVar3, font=("digitalk", 12)).pack(anchor=W)
            self.diaMi = Checkbutton(self.top, text="Miercoles", variable=self.CheckVar4, font=("digitalk", 12)).pack(anchor=W)
            self.diaJ = Checkbutton(self.top, text="Jueves", variable=self.CheckVar5, font=("digitalk", 12)).pack(anchor=W)
            self.diaV = Checkbutton(self.top, text="Viernes", variable=self.CheckVar6, font=("digitalk", 12)).pack(anchor=W)
            self.diaS = Checkbutton(self.top, text="Sabado", variable=self.CheckVar7, font=("digitalk", 12)).pack(anchor=W)

            self.boton_activar_alarma = Button(self.top, text="Activar", font=("digitalk", 20) , command=self.alarma_hilo_lanzar)
            self.boton_activar_alarma.pack(anchor="center", side="right", padx=15, pady=15)
            self.top.mainloop()
        else:
            mensaje_boton_alarma.set("Activar alarma")
            self.alarmaactiva = False
            messagebox.showinfo(message="Desactivaste la alarma", title="Alarma desactivada")
            _alarmahora.set("Alarma desactivada")

    def alarma_lanzar(self,):
        lanzar_hilo = threading.Thread(target=self.hora_hilo)
        lanzar_hilo.start()
    
    def alarma_hilo_lanzar(self,):
        mensaje_boton_alarma.set("Desactivar alarma")
        lanzar_hilo_alarma = threading.Thread(target=self.alarma_hilo)
        lanzar_hilo_alarma.start()