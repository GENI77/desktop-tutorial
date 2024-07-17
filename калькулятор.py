import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    answer_entry.delete(first=0, last='end')
    answer_entry.insert(index=0, value)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)







window = tk.Tk()
window.title('Калькулятор')
window.geometry('350x350')
window.resizable(width=False, height=False)
button_and = tk.Button(window, text='+', width=2, height=2, command=add)
button_and.place(x=100, y=200)
button_sub = tk.Button(window, text='-', width=2, height=2)
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, text='*', width=2, height=2)
button_mul.place(x=200, y=200)
button_dif = tk.Button(window, text='/', width=2, height=2)
button_dif.place(x=250, y=200)
number1_entry = tk.Entry(window, width=28)
number1_entry.place(x=100, y=75)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=275)
number1 = tk.Label(window, text='Введите первое число')
number1.place(x=100, y=50)
number2 = tk.Label(window, text='Введите второе число')
number2.place(x=100, y=125)
number3 = tk.Label(window, text='Ответ')
number3.place(x=100, y=250)
window.mainloop()