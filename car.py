from tkinter import PhotoImage


class Car:
    def __init__(self, x, y, speed_1, file):
        self.x = x
        self.y = y
        self.speed_1 = speed_1
        self.image_1 = PhotoImage(file=file)
