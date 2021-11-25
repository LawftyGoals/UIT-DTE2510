from tkinter import *

#This Cell object expands the Label class. It includes several arguments that are passed into 
# initialization of the super. Amongst these is text, image and a background color.
# none of these are in use except for image per now.
class Cell(Label):
    def __init__(self, frame: Frame, image = None, textr = "", bg = None):
        super().__init__(frame, text=textr, image = image, bg=bg)
        self.state = ""


