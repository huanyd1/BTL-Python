from tkinter import *
import time

WIDTH = 800
HEIGHT = 500
SIZE = 50
tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="blue")
canvas.pack()
color = 'black'

class Ball:
    def __init__(self, tag):
        self.shape = canvas.create_oval(0, 0, SIZE, SIZE, fill=color, tags=tag)
        self.speedx = 9 # changed from 3 to 9
        self.speedy = 9 # changed from 3 to 9
        self.active = True

    def ball_update(self):
        canvas.move(self.shape, self.speedx, self.speedy)
        pos = canvas.coords(self.shape)
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.speedx *= -1
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.speedy *= -1

global switcher
switcher = True
def cycle():
    global switcher
    canvas.tag_raise("bg")
    if switcher:
        ball2.ball_update()
        ball2.ball_update()
        canvas.tag_raise("ball")
    else:
        ball.ball_update()
        ball.ball_update()
        canvas.tag_raise("ball2")
    tk.update_idletasks()
    switcher = not switcher
    tk.after(40, cycle)

bg = canvas.create_rectangle(0, 0, WIDTH+1, HEIGHT+1, fill="gray", tags="bg")
ball = Ball("ball")
ball.ball_update()
ball2 = Ball("ball2")

tk.after(0, cycle)
tk.mainloop()