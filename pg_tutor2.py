import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Tutorial 2")

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()

game_over = False

# load and convert the image
x_img = pygame.image.load("x.png").convert()

# display the sprite
def sprite(x, y):
    gameDisplay.blit(x_img, (x, y))

x = (display_width * 0.45)
y = (display_height * 0.8)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    gameDisplay.fill(WHITE)
    sprite(x, y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()