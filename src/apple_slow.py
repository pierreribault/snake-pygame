from src.apple import Apple

class SlowApple(Apple):
    color = (52, 235, 232)
    point = 200
    tickrate = 12
    duration = 100

    def power(self) -> tuple:
        return (self.tickrate, self.duration)
