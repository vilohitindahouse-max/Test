import pygame
import random

width = 500
height = 400
speed = 5
font_size = 72

pygame.init()

background_image = pygame.transform.scale(
    pygame.image.load("background.png"), (width, height)
)

font = pygame.font.SysFont("Times New Roman", font_size)


class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()  
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color("Orange"))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def move(self, xchange, ychange):
        self.rect.x = max(0, min(self.rect.x + xchange, width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y + ychange, height - self.rect.height))


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sprite Collision")

# Sprite group
All_Sprites = pygame.sprite.Group()

sprite1 = Sprite(pygame.Color("black"), 20, 30)
sprite1.rect.x = random.randint(0, width - sprite1.rect.width)
sprite1.rect.y = random.randint(0, height - sprite1.rect.height)
All_Sprites.add(sprite1)

sprite2 = Sprite(pygame.Color("brown"), 20, 30)
sprite2.rect.x = random.randint(0, width - sprite2.rect.width)
sprite2.rect.y = random.randint(0, height - sprite2.rect.height)
All_Sprites.add(sprite2)

running = True
win = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

    if not win:
        keys = pygame.key.get_pressed()
        xchange = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed
        ychange = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speed
        sprite1.move(xchange, ychange)

        if sprite1.rect.colliderect(sprite2.rect):
            All_Sprites.remove(sprite2)
            win = True

    screen.blit(background_image, (0, 0))
    All_Sprites.draw(screen)

    if win:
        win_text = font.render("You Win!", True, pygame.Color("black"))  
        screen.blit(
            win_text,
            ((width - win_text.get_width()) // 2, (height - win_text.get_height()) // 2),
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
