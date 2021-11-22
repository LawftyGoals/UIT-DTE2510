from tkinter import *

class Cell(Label):
    def __init__(self, frame: Frame, image = None, textr = ""):
        super().__init__(frame, text=textr, image = image)
        self.state = ""


