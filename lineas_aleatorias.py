import pygame
import sys
import random
import math

verde = (0, 255, 85)
amarillo = (255,250,0)
rosado = (226,51,255)
gris = (133,133,133)
negro = (0, 0, 0 )
rojo = (255,0,0)
azul = (0,0,255)
blanco = (255,255,255)
naranja = (255, 165, 0)
cian = (0, 255, 255)
zafiro = (15,82,186)
indianRed =(205, 92, 92)
LightCoral= (240, 128, 128)
Clock = pygame.time.Clock()

pygame.init()
 
ventana = pygame.display.set_mode ((500,500))

pygame.display.set_caption("lineas aleatorias")

ventana.fill(negro)

while 1:
    Clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("sistemas guanenta",1,blanco)
    ventana.blit(texto,(100,0))
    pygame.display.flip()

    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("DANIEL DIAZ",1,blanco)
    ventana.blit(texto,(145,472))
    pygame.display.flip()

    pygame.draw.rect(ventana, amarillo, ((50, 100), (400, 300)), 1)
    puntos2 = [(200,0), (400,200), (200,400), (0,200)]
    
    for i in range(100):
        verde1 = random.randint(0,255,)
        amarillo1 = random.randint(0,255)
        rosado1 = random.randint(0,255)
        negro1 = random.randint(0,255)
        rojo1 =  random.randint(0,255)
        azul1 = random.randint(0,255)
        blanco1 = random.randint(0,255)
        naranja1 = random.randint(0,255)
        cian1 = random.randint(0,255)
        zafiro1 = random.randint(0,255)
        indianRed1 =random.randint(0,255)
        LightCoral1= random.randint(0,255)
        color_random = (verde1, amarillo1, rosado1, negro1, rojo1, azul1, blanco1, naranja1, cian1, zafiro1,indianRed1,LightCoral1)
    
        y1 = random.randint(50,450)
        y2 = random.randint(100,450)
        y3 = random.randint(100,450)
        y4 = random.randint(100,450)


        pygame.draw.line(ventana, color_random,(y1,y2),(y3, y4))

        pygame.display.flip()


    

    
