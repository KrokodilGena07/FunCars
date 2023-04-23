from car import Car


class DangerCar(Car):
    def __init__(self, x, y, speed_1, file):
        super(DangerCar, self).__init__(x, y, speed_1, file)
