from tkinter import *
import random
import time

count = 0
lost = False

class Ball:
    def __init__(self, canvas, paddle, paddle2, target1, target2, color):
        self.canvas = canvas
        self.paddle = paddle
        self.paddle2 = paddle2
        self.target1 = target1
        self.target2 = target2
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 150, 200)
        starts= [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom=False

    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False

    def hit_paddle2(self,pos):
        paddle2_pos=self.canvas.coords(self.paddle2.id)
        if pos[2] >= paddle2_pos[0] and pos[0] <= paddle2_pos[2]:
            if pos[3] >= paddle2_pos[1] and pos[3] <= paddle2_pos[3]:
                return True
            return False

    def hit_target1(self,pos):
        target1_pos=self.canvas.coords(self.target1.id)
        if pos[2] >= target1_pos[0] and pos[0] <= target1_pos[2]:
            if pos[3] >= target1_pos[1] and pos[3] <= target1_pos[3]:
                return True
            return False

    def hit_target2(self,pos):
        target2_pos=self.canvas.coords(self.target2.id)
        if pos[2] >= target2_pos[0] and pos[0] <= target2_pos[2]:
            if pos[3] >= target2_pos[1] and pos[3] <= target2_pos[3]:
                return True
            return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom=True
        if self.hit_paddle(pos)==True:
            self.y=-3
        if self.hit_paddle2(pos)==True:
            self.y=3
        if self.hit_target1(pos)==True:
            self.y=-3
        if self.hit_target2(pos)==True:
            self.y=-3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = 3

            global count
            count +=1
            score()   
        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            self.canvas.move(self.id, 150, 200)
            game_over()
            global lost
            lost = True

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 50, 10, fill=color)
        self.canvas.move(self.id, 150, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def move_left(self, evt):
            self.x = -2

    def move_right(self, evt):
            self.x = 2

class Paddle2:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 50, 10, fill=color)
        self.canvas.move(self.id, 0, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-a>", self.move_left)
        self.canvas.bind_all("<KeyPress-d>", self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def move_left(self, evt):
            self.x = -2

    def move_right(self, evt):
            self.x = 2

class Target1:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 35, 35, fill=color)
        self.canvas.move(self.id, 40, 120)
        self.x = 0

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

class Target2:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 70, 70, fill=color)
        self.canvas.move(self.id, 100, 40)
        self.x = 0

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

def start_game(event):
    global lost, count, ball
    if lost==True:
        ball=Ball(canvas,paddle,paddle2, target1, target2, "red")
    lost = False    
    count = 0
    score()
    canvas.itemconfig(game, text=" ")

def score():
    canvas.itemconfig(score_now, text="score: " + str(count))

def game_over():
    canvas.itemconfig(game, text="Game over :(")

tk = Tk()
tk.title("Guller's Cool Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost", -1)
canvas = Canvas(tk, width=200, height=400, bd=0,highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, "red")
paddle2=Paddle2(canvas, "black")
target1=Target1(canvas, "yellow")
target2=Target2(canvas, "green")
ball = Ball(canvas, paddle, paddle2, target1, target2, "blue")
score_now = canvas.create_text(155, 10, text="score: " + str(count), fill = "red", font=("Tahoma", 12))
game = canvas.create_text(100, 200, text=" ", fill="red", font=("Tahoma", 16))

while 1:
    if ball.hit_bottom==False:
        ball.draw()
        paddle.draw()
        paddle2.draw()
        target1.draw()
        target2.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(1.01)