from tkinter import *

class SuperCanvas(Canvas):

    def __init__(self, master, width, height, bd, highlightthickness, relief):

        self.ctx = Canvas(width=width, height=height, bd=bd, highlightthickness=highlightthickness, relief=relief)
        self.width = width
        self.height = height
