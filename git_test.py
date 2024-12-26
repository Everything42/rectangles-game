import pygame
from random import randint
from sys import exit

# initialize pygame
pygame.init()
clock = pygame.time.Clock()

# create counter
time_counter = 0
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)

# initialize display
displayX = 1440
displayY = 800
screen = pygame.display.set_mode((displayX, displayY))
pygame.display.set_caption("Rectangle game")


# create class that inherits from Surfaces
class Rectangles(pygame.Surface):
    def __init__(self, X, Y, dimX, dimY, VelX, VelY, color):
        super().__init__((dimX, dimY))
        self.X = X
        self.Y = Y
        self.dimX = dimX
        self.dimY = dimY
        self.VelX = VelX
        self.VelY = VelY
        self.color = color

    def move(self):
        if self.X + self.dimX > displayX: self.VelX = -1 * randint(1, 4)
        if self.Y + self.dimY > displayY: self.VelY = -1 * randint(1, 4)
        if self.X < 0: self.VelX = randint(1, 4)
        if self.Y < 0: self.VelY = randint(1, 4)
        self.X += self.VelX
        self.Y += self.VelY

    def draw(self):
        self.fill(self.color)
        screen.blit(self, (self.X, self.Y))

    def check_collision(self, other):
        rect1 = pygame.Rect(self.X, self.Y, self.dimX, self.dimY)
        rect2 = pygame.Rect(other.X, other.Y, other.dimX, other.dimY)
        return rect1.colliderect(rect2)


# create a list with instances of Rectangles that have random attributes
list_rect = []
for i in range(20):
    list_rect.append(Rectangles(X=randint(0, displayX), Y=randint(0, displayY), dimX=randint(20, 100), dimY=randint(20, 100), VelX=randint(1, 4), VelY=randint(1, 4), color=(randint(0, 255), randint(0, 255), randint(0, 255))))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == timer_event:
            time_counter += 1

    if time_counter < 5:
        screen.fill((0, 0, 0))
        for element in list_rect:
            element.draw()
            element.move()
            for other_element in list_rect:
                if other_element != element and element.check_collision(other_element):
                    if element.X > other_element.X:
                        element.VelX = 1
                        other_element.VelX = -1
                    elif element.X < other_element.X:
                        element.VelX = -1
                        other_element.VelX = 1
                    elif element.Y > other_element.Y:
                        element.VelY = 1
                        other_element.VelY = -1
                    elif element.Y < other_element.Y:
                        element.VelY = -1
                        other_element.VelY = 1

    pygame.display.update()
    clock.tick(60)
