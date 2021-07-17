import tkinter as tk

root = tk.Tk()
#Xét tỉ lệ chiều dài, chiều rộng
width = 900
height = 500

canvas = tk.Canvas(root, bg='black', width=width, height=height)
canvas.pack()

ball = canvas.create_oval(430, 10, 470, 50, fill='green')

platform_y = height - 20
platform = canvas.create_rectangle(width//2-50, platform_y, width//2+50, platform_y+10, fill='white')

# Chỉnh sửa tốc độ di chuyển của bóng
xspeed = yspeed = 2

def move_ball():
  global xspeed, yspeed
  x1, y1, x2, y2 = canvas.coords(ball)
  if x1 <= 0 or x2 >= width:
    # chạm tường và đảo ngược tốc độ của trục x
    xspeed = -xspeed
  if y1 <= 0:
    # Va vào bức tường trên cùng và xét tốc độ trục y
    yspeed = 2
  elif y2 >= platform_y:
    # tính trọng tâm của bóng
    cx = (x1 + x2) // 2
    # Kiểm tra xem bóng có bị chạm vào thanh không
    px1, _, px2, _ = canvas.coords(platform)
    if px1 <= cx <= px2:
      yspeed = -2
    else:
      canvas.create_text(width//2, height//2, text='Game Over', font=('Arial Bold', 32), fill='red')
      return
  canvas.move(ball, xspeed, yspeed)
  canvas.after(20, move_ball)

def board_right(event):
  x1, y1, x2, y2 = canvas.coords(platform)
  # Ngăn không cho thanh vượt quá bên phải
  if x2 < width:
    dx = min(width-x2, 10)
    canvas.move(platform, dx, 0)

def board_left(event):
  x1, y1, x2, y2 = canvas.coords(platform)
  # Ngược lại ngăn không cho thanh vượt quá bên trái
  if x1 > 0:
    dx = min(x1, 10)
    canvas.move(platform, -dx, 0)

canvas.bind_all('<Right>', board_right)
canvas.bind_all('<Left>', board_left)

move_ball()

root.mainloop()

#Chú thích biến
# width : chiều rộng
# height : chiều dài
# canvas : tạo canvas
# ball : tạo ball
# platform : tạo thanh ngang
# xspeed : tốc độ di chuyển trục x
# yspeed : tốc độ di chuyển trục y
