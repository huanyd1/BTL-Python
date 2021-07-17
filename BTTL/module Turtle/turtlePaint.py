# 3. Vẽ hình vuông màu đỏ, độ dày nét vẽ = 3, độ dài cạnh = 120.
# from turtle import *
# color("red")
# pensize(3)
# for i in range(4):
#     forward(120)
#     right(90)

#4. Đặt hình cho bút vẽ thành hình chú rùa, và tốc độ vẽ chậm nhất, 
#vẽ hình tam giác đều màu cam, độ dày nét vẽ = 5, độ dài cạnh = 150, 
#khi vẽ xong thì ẩn chú rùa đi

# import turtle
# t = turtle.Turtle()
# t.color("orange")
# t.speed("slowest")
# t.shape("turtle")
# t.pensize(5)
# for i in range(3):
#     t.forward(150)
#     t.left(120)
# t.hideturtle()

#5. Vẽ hai hình vuông như theo mẫu sau

# import turtle
# t = turtle.Turtle()
# t.color("green")
# t.pensize(3)
# for i in range(4):
#     t.forward(120)
#     t.right(90)
# t.penup()
# t.forward(170)
# t.pendown()
# for i in range(4):
#     t.forward(120)
#     t.right(90)
# t.hideturtle()

#6. Vẽ một hình vuông, một hình tam giác, và một hình chữ nhật cạnh nhau, 
#theo thứ tự và màu sắc như sau:

# import turtle
# t = turtle.Turtle()
# t.color("green")
# t.pensize(3)
# for i in range(4):
#     t.forward(120)
#     t.left(90)

# t.penup()
# t.forward(170)
# t.pendown()
# t.color("orange")
# for i in range(3):
#     t.forward(120)
#     t.left(120)

# t.penup()
# t.backward(110)
# t.right(90)
# t.forward(40)
# t.pendown()
# t.color("blue")
# for i in range(2):
#     t.forward(80)
#     t.left(90)
#     t.forward(180)
#     t.left(90)
# t.hideturtle()    


#7. Vẽ 6 vạch ngang màu xanh lá cây như mẫu bên dưới,
#mỗi cạnh dài 100 bước, và cách nhau 20 bước.

# import turtle
# t = turtle.Turtle()
# t.color("green")
# t.pensize(3)
# for i in range(5):
#     t.forward(100)
#     t.penup()
#     t.right(90)
#     t.forward(20)
#     t.right(-90)
#     t.pendown()
#     t.backward(100)
# t.hideturtle()

#8. Vẽ 6 bậc thang theo mẫu:

# import turtle
# t = turtle.Turtle()
# t.color("green")
# t.pensize(3)
# for i in range(6):
#     t.left(90)
#     t.forward(20)
#     t.right(90)
#     t.forward(20)
# t.hideturtle()

#9. Vẽ tam giác vuông sau bằng cách sử dụng hàm goto(x, y) 

# import turtle
# t = turtle.Turtle()
# t.color("green")
# t.pensize(3)
# t.goto(90,0)
# t.goto(90,90)
# t.goto(0,0)
# t.hideturtle()

#10. Vẽ hình bên, bao gồm một tam giác vuông và tam giác cân
#có cạnh bằng cạnh huyền của tam giác vuông. 

# import turtle
# t = turtle.Turtle()
# t.color("green")
# t.pensize(3)
# t.goto(90,0)
# t.goto(90,90)
# t.goto(0,0)

# t.sety(127.2)
# t.goto(90,90)

# t.hideturtle()

#11. Vẽ hình vuông nghiêng 15 độ theo chiều kim đồng hồ như hình mẫu.

# import turtle
# t = turtle.Turtle()
# t.color("green")
# t.pensize(3)
# t.setheading(-15)
# for i in range(4):
#     t.forward(120)
#     t.right(90)
# t.hideturtle()


#1. Vẽ hình sau:

# import turtle; t=turtle.Turtle(); 
# t.pensize(2)
# for i in range(3):
#   t.color("yellow")
#   t.fd(100); t.lt(150);
#   t.color(['purple', 'pink', 'green'][i])
#   t.fd(57); t.bk(57); t.rt(30)

