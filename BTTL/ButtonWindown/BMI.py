from tkinter import *
window = Tk()
window.title("BMI Caculate")
window.geometry("540x360")
def on_btn_clicked():
    weight = float(txt.get())
    height = float(txt2.get())
    bmi = weight/(height ** 2)
    lbl_bmi['text'] = str(round(bmi,2))
    if bmi < 16:
        lbl_bmi_result['text'] = "Severe Thinness"
    elif bmi < 17:
        lbl_bmi_result['text'] = "Moderate  Thinness"
    elif bmi < 18.5:
        lbl_bmi_result['text'] = "MoMild   Thinness"
    elif bmi < 25:
        lbl_bmi_result['text'] = "Normal"
    elif bmi < 30:
        lbl_bmi_result['text'] = "Overweight"
    elif bmi < 35:
        lbl_bmi_result['text'] = "Obese Class I"
    elif bmi < 40:
        lbl_bmi_result['text'] = "Obese Class II"
    else:
        lbl_bmi_result['text'] = "Obese Class III"

btn = Button(window, text="Caculate", font=("Tahoma", 20), fg="blue", command=on_btn_clicked)
txt = Entry(window, font=("Tahoma", 20), width=8, justify='right')
text = Label(window, text="Weight(kg): ", font=("Tahoma", 20))
txt2 = Entry(window, font=("Tahoma", 20), width=8, justify='right')
text2 = Label(window, text="Height(m): ", font=("Tahoma", 20))
text.grid(row=2, column=0)
txt.grid(row=2, column=1, padx=5, pady=5)
text2.grid(row=3, column=0)
txt2.grid(row=3, column=1, padx=5, pady=5)
btn.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
lbl_bmi = Label(window,  font=("Tahoma", 20), fg = "blue")
lbl_bmi_result = Label(window,  font=("Tahoma", 20), fg = "blue")
lbl_bmi.grid(row=5, column=0, columnspan=2)
lbl_bmi_result.grid(row=6, column=0, columnspan=2)

window.mainloop()