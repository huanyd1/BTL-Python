from tkinter import *
window = Tk()
window.title('My Caculator')
finish = False
def on_btn_clicked(ch):
    return lambda: on_click(ch)
def on_click(ch):
    global finish
    if ch == 'C':
        on_btn_clear_clicked()
    elif ch == '=':
        on_btn_equal_clicked()
    elif ch == '%':
        on_btn_percent_clicked()
    else:
        res = display.get()
        if (len(display.get()) == 1 and display.get() == '0' and not ch in '+-*/^') or \
                (not display.get() == 'ERROR' and finish == 1 and ch not in '+-*/^') or display.get() == 'ERROR':
            display.delete(0, END)
        if res == 'ERROR':
            if ch not in '+-*/^':
                display.insert(len(display.get()), ch)
                finish = False
            else:
                display.insert(len(display.get()), '0')
        else:
            display.insert(len(display.get()), ch)
            finish = False
def on_btn_clear_clicked():
    global finish
    if finish:
        display.delete(0, END)
        display.insert(0, 0)
    else:
        display.delete(len(display.get()) - 1)
def on_btn_equal_clicked():
    global finish
    try:
        text = display.get()
        true_number_sentance = text.replace('^', '**')
        res = eval(true_number_sentance)
    except Exception:
        res = 'ERROR'
    display.delete(0, END)
    display.insert(0, res)
    finish = True
def on_btn_percent_clicked():
    global finish
    res = float(display.get()) / 100
    display.delete(0, END)
    display.insert(0, res)
    finish = True
display = Entry(window, font = ('Tahoma', 20), width = 30, justify = 'right')
display.grid(row = 0, column = 0, columnspan=4, padx = 5, pady = 5)
buttons = ['C()%', '789/', '456*', '123-' , '0.=+', '^']
for i in range(len(buttons)):
    line = buttons[i]
    for j in range(len(line)):
        ch = line[j]
        btn = Button(window, text = ch, font = ('Tahoma', 20), command = on_btn_clicked(ch))
        btn.grid(row=i + 1, column=j, sticky = 'nesw', padx = 5, pady = 5)
window.mainloop()