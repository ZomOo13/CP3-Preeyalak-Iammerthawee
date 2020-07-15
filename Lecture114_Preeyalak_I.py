from tkinter import *
from tkinter import ttk
from forex_python.converter import CurrencyRates, CurrencyCodes


rate = CurrencyRates()
code = CurrencyCodes()


def Result(event):
    result = (rate.convert(first_currency_box.get(), convert_currency_box.get(), float(amount.get())))
    convert_result.configure(text = result)

def NameRates(event):
    name = code.get_currency_name(),

main_window = Tk()
title = Label(main_window, text = "การคำนวนอัตราแลกเปลี่ยนเงินตรา", bg = "yellow", font=("Saraban",12))
title.grid(row = 0 , column = 1)
first_currency = Label(main_window, text ="จาก :")
first_currency.grid(row = 1 , column = 0)
first_currency_box = ttk.Combobox(main_window)
first_currency_box['values'] = list(rate.get_rates("").keys())
first_currency_box.current(29)
first_currency_box.bind("<<ComboboxSelected>>")
first_currency_box.grid(row = 1 , column = 1)
text = Label(main_window, text = "จำนวนเงิน")
text.grid(row = 4 , column = 2)
amount = Entry(main_window, text = "ใส่จำนวนเงิน")
amount.grid(row = 1 , column = 3)
convert_currency = Label(main_window, text = "เป็น :")
convert_currency.grid(row = 5 , column = 0)
convert_currency_box = ttk.Combobox(main_window)
convert_currency_box['values'] = list(rate.get_rates("").keys())
convert_currency_box.current(10)
convert_currency_box.bind("<<ComboboxSelected>>")
convert_currency_box.grid(row = 5 , column = 1)
convert_result = Label(main_window, text = "ผลลัพธ์")
convert_result.grid(row = 5 , column = 3)
convert_button = Button(main_window, text = "แปลง", width=15)
convert_button.bind('<Button-1>', Result)
convert_button.grid(row = 4 , column = 4)


main_window.mainloop()