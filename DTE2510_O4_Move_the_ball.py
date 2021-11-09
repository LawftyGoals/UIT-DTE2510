from tkinter import *

class Move_the_ball:

    def __init__(self):

        window = Tk()
        window.title("Move the Ball")

        self.width = 250
        self.height = 150
        self.canvas = Canvas(window, bg = "white", width = self.width, height = self.height)
        self.canvas.pack()

        self.pos_x = 120
        self.pos_y = 70

        self.canvas.create_oval(self.pos_x, self.pos_y, self.pos_x+10, 
            self.pos_y+10, fill = "black", tag = "oval")
        
        self.speed_x = 5
        self.speed_y = 5

        frame1 = Frame(window)
        frame1.pack()

        bt_left = Button(frame1, text = "Left", command = self.move_left)
        bt_left.pack(side = LEFT)
        bt_right = Button(frame1, text = "Right", command = self.move_right)
        bt_right.pack(side = LEFT)
        bt_up = Button(frame1, text = "Up", command = self.move_up)
        bt_up.pack(side = LEFT)
        bt_down = Button(frame1, text = "Down", command = self.move_down)
        bt_down.pack(side = LEFT)

        window.mainloop()
    

    def speed(self, direction_x: int, direction_y: int):
        
        self.canvas.move("oval", direction_x, direction_y)

        self.pos_x += direction_x
        self.pos_y += direction_y
        
    def move_left(self):
        if self.pos_x > 5:
            self.speed(-(self.speed_x), 0)
    
    def move_right(self):
        if self.pos_x < self.width-15:
            self.speed((self.speed_x), 0)
    
    def move_up(self):
        if self.pos_y > 5:
            self.speed(0, -(self.speed_y))
    
    def move_down(self):
        if self.pos_y < self.height-15:
            self.speed(0, (self.speed_y))


Move_the_ball()

