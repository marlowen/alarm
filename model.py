from datetime import datetime
from tkinter import IntVar
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

    def __init__(self,):
        pass
    
    def alarma_activa(self, ventana, label1):
        self.window = ventana
        self.label1 = label1
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

        self.boton_activar_alarma = Button(self.top, text="Activar", font=("digitalk", 20) , command=lambda: self.alarma_hilo_lanzar(self.window))
        self.boton_activar_alarma.pack(anchor="center", side="right", padx=15, pady=15)
        self.top.mainloop()

    def alarma_hilo_lanzar(self, ventana):
        self.window = ventana
        self.alarma_hora = int(self.horaalarma.get())
        self.alarma_minutos = int(self.minutosalarma.get())
        self.top.destroy()
        self.posponer = True
        self.coincide_dia = dia(self.CheckVar1.get(), self.CheckVar2.get(), self.CheckVar3.get(), self.CheckVar4.get(), self.CheckVar5.get(), self.CheckVar6.get(), self.CheckVar7.get())
        self.label1.set(f"La alarma sonara a las {self.alarma_hora}:{self.alarma_minutos}")
        self.alarma_lanzar2()
        
    def alarma_lanzar2(self,): 
        hora = int(datetime.now().hour)
        minutos = int(datetime.now().minute)
        if hora == self.alarma_hora and minutos == self.alarma_minutos and self.coincide_dia == True:   
            while self.posponer:
                webbrowser.open_new('https://www.youtube.com/watch?v=x4ZEezBOC7g')
                self.posponer = messagebox.askokcancel(message="¿Desea continuar?", title="Posponer")
                if self.posponer is True:
                    time.sleep(300)
        self.alarma_despertador = self.window.after(30000, self.alarma_lanzar2)
        
    def alarma_desactivar(self, ventana):
        messagebox.showinfo(message="Desactivaste la alarma", title="Alarma desactivada")
        self.window = ventana
        self.window.after_cancel(self.alarma_despertador)