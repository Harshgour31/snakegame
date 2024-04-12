import pygame

from pygame .locals import *
 
import time 

import random

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000,800))

        pygame.mixer.init()
        self.snake = Snake(self.surface,2)
        self.snake.draw()
        self.apple = apple(self.surface)
        self.apple.draw()
    def is_collision(self,x1,y1,x2,y2):
        if x1 >= x2 and x1 < x2 + SIZE :
            if y1 >= y2 and y1 < y2 + SIZE:
                return True 
        return False

    def render_background(self):
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0,0))

    def play(self):
        self.render_background()

        self.snake.walk()
        
        self.apple.draw()
        
        self.display_score()
        pygame.display.flip()

        if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            sound = pygame.mixer.Sound("resources/a.mp3")
            pygame.mixer.Sound.play(sound)
            self.snake.increase_lenght()
            self.apple.move()

        for i in range(3,self.snake.length):    
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                exit(0)
    
    def display_score(self):
        font  = pygame.font.SysFont('arial',30)
        score = font.render(f"Score:{self.snake.length}",True,(0,255,255))
        self.surface.blit(score,(800,10))

    def run(self):
        
     running = True
     while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if event.key == K_UP:
                    self.snake.move_up()

                if event.key == K_DOWN:
                    self.snake.move_down()
                   

                if event.key == K_RIGHT:
                    self.snake.move_right()
                    

                if event.key == K_LEFT:
                    self.snake.move_left()
                    


            elif event.type == QUIT:
                running = False
        
        self.play()

        time.sleep(0.2)
  
SIZE = 40



class apple:
    def __init__(self,parent_screen):
        self.parent_screen = parent_screen
        self. image = pygame.image.load("resources/apple.jpg").convert()
        self.x = SIZE*3
        self.y = SIZE*3

    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0,24)*SIZE
        self.y = random.randint(0,19)*SIZE

class Snake:
    def __init__(self,parent_screen,length):
        self.length = length
        self.parent_screen = parent_screen
        self. block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = 'down'
    
    def draw(self):
        for i in range(self.length):
          self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()


    def increase_lenght(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)


    def move_up(self):
        self.direction = 'up'


    def move_down(self):
        self.direction = 'down'


    def move_left(self):
        self.direction = 'left'


    def move_right(self):
        self.direction = 'right'


    def walk(self):


        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'left':
            self.x[0] -= SIZE
        
        elif self.direction == 'right':
            self.x[0] += SIZE
    
        elif self.direction == 'up':
            self.y[0] -= SIZE

        elif self.direction == 'down':
            self.y[0] += SIZE

        self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
    
   