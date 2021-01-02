#custom modules
from classes.SuperCanvas import *
import modules.super_math as SuperMath

#official modules
from tkinter import *
from random import randint
import math

MAX_STEPS = 5
STEP = 0

START_LENGTH = 1500

screen_width, screen_height = SuperMath.get_window_size()

master = Tk()
master.geometry("{}x{}+{}+0".format(int(screen_width), screen_height, 0))
master.configure(bg='#000')

cvs = SuperCanvas(master, width=screen_width, height=(screen_height - 65), bd=0, highlightthickness=0, relief='ridge')
cvs.ctx.configure(bg="#000")
cvs.ctx.pack()

def main():


    cvs.ctx.create_line((cvs.width - START_LENGTH) / 2, cvs.height / 2 + 200,  cvs.width - (cvs.width - START_LENGTH) / 2, cvs.height / 2 + 200, fill="#fff", width=0.5)

    request_animaion_frame()

    master.mainloop()

def request_animaion_frame():

    global STEP
    # cvs.ctx.delete("all")

    objects = list(cvs.ctx.find_all())

    for i in objects:
        x1, y1, x2, y2 = cvs.ctx.coords(i)
        length = SuperMath.get_distance(x1, y1, x2, y2)
        angle = SuperMath.get_angle(x1, y1, x2, y2)

        # print("[{}]: x1 : {}, y1 : {}, x2 : {}, y2 : {}".format(i, x1, y1, x2, y2))
        # print("[{}]: angle : {}".format(i, math.degrees(angle)))
        # print("[{}]: angle : {}".format(i, angle))

        cvs.ctx.delete(i)

        x2, y2 = SuperMath.get_polar_coord(x1, y1, length / 3, angle)
        cvs.ctx.create_line(x1, y1, x2, y2, fill="#fff", width= 0.5)

        x1 = x2
        y1 = y2

        x2, y2 = SuperMath.get_polar_coord(x1, y1, length / 3, angle + 1/3 * math.pi)
        cvs.ctx.create_line(x1, y1, x2, y2, fill="#fff", width= 0.5)

        x1 = x2
        y1 = y2

        x2, y2 = SuperMath.get_polar_coord(x1, y1, length / 3, math.radians(300) + angle)
        cvs.ctx.create_line(x1, y1, x2, y2, fill="#fff", width= 0.5)

        x1 = x2
        y1 = y2

        x2, y2 = SuperMath.get_polar_coord(x1, y1, length / 3, angle)
        cvs.ctx.create_line(x1, y1, x2, y2, fill="#fff", width= 0.5)


    cvs.ctx.update()

    if STEP < MAX_STEPS:
        cvs.ctx.after(1000, request_animaion_frame)
        STEP += 1


if __name__ == "__main__":
    main()