#2. Vẽ ba bông hoa như hình mẫu.
# import turtle
# t = turtle.Turtle()
# t.speed(0)
# t.pensize(4)
# t.color('red')
# for i in range(1):
#   t.fd(190)
#   t.lt(90)
#   t.fd(90)
# t.lt(90)
# for i in range(1):
#   t.fd(200)
#   t.lt(90)
#   t.fd(90)
# t.lt(90)

# t.fd(30)
# t.lt(90)
# t.fd(4)
# t.color('white')
# t.fd(20)
# t.color('brown')
# t.fd(30)
# t.color('yellow')
# for i in range(10):
#   t.rt(36)
#   t.fd(20)
#   t.bk(20)
# t.lt(180)
# t.penup()
# t.fd(54)
# t.lt(90)
# t.fd(70)
# t.lt(90)
# t.fd(10)
# t.pendown()
# t.color('green')
# t.fd(30)
# t.color('pink')
# for i in range(10):
#   t.rt(36)
#   t.fd(20)
#   t.bk(20)
# t.lt(180)
# t.penup()
# t.fd(44)
# t.lt(90)
# t.fd(70)
# t.lt(90)
# t.fd(30)
# t.pendown()
# t.color('green')
# t.fd(30)
# t.color('purple')
# for i in range(10):
#   t.rt(36)
#   t.fd(20)
#   t.bk(20)

#3. Vẽ sân bóng đá như hình mẫu.
# import turtle

# t = turtle.Turtle()
# t.reset()
# t.color('green')
# t.pensize(3)
# t.pu()
# t.speed(5)

# def myrectangle(length, width):
#   for i in range(1, 3):
#     t.fd(length)
#     t.lt(90)
#     t.fd(width)
#     t.lt(90)

# t.goto(-120, -80)
# t.pd()
# myrectangle(240, 160)
# t.fd(120)
# t.lt(90)
# t.fd(160)
# t.rt(90)
# t.pu()
# t.goto(-120, -60)
# t.pd()
# t.fd(30)
# t.lt(90)
# t.fd(120)
# t.lt(90)
# t.fd(30)
# t.pu()
# t.goto(120, -60)
# t.pd()
# t.fd(30)
# t.rt(90)
# t.fd(120)
# t.rt(90)
# t.fd(30)
# t.pu()
# t.goto(0, -10)
# t.pd()
# t.circle(10)

#4. Vẽ hình sau:

# import turtle as t 
# t.pensize(4)
# t.speed(0)
# t.color('yellow')
# t.circle(50)
# t.rt(90)
# t.color('blue')
# t.circle(50)
# t.rt(90)
# t.color('green')
# t.circle(50)
# t.rt(90)
# t.color('purple')
# t.circle(50)
# t.done()

#Vẽ quốc kỳ Việt Nam

# import turtle
# t = turtle.Turtle()
# t.color('red')
# t.pensize(5)
# t.shape('arrow')
# t.speed(0)


# t.begin_fill()
# for i in range(4):
#   t.fd(100)
#   t.rt(90)
# t.end_fill()  

# t.pu()
# t.goto(20, -40)
# t.color('yellow')
# t.begin_fill()
# for i in range(5):
#   t.fd(60)
#   t.rt(144)
# t.end_fill()  


#1. Vẽ hình sau:

# from turtle import *
# color('green', 'yellow')
# pensize(5)
# begin_fill()
# circle(100)
# end_fill()
# hideturtle()


#2. Vẽ hình sau:

# from turtle import *
# color('green', 'yellow')
# begin_fill()
# circle(100, extent=90)
# goto(100,0)
# home()
# end_fill()
# hideturtle()
# done()





#Vẽ quả bóng màu xanh chuyển động qua lại ngang màn hình 
#(đến biên của bảng vẽ thì chuyển động ngược lại).

# from turtle import *
# import time
# tracer(0)
# color("green")
# for i in range(100):
#     for i in range(-50, 50):
#         clear()
#         pu();    goto(i*5, 0);    pd()
#         begin_fill()
#         circle(20)
#         end_fill()
#         ht()
#         update()
#         time.sleep(0.02)

#     for i in range(-50, 50):
#         clear()
#         pu();    goto(-i*5, 0);    pd()
#         begin_fill()
#         circle(20)
#         end_fill()
#         ht()
#         update()
#         time.sleep(0.02)