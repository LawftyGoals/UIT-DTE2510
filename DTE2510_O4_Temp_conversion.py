from tkinter import *

class Temp_conversion:
    def __init__(self):
        
        self.previous_cel = 0.0
        self.previous_faren = 0.0

        window = Tk()
        window.title("Temp Conversion")

        frame1 = Frame(window)
        frame1.pack()

        self.cel = StringVar()
        self.faren = StringVar()

        enter_cel = Entry(frame1, textvariable= self.cel)
        enter_faren = Entry(frame1, textvariable= self.faren)

        self.lbl1 = Label(frame1)

        convert_button = Button(frame1, text = "Convert", command = self.process_conversion)

        enter_cel.grid(row = 1, column = 0)
        enter_faren.grid(row = 1, column = 1)
        self.lbl1.grid(row = 0, column = 1, sticky = W)
        convert_button.grid(row = 1, column = 2)

        window.mainloop()


    
    def process_conversion(self):
        if self.cel.get() == "" and self.faren.get() == "":
            cel = 0.0
            faren = 0.0
        elif self.cel.get() == "":
            cel = 0.0
            faren = float(self.faren.get())
        elif self.faren.get() == "":
            faren = 0.0
            cel = float(self.cel.get())
        else:
            faren = float(self.faren.get())
            cel = float(self.cel.get())

        if (cel == self.previous_cel):
            self.lbl1["text"] = str(round((faren-32.0)*(5/9), 1)) + " Celsius"
            self.previous_faren = faren

        elif(faren == self.previous_faren):
            self.lbl1["text"] = str(round((cel*(5/9))+32.0, 1)) + " Farenheit"
            self.previous_cel = cel


Temp_conversion()