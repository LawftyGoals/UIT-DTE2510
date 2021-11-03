from tkinter import *

class testere:

    def __init__(self):
        window = Tk()
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
        btChangeText = Button(frame2, text = "change text", command =self.processButton)
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
        
testere()



"""
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
