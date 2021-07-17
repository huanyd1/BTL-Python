#Nhập thư viện, đặt tên chương trình

import math
from tkinter import *
window = Tk()
window.title("My Caculator")
finish = False

#Gọi sự kiện click
def on_btn_clicked(ch):
    return lambda: on_click(ch)
#Vùng sự kiện click
def on_click(ch):
    global finish
    ch = ch.replace("2nd","").replace("x²","^2").replace("1/x","1/").replace("xʸ","^").replace("|x|","abs(")\
        .replace("√x","√(").replace("n!","!").replace("10ˣ","10^").replace("log","log(").replace("ln","ln(")\
        .replace("exp","exp(")
    if ch == "C":
        on_btn_clear_clicked()
    elif ch == "⌫":
        on_btn_delete_clicked()
    elif ch == "=":
        on_btn_equal_clicked()
    elif ch == "!":
        on_btn_factorial_clicked()
    elif ch == "exp":
        on_btn_exp_clicked()
    elif ch == "+/_":
        on_btn_change_clicked()
    else:
        res = display.get()
        if (len(display.get()) == 1 and display.get() == '0' and not ch in '+-×÷^.') or \
                (not display.get() == 'ERROR' and finish == 1 and ch not in '+-×÷^') or display.get() == 'ERROR':
            display.delete(0, END)
        if res == 'ERROR':
            if ch not in '+-×÷^':
                display.insert(len(display.get()), ch)
                finish = False
            else:
                display.insert(len(display.get()), '0')
        else:
            display.insert(len(display.get()), ch)
            finish = False
#Sự kiện xóa click
def on_btn_clear_clicked():
    display.delete(0, END)

#Sự kiện xóa chuỗi click
def on_btn_delete_clicked():
    display.delete(len(display.get()) - 1)

#Sự kiện tính, xử lí dữ liệu
def on_btn_equal_clicked():
    global finish
    try:
        text = display.get()
        true_number_sentance = text.replace('×', '*').replace('÷', '/').replace('^','**')\
            .replace('π','math.pi').replace('e','math.e').replace('abs','math.fabs').replace('√','math.sqrt')\
            .replace('log','math.log10').replace('ln','math.log').replace('mod','%')
        res = eval(true_number_sentance)
    except Exception:
        res = 'ERROR'
    display.delete(0, END)
    display.insert(0, res)
    finish = True
#Hàm tính giai thừa
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
#Sự kiện tính giai thừa
def on_btn_factorial_clicked():
    global finish
    res = factorial(int(display.get()))
    display.delete(0, END)
    display.insert(0, res)
    finish = True
#Sự kiện tính lũy thừa
def on_btn_exp_clicked():
    global finish
    res = math.exp(float(display.get()))
    display.delete(0, END)
    display.insert(0, res)
    finish = True

#Sự kiện sửa, xử lí lỗi
def on_btn_change_clicked():
    global finish
    res = display.get()
    if (len(display.get()) == 1 and display.get() == '0' and not ch in '+-×÷^') or \
            (not display.get() == 'ERROR' and finish == 1 and ch not in '+-×÷^') or display.get() == 'ERROR':
        display.delete(0, END)
    if res == 'ERROR':
        display.insert(len(display.get()), '-')
        finish = False
    else:
        i = len(display.get())-1
        while res[i] in '1234567890.' and i>0:
            i -= 1
        if res[i] == '-':
            res = res[:i] + '+' + res[i+1:]
        elif res[i] == '+':
            res = res[:i] + '-' + res[i+1:]
        elif i==0:
            res = '-' + res
        else:
            res = res[:i+1] + '(-' + res[i+1:]
        display.delete(0, END)
        display.insert(0,res)
        finish = False
#Tạo màn hình
display = Entry(window, font = ("Tahoma", 20), justify = "right")
display.grid(row = 0, column = 0, padx = 5, pady = 5, columnspan = 5)
#Tạo danh sách button
buttons = ["2nd","π","e","C","⌫", "x²","1/x","|x|","exp","mod", "√x","(",")","n!","÷", "xʸ","7","8","9","×",
           "10ˣ","4","5","6","-", "log","1","2","3","+", "ln","+/_","0",".","="]
for i in range(7):
    for j in range(5):
        ch = buttons[i*5+j]
        btn = Button(window, text = ch, font = ("Tahoma", 20), width = 4, command = on_btn_clicked(ch))
        btn.grid(row = i+1, column = j, padx = 5, pady = 5)
window.mainloop()