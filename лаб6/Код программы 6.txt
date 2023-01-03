import random
import time
import tkinter as tk

def close():
    global running
    running = False

WINH = 700
WINW = 1200

x = WINW/2
y = WINH/2
r = 20
speed_x = 1
colors = ['red', 'blue', 'green', 'yellow']


win = tk.Tk()
win.title("Animation")
win.config(width=WINW, height=WINH)
win.resizable(False, False)
win.protocol("WM_DELETE_WINDOW", close)

canvas = tk.Canvas(win, bg='#036', highlightthickness=0)
canvas.place(x=0, y=0, width = WINW, heigh = WINH)


def create_objects(N):
    object_list = []
    for i in range (N):
        x=random.randint(100, WINW - 100)
        y = random.randint(100, WINH - 100)
        r = random.randint(10,50)
        speed_x = random.randint(0, 4) - 2
        speed_y = random.randint(0, 4) - 2
        color1 = random.choice(colors)
        color2 = random.choice(colors)
        simple_object = canvas.create_oval(x-r, y-r, x+r, y+r, fill=color1, outline=color2, width=3)

        config = {'obj': simple_object,
                  'speed_x': speed_x,
                  'speed_y': speed_y}


        object_list.append(config)
    return object_list


objects = create_objects(100)

running = True
while running:
    for config in objects:
        canvas.move(config['obj'], config['speed_x'], config['speed_y'])


        coords = canvas.coords(config['obj'])
        if coords[0]<0 or coords[2] > WINW:
            config['speed_x'] =-config['speed_x']
        if coords[1] < 0 or coords[3] > WINH:
            config['speed_y'] = -config['speed_y']


    win.update()
    time.sleep(0.01)

win.destroy()



