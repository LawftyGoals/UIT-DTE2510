from tkinter import *

class buttons_and_radiobuttons:
    def __init__(self):
        window = Tk()
        window.title("Buttons and Radiobuttons")

        frame1 = Frame(window)
        frame1.pack()

        self.v1 = StringVar()
        rb_red = Radiobutton(frame1, text="Red", bg = "red", variable = self.v1, 
            value="R", command = self.process_radiobutton)
        rb_yellow = Radiobutton(frame1, text="Yellow", bg = "yellow", 
            variable = self.v1, value="Y", command = self.process_radiobutton)
        rb_white = Radiobutton(frame1, text="White", bg = "white", 
            variable = self.v1, value="W", command = self.process_radiobutton)
        rb_gray = Radiobutton(frame1, text="Gray", bg = "gray", 
            variable = self.v1, value="G", command = self.process_radiobutton)
        rb_green = Radiobutton(frame1, text="Green", bg = "green", 
            variable = self.v1, value="GR", command = self.process_radiobutton)

        self.text = Text(window, height = 10, width = 40)
        self.text.pack()
        self.text.insert(END, "Welcome")

        frame2 = Frame(window)
        frame2.pack()
        
        rb_left = Button(frame2, text="<=", bg = "white", command = self.process_left_space)
        rb_right = Button(frame2, text="=>", bg = "white", command = self.process_right_space)
        
        rb_red.grid(row = 0, column = 0)
        rb_yellow.grid(row = 0, column = 1)
        rb_white.grid(row = 0, column = 2)
        rb_gray.grid(row = 0, column = 3)
        rb_green.grid(row = 0, column = 4)

        rb_left.grid(row = 0, column = 0)
        rb_right.grid(row = 0, column = 1)

        window.mainloop()
    
    def process_radiobutton(self):
        print(self.v1)
        if self.v1.get() == "R":
            self.text["bg"] = "red"
        if self.v1.get() == "Y":
            self.text["bg"] = "yellow"
        if self.v1.get() == "W":
            self.text["bg"] = "white"
        if self.v1.get() == "G":
            self.text["bg"] = "gray"
        if self.v1.get() == "GR":
            self.text["bg"] = "green"

        

    def process_left_space(self):
        if self.text.get("0.0") != "W":
            self.text.delete("0.0")
        print("3")
        
    def process_right_space(self):
        self.text.insert("0.0", " ")
        print("1")

buttons_and_radiobuttons()