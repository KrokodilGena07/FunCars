from tkinter import PhotoImage


class Pit:
    def __init__(self, x, y, file):
        self.x = x
        self.y = y
        self.image = PhotoImage(file=file)
