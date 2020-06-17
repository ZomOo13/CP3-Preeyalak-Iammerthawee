from tkinter import *
import math

def leftClick(event):
    BMI = (float(textBoxW.get()) / math.pow(float(textBoxH.get()) / 100, 2))
    print(BMI)
    if BMI >= 30:
        labelResult.configure(text=BMI)
        result.configure(text="อ้วนมาก")
    elif BMI >= 25:
        labelResult.configure(text=BMI)
        result.configure(text="อ้วน")
    elif BMI >= 23:
        labelResult.configure(text=BMI)
        result.configure(text="น้ำหนักเกิน")
    elif BMI >= 18.6:
        labelResult.configure(text=BMI)
        result.configure(text="น้ำหนักปกติ เหมาะสม")
    elif BMI <= 18.5:
        labelResult.configure(text=BMI)
        result.configure(text="ผอมเกินไป")
    else:
        print("ERROR !!!")

mWindow = Tk()
labelH = Label(mWindow,text ="ส่วนสูง (cm)").grid(row=0,column=0)
textBoxH = Entry(mWindow)
textBoxH.grid(row=0,column=1)
labelW = Label(mWindow,text ="น้ำหนัก (kg)").grid(row=1,column=0)
textBoxW = Entry(mWindow)
textBoxW.grid(row=1,column=1)
calButton = Button(mWindow,text = "คำนวณ")
calButton.bind('<Button-1>',leftClick)
calButton.grid(row=2,column=0)
labelResult = Label(mWindow,text ="ผลลัพธ์")
labelResult.grid(row=2,column=1)
result = Label(mWindow,text = "ผลประเมิน",fg="blue")
result.grid(row=3,column=1)
mWindow.mainloop()



