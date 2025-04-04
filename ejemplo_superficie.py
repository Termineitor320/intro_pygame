# importamos la libreria pygamme
import pygame 
import random  

# inicializamos los modulos de pygame
pygame.init()

# establecer titulo a la ventana
pygame.display.set_caption("Surface")

# establecemos las dimenciones de la ventana 

ventana = pygame.display.set_mode((400,400))

# definnimmos un color 
azul = (51, 246, 255)

# crear una superficie 
azul_Superficie = pygame.Surface((300,300))

# rellenamos la superficie de azul
azul_Superficie.fill(azul)

# inserto o muevo  la superficie de la ventana 
ventana.blit(azul_Superficie, (0,0))

# actualiza la visualizacion de la ventana
pygame.display.flip()

# bucle del juego 
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()






