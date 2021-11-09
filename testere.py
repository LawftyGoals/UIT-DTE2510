from tkinter import *

class testere:

    def __init__(self, s):
        self.s = s

    def print(self):
        print(self.s)


t = testere("welcome")

t.print()

"""

        window = Tk()
        window.title("Grid Manager Demo")

        message = Message(window, text="This message widget occupies three rows and two columns")
        message.grid(row = 0, column = 0, rowspan = 3, columnspan = 2)
        Label(window, text = "First name:").grid(row = 0, column = 2)
        Entry(window).grid(row = 0, column = 3, padx = 5, pady = 5)
        Label(window, text = "Last name:").grid(row = 1, column = 2)
        Entry(window).grid(row = 1, column = 3)
        Button(window, text = "Get name").grid(row = 2, padx = 5, pady = 5, column = 3, sticky = W)

        window.mainloop()

        if self.pos_x <= self.width-15 and self.pos_x >= 5 and self.pos_y <= self.height-15 and self.pos_y >= 5:
            self.pos_x += self.speed_x
        else:
            self.speed_x = 0
        if self.pos_y <= self.height-15 and self.pos_y >= 5:

            self.pos_y += self.speed_y
        else:
            self.speed_y = 0

        window.title("Canvas Demo")

        self.canvas = Canvas(window, width = 200, height = 100, bg = "white")
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        bt_rectangle = Button(frame, text = "Rectangle", 
            command = self.display_rect)
        bt_oval = Button(frame, text = "Oval", command = self.display_oval)
        bt_clear = Button(frame, text = "Clear", command = self.clear_canvas)

        bt_rectangle.grid(row = 0, column = 0)
        bt_oval.grid(row = 0, column = 1)
        bt_clear.grid(row = 0, column = 2)

        window.mainloop()

    def display_rect(self):
        self.canvas.create_rectangle(10,10,190,90, activefill = "blue", tags="rect")
    
    def display_oval(self):
        self.canvas.create_oval(55,10,145,90, fill = "red", tags="oval")
    
    def clear_canvas(self):
        self.canvas.delete("rect", "oval")





            window.title("Change label Demo")


        frame1 = Frame(window)
        frame1.pack()
        self.lbl = Label(frame1, text = "Programming is fun")
        self.lbl.pack()

        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text = "Enter text: ")
        self.msg = StringVar()
        entry = Entry(frame2, textvariable = self.msg)
        btChangeText = Button(frame2, text = "change text", command = self.processButton)
        self.v1 = StringVar()
        rbRed = Radiobutton(frame2, text = "Red", bg = "red", variable = self.v1,
            value = 'R', command = self.processRadiobutton)
        rbYellow = Radiobutton(frame2, text = "Yellow", bg = "yellow", variable = self.v1,
            value = 'Y', command = self.processRadiobutton)
        
        label.grid(row = 1, column = 1)
        entry.grid(row = 1, column = 2)
        btChangeText.grid(row = 1, column = 3)
        rbRed.grid(row = 1, column = 4)
        rbYellow.grid(row = 1, column = 5)

        window.mainloop()

    def processRadiobutton(self):
        if self.v1.get() == 'R':
            self.lbl["fg"] = "red"
        elif self.v1.get() == 'Y':
            self.lbl["fg"] = "yellow"

    def processButton(self):
        self.lbl["text"] = self.msg.get()
        print("shit")



    def __init__(self):
        window = Tk()
        window.title("Widgets Demo")

        frame1 = Frame(window)
        frame1.pack()
        self.v1 = IntVar()

        cbtBold = Checkbutton(frame1, text = "Bold",
            variable = self.v1, command = self.processCheckbutton)
        self.v2 = IntVar()
        rbRed = Radiobutton(frame1, text = "Red", bg = "red", 
            variable = self.v2, value = 1, command = self.processRadiobutton)
        rbYellow = Radiobutton(frame1, text = "Yellow", bg = "yellow", 
            variable = self.v2, value = 2, command = self.processRadiobutton)
        cbtBold.grid(row = 1, column = 1)
        rbRed.grid(row = 1, column = 2)
        rbYellow.grid(row = 1, column = 3)

        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text = "Enter your name: ")
        self.name = StringVar()
        entryName = Entry(frame2, textvariable = self.name)
        btGetName = Button(frame2, text = "Get Name", command = self.processButton)
        message = Message(frame2, text = "It is a widgets demo")
        label.grid(row = 1, column = 1)
        entryName.grid(row = 1, column = 2)
        btGetName.grid(row = 1, column = 3)
        message.grid(row = 1, column = 4)

        text = Text(window)
        text.pack()
        text.insert(END, "Tip\nThe best way to learn Tkinter is to read ")
        text.insert(END, "these carfully designed examples and use them ")
        text.insert(END, "to create your applications.")

        window. mainloop()
    
    def processCheckbutton(self):
        print("check button is " + ("checked" if self.v1.get() == 1 else "unchecked"))
    
    def processRadiobutton(self):
        print(("Red" if self.v2.get() == 1 else "Yellow") + " is selected ")
    
    def processButton(self):
        print("Your name is " + self.name.get())

testere()

   def __init__(self):
        window = Tk()
        btOK = Button(window, text = "ok", fg = "red", command = self.processOK)
        btCancel = Button(window, text = "cancel", bg = "yellow", command = self.processCancel)
        btOK.pack()
        btCancel.pack()

        window.mainloop()
    
    def processOK(self):
        print("OK button is clicked")
    
    def processCancel(self):
        print("Cancel Button is clicked")

testere()
"""


#def essOK():
#    print("OK button is clicked")
#
#def  essCancel():
#    print("Cancel butoon is clicked")

#window =Tk()
#btOK = Button(window, text = "OK", fg = "red", command = essOK)
#btCancel = Button(window, text = "Cancel", bg = "yellow", command = essCancel)
#btOK.pack()
#btCancel.pack()

#window.mainloop()


#import os

#dirList = os.listdir()

#for i in dirList:
#    if 'DTEO' in i:
#        j = i.replace("DTEO","DTE2510")
#        os.rename(i,j)
