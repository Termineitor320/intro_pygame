import pygame 
import sys
import math
 
verde = (0, 255, 85)
amarillo = (255,250,0)
rosado = (226,51,255)
negro = (0, 0, 0 )
rojo = (255,0,0)
azul = (0,0,255)
blanco = (255,255,255)
naranja = (255, 165, 0)
cian = (0, 255, 255)
zafiro = (15,82,186)
indianRed =(205, 92, 92)
LightCoral= (240, 128, 128)
PI = math.pi 

pygame.init()
 
ventana = pygame.display.set_mode ((400,400))

pygame.display.set_caption("dibujar formas con pygame")

Clock = pygame.time.Clock()

XX = 366
MOVIMIENTO = 3

###########################
# Bucle principal del juego 
###########################

# ciclo para la deteccion de los eventos del juego 
while 1:
    Clock.tick(58)

    for event in pygame.event.get():
        # si se hace click sobre boton de cerrar de la ventana, el juego termina
        if event.type == pygame.QUIT:
            sys.exit()
    
    # rellenar la ventana de color
    ventana.fill(negro)

    # dibujar una linea 
    pygame.draw.line(ventana, rosado, (100,100), (300,300))
    pygame.draw.line(ventana, rosado, (100,300), (300,100))

    # dibujar una linea discontinua 
    # True: crea un poligono 
    puntos1 = [(0,0), (50,100), (100,50), (250,200), (400,400) ]
    puntos2 = [(200,0), (400,200), (200,400), (0,200)]
    pygame.draw.lines(ventana, rosado,True, puntos1 )
    pygame.draw.lines(ventana, rosado, True, puntos2)

    # dibujar un rectangulo 
    # rectangulo relleno, ubicado en la coordenada (200,200) y de ancho 200 y altura 100
    pygame.draw.rect(ventana, verde, (200,200, 200, 100))
    
    # rectangulo sin relleno, esquina sup, izq: (100,100), esquina, inf, der: (150, 200), y de grosor 1
    pygame.draw.rect(ventana, amarillo, ((100, 100), (150, 200)), 1)

    # dibujar un poligono 
    puntos3 = [(200,200),(250,300), (380,325), (400,350)]
    pygame.draw.polygon(ventana, rojo, puntos3)

    #dibujar un circulo
    # centro del circulo: (300,100)
    # radio del circulo: (100)
    # grosor contorno del circulo: 1
    pygame.draw.circle(ventana, blanco, (300,100 ),100,1 )

    # dibujar una elipse 
    pygame.draw.ellipse(ventana, naranja, (100, 150, 200, 100), 1)

    # arco de circunferencia 
    pygame.draw.arc(ventana, cian, (300, 25, 180, 150 ), PI/2, PI, 1)
    
    # texto
    #fuente de tipo arial, tamaño 35, negrrilla y cursiva
    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("sistemas guanenta",1,blanco)

    # actualiza la visualizacion de la ventana 
    pygame.display.flip()