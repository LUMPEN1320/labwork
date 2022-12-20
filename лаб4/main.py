import tkinter
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Курс по программированию")
root.geometry("350x400")

def reg():
    root1 = Tk()
    root1.title("Курс по программированию")
    root1.geometry("300x50+400+250")

    Name = e1.get()

    label4 = ttk.Label(root1, text=f"Регистрация прошла успешно,{Name}")
    label4.pack()

    def destroy():
        root1.quit()
    b2 = ttk.Button(root1,text='OK',command=destroy)
    b2.place(x=120,y=20)

def select_level():
    level = level_var.get()
    if level == 1:
        label7=Label(root,text='Ваш курс будет построен на легком уровне').place(x=60,y=220)
    elif level==2:
        label8=Label(root,text='Ваш курс будет построен на среднем уровне').place(x=60,y=220)
    elif level == 3:
        label9 = Label(root, text='Ваш курс будет построен на сложном уровне').place(x=60,y=220)





def selected(event):
    # получаем выделенный элемент
    selection = combobox.get()
    label1["text"] = f"Выбран язык: {selection}"

label = Label(root, text="Регистрация", font="times 14 bold", bg='blue', fg='white')
label.place(x=130, y=10)
label2 = Label(root, text="Заполните информацию", font="times 12 bold", bg='red', fg='white')
label2.place(x=100, y=45)
languages = ["Python", "C#", "Java", "JavaScript"]
label1 = ttk.Label()
label1.place(x=50, y=95)



combobox = ttk.Combobox(values=languages, state="readonly")
combobox.place(x=115, y=75)
combobox.bind("<<ComboboxSelected>>", selected)

level_var = IntVar()
label5 = Label(root, text='Уровень сложности', bg='#40B05E', fg='white').place(x=130, y=130)
rb1 = ttk.Radiobutton(root, text = 'EASY',variable=level_var,value=1, command=select_level).place(x=160, y=160)
rb2 = ttk.Radiobutton(root, text = 'MIDDLE',variable=level_var,value=2,command=select_level).place(x=160, y=180)
rb3 = ttk.Radiobutton(root, text = 'HARD',variable=level_var,value=3,command=select_level).place(x=160, y=200)




label3 = Label(root, text='Ведите имя',bg ='#40B05E', fg='white').place(x=155, y=260)
e1 = Entry(root, width=15)
e1.place(x=140, y=290)


b1 = Button(root, text= 'Подтвердить', font='times 10', bg ='green', command = reg)
b1.place(x=145,y=350)




root.mainloop()