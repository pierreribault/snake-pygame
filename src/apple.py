import random, pygame

class Apple:
    color = (205, 235, 52)
    point = 100
    active = False

    def __init__(self, width: int, height: int, pixel: int) -> None:
        self.width = width
        self.height = height
        self.pixel = pixel

    def generate(self, x: int, y: int) -> None:
        if self.active:
            self.x = round(random.randint(0, self.width - self.pixel) / self.pixel) * self.pixel
            self.y = round(random.randint(0, self.height - self.pixel) / self.pixel) * self.pixel

            if (self.x == x and self.y == y):
                self.generate(x, y)

    def isHere(self, x: float, y: float) -> bool:
        if self.active:
            return x == self.x and y ==self.y
        return False

    def score(self) -> int:
        return self.point

    def enable(self) -> None:
        self.active = True

    def disable(self) -> None:
        self.active = False

    def render(self, display: pygame.Surface) -> None:
        if self.active:
            pygame.draw.rect(display, self.color, [self.x, self.y, self.pixel, self.pixel])
