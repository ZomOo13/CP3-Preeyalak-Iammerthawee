from tkinter import *
import math

def leftClick(event):
    BMI = (float(textBoxW.get()) / math.pow(float(textBoxH.get()) / 100, 2))
    print(BMI)
    if BMI >= 30:
        labelResult.configure(text=BMI)
        labelR.configure(text="อ้วนมาก")
        result.configure(text = "ค่อนข้างอันตราย เสี่ยงต่อการเกิดโรคร้ายแรงที่แฝงมากับความอ้วน หากค่า BMI อยู่ในระดับนี้ จะต้องปรับพฤติกรรมการทานอาหาร และควรเริ่มออกกำลังกาย และหากเลขยิ่งสูงกว่า 40.0 ยิ่งแสดงถึงความอ้วนที่มากขึ้น ควรไปตรวจสุขภาพ และปรึกษาแพทย์")
    elif BMI >= 25:
        labelResult.configure(text=BMI)
        labelR.configure(text="อ้วน")
        result.configure(text="อ้วนในระดับหนึ่ง ถึงแม้จะไม่ถึงเกณฑ์ที่ถือว่าอ้วนมาก ๆ แต่ก็ยังมีความเสี่ยงต่อการเกิดโรคที่มากับความอ้วนได้เช่นกัน ทั้งโรคเบาหวาน และความดันโลหิตสูง ควรปรับพฤติกรรมการทานอาหาร ออกกำลังกาย และตรวจสุขภาพ")
    elif BMI >= 18.6:
        labelResult.configure(text=BMI)
        labelR.configure(text="น้ำหนักปกติ")
        result.configure(text="น้ำหนักที่เหมาะสมสำหรับคนไทยคือค่า BMI ระหว่าง 18.5-24 จัดอยู่ในเกณฑ์ปกติ ห่างไกลโรคที่เกิดจากความอ้วน และมีความเสี่ยงต่อการเกิดโรคต่าง ๆ น้อยที่สุด ควรพยายามรักษาระดับค่า BMI ให้อยู่ในระดับนี้ให้นานที่สุด และควรตรวจสุขภาพทุกปี")
    elif BMI <= 18.5:
        labelResult.configure(text=BMI)
        labelR.configure(text="ผอมเกินไป")
        result.configure(text="น้ำหนักน้อยกว่าปกติก็ไม่ค่อยดี หากคุณสูงมากแต่น้ำหนักน้อยเกินไป อาจเสี่ยงต่อการได้รับสารอาหารไม่เพียงพอหรือได้รับพลังงานไม่เพียงพอ ส่งผลให้ร่างกายอ่อนเพลียง่าย การรับประทานอาหารให้เพียงพอ และการออกกำลังกายเพื่อเสริมสร้างกล้ามเนื้อสามารถช่วยเพิ่มค่า BMI ให้อยู่ในเกณฑ์ปกติได้",)


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
labelR = Label(mWindow)
labelR.grid(row=3,column=0)
result = Label(mWindow,text = "ผลประเมิน")
result.grid(row=3,column=1)
mWindow.mainloop()



