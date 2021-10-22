import sys, pygame, random
from src.snake import Snake
from src.apple import Apple

class SnakeGame:
  game_over = False
  width = 800
  height = 600
  tickrate = 20

  colors = {
    "blue": (0,0,255),
    "red": (255,0,0),
    "green": (0, 255, 0),
    "black": (0,0,0)
  }
  
  def __init__(self):
    pygame.init()
    self.display = self.initDisplay()
    self.snake = Snake(self.width, self.height)
    self.apple = Apple(self.width, self.height, self.snake.pixel)
    self.apple.generate(self.snake.x, self.snake.y)
    self.main()

  def initDisplay(self):
    pygame.display.set_caption('Snake - ESGI')
    self.clock = pygame.time.Clock()
    
    return pygame.display.set_mode((self.width, self.height))

  def keyEvents(self, event):
    if event.type == pygame.QUIT:
          self.game_over = True

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT: 
        self.snake.direction = (-self.snake.pixel, 0)
      if event.key == pygame.K_RIGHT: 
        self.snake.direction = (self.snake.pixel, 0)
      if event.key == pygame.K_UP: 
        self.snake.direction = (0, -self.snake.pixel)
      if event.key == pygame.K_DOWN:
        self.snake.direction = (0, self.snake.pixel)

  def refresh(self):
    #Override everything to black
    self.display.fill(self.colors["black"])

    #Draw snake body and apple
    self.snake.render(self.display)
    self.apple.render(self.display)
    
    #Update display and clock tickrate
    pygame.display.update()
    self.clock.tick(self.tickrate)

  def cycle(self) -> None:
    for event in pygame.event.get():
      self.keyEvents(event)
      
    self.snake.move()

    if self.apple.isHere(self.snake.x, self.snake.y):
      self.snake.grow()
      self.apple.generate(self.snake.x, self.snake.y)

    self.refresh()    

  def main(self):
    while not self.game_over:
      if self.snake.x >= self.width or self.snake.x < 0 or self.snake.y >= self.height or self.snake.y < 0:
        self.game_over = True
      self.cycle()
      
    pygame.quit()
    quit()

snake = SnakeGame()