import random, pygame

class Apple:
  color = (255, 0 ,0)

  def __init__(self, width: int, height: int, pixel: int) -> None:
    self.width = width
    self.height = height
    self.pixel = pixel

  def generate(self, x: int, y: int) -> None:
    self.x = round(random.randint(0, self.width - self.pixel) / self.pixel) * self.pixel
    self.y = round(random.randint(0, self.height - self.pixel) / self.pixel) * self.pixel

    print(self.x, self.y)
    if (self.x == x and self.y == y):
      self.generate(x, y)
  
  def isHere(self, x: float, y: float) -> bool:
    return x == self.x and y ==self.y

  def render(self, display: pygame.Surface) -> None:
    pygame.draw.rect(display, self.color, [self.x, self.y, self.pixel, self.pixel])
