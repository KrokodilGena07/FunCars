from tkinter import PhotoImage
from car import Car


class UserCar(Car):
    def __init__(self, x, y, speed_1, file):
        super(UserCar, self).__init__(x, y, speed_1, file)
        self.speed_2 = 0
        self.image_2 = PhotoImage(file='images/car_2.png')
        self.image_3 = PhotoImage(file='images/car_3.png')
        self.image_4 = PhotoImage(file='images/car_4.png')

    def move_up(self, event):
        self.speed_1 = -2.5

    def move_right(self, event):
        self.speed_2 = 2.5

    def move_left(self, event):
        self.speed_2 = -2.5

    def stop_move(self, event):
        self.speed_1 = 0
        self.speed_2 = 0

    def is_crash(self, game_obj):
        return ((self.x - game_obj.x) ** 2 + (self.y - game_obj.y)
                ** 2) ** 0.5 <= ((15 + 15) ** 2 + (23 + 23) ** 2) ** 0.5
