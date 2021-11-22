from tkinter import *
from Cell import *

class Tic_Tac_Toe:
    def __init__(self):

        self.turn = 1
        self.game_ended = False

        window = Tk()
        window.title("Tic-Tac-Toe")

        self.x_image = PhotoImage(file="x.gif")
        self.o_image = PhotoImage(file="o.gif")
        empty_image = PhotoImage(file="empty.gif")

        frame1 = Frame(window)
        frame1.pack()

        self.lbl1 = Cell(frame1, image=empty_image)
        self.lbl2 = Cell(frame1, image=empty_image)
        self.lbl3 = Cell(frame1, image=empty_image)
        self.lbl4 = Cell(frame1, image=empty_image)
        self.lbl5 = Cell(frame1, image=empty_image)
        self.lbl6 = Cell(frame1, image=empty_image)
        self.lbl7 = Cell(frame1, image=empty_image)
        self.lbl8 = Cell(frame1, image=empty_image)
        self.lbl9 = Cell(frame1, image=empty_image)

        self.lbl_list = [self.lbl1, self.lbl2, self.lbl3,
            self.lbl4, self.lbl5, self.lbl6, 
            self.lbl7, self.lbl8, self.lbl9]
        
        self.lbl1.bind("<Button-1>", self.processMouseEvent)
        self.lbl2.bind("<Button-1>", self.processMouseEvent)
        self.lbl3.bind("<Button-1>", self.processMouseEvent)
        self.lbl4.bind("<Button-1>", self.processMouseEvent)
        self.lbl5.bind("<Button-1>", self.processMouseEvent)
        self.lbl6.bind("<Button-1>", self.processMouseEvent)
        self.lbl7.bind("<Button-1>", self.processMouseEvent)
        self.lbl8.bind("<Button-1>", self.processMouseEvent)
        self.lbl9.bind("<Button-1>", self.processMouseEvent)


        self.lbl1.grid(row=0, column=0)
        self.lbl2.grid(row=0, column=1)
        self.lbl3.grid(row=0, column=2)
        self.lbl4.grid(row=1, column=0)
        self.lbl5.grid(row=1, column=1)
        self.lbl6.grid(row=1, column=2)
        self.lbl7.grid(row=2, column=0)
        self.lbl8.grid(row=2, column=1)
        self.lbl9.grid(row=2, column=2)

        frame2 = Frame(window)
        frame2.pack()

        self.lblgs = Label(frame2, text="Tic-Tac-Toe")
        self.lblgs.grid()

        window.mainloop()

    def processMouseEvent(self, event):
        if self.game_ended == False:
            print(event.widget.state)
            if self.turn == 1 and event.widget.state == "":
                event.widget["image"] = self.x_image
                event.widget.state = "X"
                self.lblgs["text"] = "X set, O's turn"
                self.turn*=-1

            elif self.turn == -1 and event.widget.state == "":
                event.widget["image"] = self.o_image
                event.widget.state = "O"
                self.lblgs["text"] = "O set, x's turn"
                self.turn*=-1
            else:
                print("Else")
                self.lblgs["text"] = "Token already set"
        else:
            pass
        self.check_rows()
            

    def check_rows(self):
        horizontals = [[],[],[]]
        for i in range(3):
            horizontals[0].append(self.lbl_list[i].state)
        for ii in range(3,6):
            horizontals[1].append(self.lbl_list[ii].state)   
        for iii in range(6,9):
            horizontals[2].append(self.lbl_list[iii].state)
        
        print(horizontals)

        verticals = [[],[],[]]
        for j in range(3):
            for jj in range(3):
                verticals[j].append(horizontals[jj][j])
        
        print(verticals)

        diagonals = [[],[]]
        for k in range(3):
            diagonals[0].append(horizontals[k][k])
            diagonals[1].append(horizontals[2-k][k])

        print(diagonals)

        if ["X","X","X"] in verticals or ["X","X","X"] in horizontals or ["X","X","X"] in diagonals:
            self.game_ended = True
            self.lblgs["text"] = "Game is over, X has won!"
        
        if ["O","O","O"] in verticals or ["O","O","O"] in horizontals or ["O","O","O"] in diagonals:
            self.game_ended = True
            self.lblgs["text"] = "Game is over, O has won!"

Tic_Tac_Toe()
