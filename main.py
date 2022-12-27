
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Исключения")
root.geometry("250x200")

nums = (list(range(100+1)))
label1 = Label(root, text = "Введите число от 1 до 100")
label1.pack()


def show():
    m = e1.get()
    try:
        s = int(m)
        label2 = Label(root,text = nums[s]).pack()
    except IndexError:
        label3 = Label(root,text='Числа  не существует').pack()
e1 = ttk.Entry(root)
e1.pack()

b1=Button(root,text='Click',command=show).pack()


root.mainloop()