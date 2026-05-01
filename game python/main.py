import pygame


#layar
height = 1366
width = 768
screen = pygame.display.set_mode([height,width])

#warna layar
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

#logo

#gambar
image = pygame.image.load("startup.png")
screen.blit(image,(100,100))

pygame.quit
