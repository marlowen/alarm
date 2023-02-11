from datetime import datetime
from tkinter import StringVar, IntVar
from tkinter import messagebox
from tkinter import ttk
from tkinter import Checkbutton
from tkinter import Label
from tkinter import Toplevel
from tkinter import Button
from tkinter.font import Font
from tkinter import *
import time
import webbrowser
import threading


def dia(D, L, M, Mi, J, V, S):
    hoy = datetime.today().strftime("%A")
    Sunday = D
    Monday = L
    Tuesday = M
    Wendsday = Mi
    Thursday = J
    Friday = V
    Saturday = S
    if Sunday == 1:
        if hoy == "Sunday":
            return True
    if Monday == 1:
        if hoy == "Monday":
            return True
    if Tuesday == 1:
        if hoy == "Tuesday":
            return True
    if Wendsday == 1:
        if hoy == "Wednesday":
            return True
    if Thursday == 1:
        if hoy == "Thursday":
            return True
    if Friday == 1:
        if hoy == "Friday":
            return True
    if Saturday == 1:
        if hoy == "Saturday":
            return True
    return False

class Alarmamodel:
    
    alarmahora = ""

    def __init__(self,):
        pass
    
    def alarma_hilo(self,):
        self.alarma_hora = int(self.horaalarma.get())
        self.alarma_minutos = int(self.minutosalarma.get())
        self.top.destroy()
        self.posponer = True
        self.coincide_dia = dia(self.CheckVar1.get(), self.CheckVar2.get(), self.CheckVar3.get(), self.CheckVar4.get(), self.CheckVar5.get(), self.CheckVar6.get(), self.CheckVar7.get())
        self.__class__.alarmahora = f"La alarma sonara a las {self.alarma_hora}:{self.alarma_minutos}"
        while alarmaactiva:
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

    def alarma_hilo_lanzar(self,):
        global alarmaactiva
        alarmaactiva = True
        self.lanzar_hilo = threading.Thread(target=self.alarma_hilo)
        self.lanzar_hilo.start()

    def alarma_desactivar(self,):
        global alarmaactiva
        messagebox.showinfo(message="Desactivaste la alarma", title="Alarma desactivada")
        alarmaactiva = False