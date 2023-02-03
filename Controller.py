from tkinter import Tk
from view import AlarmaView


class AlarmaController:
    
    def __init__(self, window):
        self.window = window
        self.visual = AlarmaView(self.window)
        self.visual.alarma_lanzar()


if __name__ == "__main__":
    root = Tk()
    app = AlarmaController(root)
    root.mainloop()