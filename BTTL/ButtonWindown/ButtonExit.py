from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("BMI Caculate")
window.geometry("540x360")
def on_closing():
    confirm = messagebox.askyesnocancel("Want to quit?", "Do you really want to exit?", default=messagebox.YES)
    if confirm:
        window.quit()
window.protocol("WM_DELETE_WINDOWS", on_closing)
# print(*font.families(), sep = '\n')
# print(len(font.families()))
btn = Button(window, text = "Exit", font = ("Tahoma", 24), fg = "blue", command=on_closing)
btn.pack()
window.mainloop()