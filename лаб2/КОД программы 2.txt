from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("400x400+500+100")
window.title('LAB2')
window.config(background='#B4E67B')
def calculate():
    window1 = Tk()
    window1.geometry("200x80+600+400")
    window1.title('PAYMENT')
    N = e1.get()
    B = e2.get()
    D = e3.get()
    S = e4.get()

    total = (int(N)*5)+(int(B)*12)+(int(D)*3)+(int(S)*1)
    label10=Label(window1,text = 'FOR PAYMENT',font="times 10 bold",bg='blue',fg='white')
    label10.place(x=60,y=2)
    label11 = Label(window1, text=total, font="times 20 bold", fg='green')
    label11.place(x=90, y=45)
    label11 = Label(window1, text='$', font="times 20 bold", fg='green')
    label11.place(x=140, y=45)




#-----------MENU---------------

label1 = Label(window, text='MENU', font="times 28 bold", bg="red", fg='white')
label1.place(x=150, y=15)

label2 = Label(window, text='nuggets     5$', font="times 14 ", bg="#69AB1E", fg='white')
label2.place(x=250, y=100)

label3 = Label(window, text='burger     12$', font="times 14 ", bg="#69AB1E", fg='white')
label3.place(x=250, y=130)

label4 = Label(window, text='drink 0.5 ml   3$', font="times 14 ", bg="#69AB1E", fg='white')
label4.place(x=250, y=160)

label4 = Label(window, text='sauce     1$', font="times 14 ", bg="#69AB1E", fg='white')
label4.place(x=250, y=190)

lable5 = Label(window, text = 'SELECT YOUR ITEMS', font='times 10',bg ='yellow')
lable5.place(x=70, y=100)

label6 = Label(window, text='NUGGETS',bg ='#40B05E', fg='white').place(x=10, y=130)
e1 = Entry(window,width=8)
e1.place(x=70, y=130)

label7 = Label(window, text='BURGER',bg ='#40B05E', fg='white').place(x=10, y=160)
e2 = Entry(window,width=8)
e2.place(x=70, y=160)

label8 = Label(window, text='DRINK',bg ='#40B05E', fg='white').place(x=10, y=190)
e3 = Entry(window,width=8)
e3.place(x=70, y=190)

label9 = Label(window, text='SAUCE',bg ='#40B05E', fg='white').place(x=10, y=220)
e4 = Entry(window,width=8)
e4.place(x=70, y=220)

b1 = Button(window, text= 'PAYMENT',font='times 10',bg ='green',command = calculate)
b1.place(x=175,y=350)





window.mainloop()

