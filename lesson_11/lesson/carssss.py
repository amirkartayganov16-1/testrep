import lesssson2

class Car(lesssson2.Transport):

    def __init__(self, title, model, color, speed):
        super().__init__(title, model, color)
        self.speed = speed


class Airplane(lesssson2.Transport):

    def __init__(self, title, model, color, speed):
        super().__init__(title, model, color)
        self.speed = speed