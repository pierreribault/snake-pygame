import pygame
import random
from src.snake import Snake
from src.apple import Apple
from src.score import Score
from src.apple_slow import SlowApple
from src.apple_fast import FastApple
from src.apple_invinsible import InvinsibleApple

class SnakeGame:
    game_over = False
    exit = False
    width = 800
    height = 600
    tickrate = 17
    score = 0
    last_key_event = ""
    username = ""
    setup = False
    slow = 0
    fast = 0
    invinsible = 0

    colors = {
        "blue": (0, 0, 255),
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "black": (0, 0, 0),
        "white": (255, 255, 255),
    }

    def __init__(self):
        pygame.init()
        self.font25 = pygame.font.SysFont("arial", 25)
        self.font16 = pygame.font.SysFont("arial", 16)
        self.display = self.initDisplay()

        self.snake = Snake(self.width, self.height)
        self.apple = Apple(self.width, self.height, self.snake.pixel)
        self.apple.enable()
        self.apple.generate(self.snake.x, self.snake.y)

        self.slow_apple = SlowApple(self.width, self.height, self.snake.pixel)
        self.fast_apple = FastApple(self.width, self.height, self.snake.pixel)
        self.invinsible_apple = InvinsibleApple(self.width, self.height, self.snake.pixel)

        self.storage = Score()
        self.main()

    def initDisplay(self):
        pygame.display.set_caption('Snake - ESGI')
        self.clock = pygame.time.Clock()

        return pygame.display.set_mode((self.width, self.height))

    def keyEvents(self, event):
        if event.type == pygame.QUIT:
            self.game_over = True
            self.exit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.exit = True
            if event.key == pygame.K_LEFT and self.last_key_event != pygame.K_RIGHT:
                self.snake.setDirection(-self.snake.pixel, 0, 'horizontal')
            if event.key == pygame.K_RIGHT and self.last_key_event != pygame.K_LEFT:
                self.snake.setDirection(self.snake.pixel, 0, 'horizontal')
            if event.key == pygame.K_UP and self.last_key_event != pygame.K_DOWN:
                self.snake.setDirection(0, -self.snake.pixel, 'vertical')
            if event.key == pygame.K_DOWN and self.last_key_event != pygame.K_UP:
                self.snake.setDirection(0, self.snake.pixel, 'vertical')
            self.last_key_event = event.key

    def refresh(self):
        #Override everything to black
        self.display.fill(self.colors["black"])
        self.scoretracker()
        self.statustracker()

        color = None

        #Draw snake body and apples
        if (self.invinsible > 0):
            color = self.invinsible_apple.color
        elif (self.slow > 0 ):
            color = self.slow_apple.color
        elif (self.fast > 0 ):
            color = self.fast_apple.color

        self.snake.render(self.display, color)
        self.apple.render(self.display)
        self.slow_apple.render(self.display)
        self.fast_apple.render(self.display)
        self.invinsible_apple.render(self.display)

        #Update display and clock tickrate
        pygame.display.update()
        self.clock.tick(self.tickrate)

    def scoreboard(self):
        for event in pygame.event.get():
            self.keyEvents(event)

        self.display.fill(self.colors["black"])
        leaderboard = self.storage.read()[:15]
        x = 20
        y = 60

        element = self.font25.render("TABLEAU DES SCORES - TOP 15", True, self.colors["green"])
        self.display.blit(element, [20, 20])

        element = self.font25.render("Appuyer sur Entrer pour quitter le programme", True, self.colors["blue"])
        self.display.blit(element, [20, 550])

        for score in leaderboard:
            text = f'{score.get("username")}: {score.get("score")} points'
            element = self.font16.render(text, True, self.colors["white"])
            self.display.blit(element, [x, y])
            y += 30

        pygame.display.update()
        self.clock.tick(self.tickrate)

    def player(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.setup = True
                self.game_over = True
                self.exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(self.username) > 0:
                    self.setup = True
                elif event.key == pygame.K_BACKSPACE:
                    self.username = self.username[:-1]
                else:
                    self.username += event.unicode

        self.display.fill(self.colors["black"])

        element = self.font25.render("Nom du joueur:", True, self.colors["green"])
        self.display.blit(element, [20, 20])

        element = self.font25.render(self.username, True, self.colors["white"])
        self.display.blit(element, [200, 20])

        element = self.font25.render("Appuyer sur Entrer pour valider", True, self.colors["blue"])
        self.display.blit(element, [20, 550])

        element = self.font25.render("Liste des différents types de Pomme", True, self.colors["white"])
        self.display.blit(element, [20, 150])

        pygame.draw.rect(self.display, self.apple.color, [20, 200, 30, 30])
        element = self.font25.render(f"Normal", True, self.colors["white"])
        self.display.blit(element, [70, 200])

        pygame.draw.rect(self.display, self.slow_apple.color, [20, 250, 30, 30])
        element = self.font25.render(f"Lent - Durée {self.slow_apple.duration}", True, self.colors["white"])
        self.display.blit(element, [70, 250])

        pygame.draw.rect(self.display, self.fast_apple.color, [20, 300, 30, 30])
        element = self.font25.render(f"Rapide - Durée {self.fast_apple.duration}", True, self.colors["white"])
        self.display.blit(element, [70, 300])

        pygame.draw.rect(self.display, self.invinsible_apple.color, [20, 350, 30, 30])
        element = self.font25.render(f"Invinsible - Durée {self.invinsible_apple.duration}", True, self.colors["white"])
        self.display.blit(element, [70, 350])

        pygame.display.update()
        self.clock.tick(self.tickrate)

    def scoretracker(self):
        value = self.font25.render("Score " + str(self.score), True, self.colors["green"])
        self.display.blit(value, [10, 10])

    def statustracker(self):
        if (self.slow > 0):
            value = self.font25.render("Slow " + str(self.slow), True, self.slow_apple.color)
            self.display.blit(value, [10, 50])
            self.slow -= 1
        elif (self.fast > 0):
            value = self.font25.render("Fast " + str(self.fast), True, self.fast_apple.color)
            self.display.blit(value, [10, 50])
            self.fast -= 1
        elif (self.invinsible > 0):
            value = self.font25.render("Invinsible " + str(self.invinsible), True, self.invinsible_apple.color)
            self.display.blit(value, [10, 50])
            self.invinsible -= 1
        else:
            self.slow = self.fast = self.invinsible = 0
            self.tickrate = 17

    def randomApple(self):
        select = random.randint(0, 100)

        if select < 55 or self.slow > 0 or self.fast > 0 or self.invinsible > 0:
            self.apple.enable()
            self.apple.generate(self.snake.x, self.snake.y)
        elif select >= 55 and select < 70:
            self.invinsible_apple.enable()
            self.invinsible_apple.generate(self.snake.x, self.snake.y)
        elif select >= 70 and select < 85:
            self.slow_apple.enable()
            self.slow_apple.generate(self.snake.x, self.snake.y)
        else:
            self.fast_apple.enable()
            self.fast_apple.generate(self.snake.x, self.snake.y)

    def cycle(self) -> None:
        for event in pygame.event.get():
            self.keyEvents(event)

        if self.invinsible == 0 and self.snake.suicide():
            self.game_over = True

        self.snake.move()

        if self.apple.isHere(self.snake.x, self.snake.y):
            self.score += self.apple.score()
            self.apple.disable()
            self.snake.grow()
            self.randomApple()

        if self.slow_apple.isHere(self.snake.x, self.snake.y):
            self.score += self.slow_apple.score()
            self.tickrate, self.slow = self.slow_apple.power()
            self.snake.grow()
            self.slow_apple.disable()
            self.randomApple()

        if self.fast_apple.isHere(self.snake.x, self.snake.y):
            self.score += self.fast_apple.score()
            self.tickrate, self.fast = self.fast_apple.power()
            self.snake.grow()
            self.fast_apple.disable()
            self.randomApple()

        if self.invinsible_apple.isHere(self.snake.x, self.snake.y):
            self.score += self.invinsible_apple.score()
            self.invinsible = self.invinsible_apple.power()
            self.snake.grow()
            self.invinsible_apple.disable()
            self.randomApple()

        self.refresh()

    def main(self):
        while not self.setup:
            self.player()

        while not self.game_over:
            if self.snake.x >= self.width or self.snake.x < 0 or self.snake.y >= self.height or self.snake.y < 0:
                self.game_over = True
            self.cycle()

        self.storage.save(self.storage.add(self.username, self.score))

        while not self.exit:
            self.scoreboard()

        pygame.quit()
        quit()

snake = SnakeGame()
