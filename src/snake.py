import pygame

class Snake:
    color = (0, 255, 0)
    body = []
    direction = {'movement': '', 'position': (0, 0)}
    lenght = 1
    pixel = 20

    def __init__(self, width: int, height: int) -> None:
        self.x = round(width / 2)
        self.y = round(height / 2)

    def move(self) -> None:
        (self.x, self.y) = self.getNextPosition()
        self.body.append([self.x, self.y])

        if len(self.body) > self.lenght:
            self.body.pop(0)

    def setDirection(self, x: int, y: int, movement: str) -> None:
        if self.direction['movement'] != movement:
            self.direction['position'] = (x, y)
            self.direction['movement'] = movement

    def getNextPosition(self) -> tuple:
        x = self.x + self.direction['position'][0]
        y = self.y + self.direction['position'][1]

        return (x, y)

    def grow(self) -> None:
        self.lenght += 1

    def suicide(self) -> bool:
        return True if list(self.getNextPosition()) in self.body[:-1] else False

    def render(self, display: pygame.Surface, color = None) -> None:
        if (color == None):
            color = self.color

        for body in self.body:
            pygame.draw.rect(display, color, [body[0], body[1], self.pixel, self.pixel])
