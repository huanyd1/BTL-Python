#Khai báo thư viện Tkinter
from tkinter import *
import random
import  time
import PIL.Image
from playsound import playsound
from threading import Thread
import winsound
import tkinter

#Khai báo biến sử dụng
is_game_over = False
#Khai báo background
end_game_bg = None
#Khai báo điểm số
end_game_score = None
ms = 20
#Khai báo biến điểm số
score = 0
#Khai báo biến level
level = 1
#Khai báo biến điểm cộng
plus = 1

window = Tk()
#Khai báo tiêu đề cửa sổ
window.title('Flappy bird')
#Khai báo kích thước của cửa sổ
cw, ch = 540, 960
#Khai báo Canvas , chiều dài, chiều rộng, background, dộ dày viền

canvas = Canvas(window, width = cw, height = ch, bg = "LightBlue", highlightthickness = 0)
canvas.pack()
bg_img = PhotoImage(file="D:/Python/BTTL/Game/sky.png")
bg = canvas.create_image(50 ,50 , image = bg_img)

#Định dạng Canvas
d = 200

#Khai báo ống bên trên : chiều dài, chiều rộng, màu, đường viền
pipeup= canvas.create_rectangle(cw - 100, 0, cw, 350, fill = '#58FA82', outline = '#000000')
#Khai báo ống bên dưới : chiều dài, chiều rộng, màu, đường viền
pipedown = canvas.create_rectangle(cw - 100, 600, cw, ch, fill = '#58FA82', outline = '#000000')
#Khai báo biến text sử dụng
text = canvas.create_text(15,60,fill="#FF0000",font=("Script",40),text="Score: " + str(score), anchor=W)
#Khai báo biến text level
lv_text = canvas.create_text(400,60,fill="#FF0000",font=("Script",40),text="Lv. " + str(level), anchor=W)
#Khai báo đường dẫn ảnh chim
# bird_img = PhotoImage(file ="bird.gif")
canvas.images = list()
canvas.images.append(tkinter.PhotoImage(file="D:/Python/BTTL/Game/bird1.png"))
canvas.images.append(tkinter.PhotoImage(file="D:/Python/BTTL/Game/bird2.png"))
canvas.images.append(tkinter.PhotoImage(file="D:/Python/BTTL/Game/bird3.png"))

#Khai báo đối tượng chim
bird = canvas.create_image((50, 50), image=canvas.images[0])


#Khai báo biến trọng lực
gravity = 0
#Khai báo tốc độ chim tăng dần
acer = 0.5
def animate_and_move(i):
    i = (i + 1) % 2
    canvas.itemconfig(bird, image=canvas.images[i])
    canvas.move(bird, 1, 1)
    canvas.after(100, animate_and_move, i)
#Khai báo hàm chim rơi xuống
def bird_fall():
    global gravity, acer, is_game_over
    if is_game_over:
        return
    #Khai báo tọa độ chim
    x1, y1 = canvas.coords(bird)
    #Biến trọng lực tăng dần
    y1 += gravity
    #Biến tốc độ tăng dần
    gravity += acer
    #Nếu tọa độ chim > chiều cao thì trả về Game Over
    if y1 > ch:
        audio_bird_die()
        game_over()
    canvas.coords(bird, x1, y1)
    #Sau 20ms chim rơi
    window.after(20, bird_fall)

up_count = 0
#Khai báo chim bay lên
def bird_up(evt=None):
    global up_count, gravity, is_game_over
    #Nếu là biến is_game_over thì restart game
    if is_game_over:
        restart_game()
        return
    #Lấy tọa độ chim    
    x1, y1 = canvas.coords(bird)
    gravity = 0
    y1 -= 25 - up_count * 5
    if up_count < 5:
        
        up_count += 1
        window.after(20, bird_up)
    else:
        audio_bird()
        up_count = 0
    canvas.coords(bird, x1, y1)

#Khai báo hàm di chuyển ống
def move_pipe():
    global  plus, is_game_over, score, ms, level
    if is_game_over:
        return
    x1, y1 , x2, y2 = canvas.coords(pipeup)
    x1 -= 5
    if x1 < -100:
        x1 = cw
        y2 = random.randint(100, ch - 350)
        plus = 0
    canvas.coords(pipeup, x1, 0, x1 + 100, y2)
    canvas.coords(pipedown, x1, y2 + 250, x1 + 100, ch)
    check_col()

    window.after(int(ms), move_pipe)

#Khai báo hàm kiểm tra va chạm
def check_col():
    global score, plus, is_game_over, ms, level
    if is_game_over:
        return
    bird_w = 100
    bird_h = 70
    x, y = canvas.coords(bird)
    xp, yp, xp2, yp2 = canvas.coords(pipeup)
    if x < xp2 and x + bird_w > xp + 50 and (y + bird_h > yp2 + 250 or y < yp2):
        audio_bird_die()
        game_over()
    elif y > yp2:
        if plus == 0:
            score += 1
            #Nếu điểm khác 0 và điểm chia hết cho 10 thì cộng lv thêm 1 và tăng tốc độ rơi 0,9 lần
            if score != 0 and score % 5 == 0:
                level += 1
                ms *= 0.9
            plus = 1
            #Sửa giá trị canvas
            canvas.itemconfig(text, text= "Score: " + str(score))
            canvas.itemconfig(lv_text, text="Lv. " + str(level))

move_pipe()
bird_fall()

#Hàm khai báo kết thúc game
def game_over():
    global is_game_over, end_game_bg, end_game_score
    is_game_over = True
    end_game_bg = canvas.create_rectangle(0, 0, cw, ch, fill = "#000000", outline = "white")
    # end_game_img = PhotoImage(file = "background_img.png")
    # end_game_bg = canvas.create_image(50, 50, Image= end_game_img)
    #In ra số điểm
    audio_bird_point()
    end_game_score = canvas.create_text(15,450,fill="#ffffff",font=("Script",70), text="Your score is: " + str(score), anchor=W)
#Hàm khởi động lại game
def restart_game():
    #Thiết lập lại các biến
    global is_game_over, end_game_bg, end_game_score, score, gravity, level, ms
    canvas.delete(end_game_bg)
    canvas.delete(end_game_score)
    #Thiết lập lại chỉ số 
    score = 0
    canvas.itemconfig(text, text="Score: " + str(score))
    level = 1
    canvas.itemconfig(lv_text, text="Lv. " + str(level))
    ms = 20
    canvas.coords(bird, 100, ch // 2)
    canvas.coords(pipeup, cw - 100, 0, cw, 350)
    canvas.coords(pipedown, cw - 100, 600, cw, ch)
    is_game_over = False
    gravity = 0
    move_pipe()
    bird_fall()

#Thiết lập âm thanh
def audio_bird():  
    winsound.PlaySound('D:/Python/BTTL/Game/sfx_wing.wav',  winsound.SND_ASYNC | winsound.SND_ALIAS )
def audio_bird_die():
    winsound.PlaySound('D:/Python/BTTL/Game/sfx_die.wav', winsound.SND_ASYNC| winsound.SND_ALIAS)
def audio_bird_point():
    winsound.PlaySound('D:/Python/BTTL/Game/sfx_point.wav', winsound.SND_ASYNC| winsound.SND_ALIAS)
animate_and_move(0)
#Thiết lập nút bấm
window.bind('<space>', bird_up)
window.mainloop()