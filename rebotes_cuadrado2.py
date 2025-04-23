import pygame 
import sys
import random 


      

rojo = (255,0,0)
azul = (0,0,255)
amarillo = (255,250,0)
rosado = (226,51,255)
verde = (205,255,51)

pygame.init()
 
ventana = pygame.display.set_mode ((500,500))

pygame.display.set_caption("El cuadrado que rebota")

Clock = pygame.time.Clock()

XX = 366
MOVIMIENTO = 3

while 1:
    Clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    ventana.fill(azul)
    XX = XX + MOVIMIENTO

    if XX >= 450:
        XX = 450
        MOVIMIENTO = -3
    elif XX <= 0:
        XX = 0
        MOVIMIENTO = 3

    pygame.draw.rect(ventana, rojo, (XX, 00, 50, 50))
    pygame.display.flip()

    pygame.draw.rect(ventana, amarillo, (XX, 450, 50, 50))
    pygame.display.flip()

    pygame.draw.rect(ventana, rosado, (450, XX, 50, 50))
    pygame.display.flip()

    pygame.draw.rect(ventana, verde, (0, XX, 50, 50))
    pygame.display.flip()

    rojo1 = random.randint(0,255) 
    azul1= random.randint(0,255) 
    verde1 = random.randint(0,255)
    color_random = (rojo1, azul1, verde1)

    pygame.draw.rect(ventana, color_random, (200, 200, 100, 100))
    pygame.display.flip()

    

        
    
    
        




    

    






