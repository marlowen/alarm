from tkinter import Label, StringVar
from tkinter import Button
from tkinter import Frame
from tkinter import Toplevel
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import time
import threading
import webbrowser
from tkinter.font import Font


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
        self.alarmaactiva = False
        hora = StringVar()
        fecha = StringVar()
        _alarmahora = StringVar()
        _alarmahora.set("Alarma desactivada")

        self.horaactual = Label(self.frame, textvariable=hora, font=("digitalk", 100), bd=3)
        self.horaactual.pack(anchor="center")

        self.fecha = Label(self.frame, textvariable=fecha, font=("digitalk", 30))
        self.fecha.pack(anchor="center")
        self.alarmahora = Label(self.frame, textvariable=_alarmahora, font=("digitalk", 15))
        self.alarmahora.pack(anchor="center")
        self.boton_alarma = Button(self.frame, text="Activar Alarma", font=("digitalk", 20) , command=self.alarma_activa)
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
        _alarmahora.set(f"La alarma sonara a las {self.alarma_hora}:{self.alarma_minutos}")
        while self.alarmaactiva:
            hora = int(datetime.now().hour)
            minutos = int(datetime.now().minute)
            if hora == self.alarma_hora and minutos == self.alarma_minutos:   
                while self.posponer:
                    webbrowser.open_new('https://www.youtube.com/watch?v=x4ZEezBOC7g')
                    self.posponer = messagebox.askokcancel(message="¿Desea continuar?", title="Posponer")
                    time.sleep(300)
    
    def alarma_activa(self,):
        self._hora = []
        self._minutos = []
        for x in range(0,24):
            self._hora.append(x)
        for x in range(0,60):
            self._minutos.append(x)

        if self.alarmaactiva == False:
            self.top = Toplevel()
            self.top.geometry("300x200")
            self.top.title("Definir Alarma")
            self.font = Font(family = "digitalk", size = 15)
            self.top.option_add("*TCombobox*Listbox*Font", self.font)
            self.horaalarma = ttk.Combobox(self.top, values=self._hora, font=("digitalk", 15))
            self.horaalarma.pack(anchor="center", padx=15, pady=15)
            self.horaalarma.current(0)
            self.minutosalarma = ttk.Combobox(self.top, values=self._minutos, font=("digitalk", 15))
            self.minutosalarma.pack(anchor="center", padx=15, pady=15)
            self.minutosalarma.current(0)
            self.boton_activar_alarma = Button(self.top, text="Activar", font=("digitalk", 20) , command=self.alarma_hilo_lanzar)
            self.boton_activar_alarma.pack(anchor="center", side="right", padx=15, pady=15)
            self.top.mainloop()
        else:
            self.alarmaactiva = False
            messagebox.showinfo(message="Desactivaste la alarma", title="Alarma desactivada")
            _alarmahora.set("Alarma desactivada")

    def alarma_lanzar(self,):
        lanzar_hilo = threading.Thread(target=self.hora_hilo)
        lanzar_hilo.start()
    
    def alarma_hilo_lanzar(self,):
        lanzar_hilo_alarma = threading.Thread(target=self.alarma_hilo)
        lanzar_hilo_alarma.start()