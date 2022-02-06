import random, pygame
from src.apple import Apple

class FastApple(Apple):
    color = (235, 64, 52)
    point = 300
    tickrate = 30
    duration = 300

    def power(self) -> tuple:
        return (self.tickrate, self.duration)
