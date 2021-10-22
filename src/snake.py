import pygame

class Snake:
  color = (0, 255, 0)
  body = []
  direction = (0, 0)
  lenght = 1
  pixel = 10

  def __init__(self, width: int, height: int) -> None:
    self.x = round(width / 2)
    self.y = round(height / 2)

  def move(self) -> None:
    self.x += self.direction[0]
    self.y += self.direction[1]
    self.body.append([self.x, self.y])

    if len(self.body) > self.lenght:
      self.body.pop(0)
  
  def grow(self) -> None:
    self.lenght += 1

  def render(self, display: pygame.Surface) -> None:
    for body in self.body:
      pygame.draw.rect(display, self.color, [body[0], body[1], self.pixel, self.pixel])