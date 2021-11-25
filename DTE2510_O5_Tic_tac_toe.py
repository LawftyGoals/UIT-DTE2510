from tkinter import *
from Cell import *

class Tic_Tac_Toe:
    def __init__(self):
# Self.turn concerns which player's turn it is, after making a press the turn is multiplied by -1.
# +1 is x, -1 is o. Game_ended when true signals the game is over and someone has won.
        self.turn = 1
        self.game_ended = False

        window = Tk()
        window.title("Tic-Tac-Toe")

# importing images
        self.x_image = PhotoImage(file="x.gif")
        self.o_image = PhotoImage(file="o.gif")
        empty_image = PhotoImage(file="empty.gif")

        frame1 = Frame(window, background="black")
        frame1.pack()

# set up a Cell class object that expands on the Label class.

        self.lbl1 = Cell(frame1, image=empty_image)
        self.lbl2 = Cell(frame1, image=empty_image)
        self.lbl3 = Cell(frame1, image=empty_image)
        self.lbl4 = Cell(frame1, image=empty_image)
        self.lbl5 = Cell(frame1, image=empty_image)
        self.lbl6 = Cell(frame1, image=empty_image)
        self.lbl7 = Cell(frame1, image=empty_image)
        self.lbl8 = Cell(frame1, image=empty_image)
        self.lbl9 = Cell(frame1, image=empty_image)

# this list adds all the Cell labels to keep them in 1 place for processing later in the
# check phase (check if any 3s have been made.)
        self.lbl_list = [self.lbl1, self.lbl2, self.lbl3,
            self.lbl4, self.lbl5, self.lbl6, 
            self.lbl7, self.lbl8, self.lbl9]
        
# button 1 is bound to each of the label objects. whe the object is pressed it calls thë́
# the processMouseEvent which checks if 3s have been made after each press.
        
        self.lbl1.bind("<Button-1>", self.processMouseEvent)
        self.lbl2.bind("<Button-1>", self.processMouseEvent)
        self.lbl3.bind("<Button-1>", self.processMouseEvent)
        self.lbl4.bind("<Button-1>", self.processMouseEvent)
        self.lbl5.bind("<Button-1>", self.processMouseEvent)
        self.lbl6.bind("<Button-1>", self.processMouseEvent)
        self.lbl7.bind("<Button-1>", self.processMouseEvent)
        self.lbl8.bind("<Button-1>", self.processMouseEvent)
        self.lbl9.bind("<Button-1>", self.processMouseEvent)


        self.lbl1.grid(row=0, column=0, padx=2, pady=2)
        self.lbl2.grid(row=0, column=1, padx=2, pady=2)
        self.lbl3.grid(row=0, column=2, padx=2, pady=2)
        self.lbl4.grid(row=1, column=0, padx=2, pady=2)
        self.lbl5.grid(row=1, column=1, padx=2, pady=2)
        self.lbl6.grid(row=1, column=2, padx=2, pady=2)
        self.lbl7.grid(row=2, column=0, padx=2, pady=2)
        self.lbl8.grid(row=2, column=1, padx=2, pady=2)
        self.lbl9.grid(row=2, column=2, padx=2, pady=2)

        frame2 = Frame(window)
        frame2.pack()
    
# here is the label that notifys of the state of the game.

        self.lblgs = Label(frame2, text="Tic-Tac-Toe")
        self.lblgs.grid()

        window.mainloop()

    def processMouseEvent(self, event):
#processMouseEvent first sets an image to an empty tile or ignores it if the image is blank
# tells the player if the token is already set.

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

# Checks the rows to see if there are any 3s, on horizontal, diagonal or vertical sets
        self.check_rows()
            

    def check_rows(self):
# initially sets up a array containing 3 arrays, this will give us the horizontals. each of the
# 3 belonging values into each level.
        horizontals = [[],[],[]]
        for i in range(3):
            horizontals[0].append(self.lbl_list[i].state)
        for ii in range(3,6):
            horizontals[1].append(self.lbl_list[ii].state)   
        for iii in range(6,9):
            horizontals[2].append(self.lbl_list[iii].state)

# Now the horizontals are used to set up vertical sets.
        verticals = [[],[],[]]
        for j in range(3):
            for jj in range(3):
                verticals[j].append(horizontals[jj][j])
        
# now the diagonals are done.
        diagonals = [[],[]]
        for k in range(3):
            diagonals[0].append(horizontals[k][k])
            diagonals[1].append(horizontals[2-k][k])


# The rest of the code checks if there are either 3 x or 3 o in any of the lists, horizontal,
# verticals and diagonal

        if ["X","X","X"] in verticals or ["X","X","X"] in horizontals or ["X","X","X"] in diagonals:
            self.game_ended = True
            self.lblgs["text"] = "Game is over, X has won!"
        
        if ["O","O","O"] in verticals or ["O","O","O"] in horizontals or ["O","O","O"] in diagonals:
            self.game_ended = True
            self.lblgs["text"] = "Game is over, O has won!"

#this part of the code checks if all the tokens are filled and if so but no one has won delcares
# a draw.
        filled = 0
        for kk in self.lbl_list:
            if kk.state != "":
                filled += 1

        if filled >= 9:
            self.game_ended = True
            self.lblgs["text"] = "Game is over, it's a draw!"



Tic_Tac_Toe()
