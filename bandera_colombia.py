# importamos la libreria pygamme
import pygame 

# inicializamos los modulos de pygame
pygame.init()

# establecer titulo a la ventana
pygame.display.set_caption("Nesticor.py")

# establecemos las dimenciones de la ventana 

ventana = pygame.display.set_mode((400,400))


# definnimmos un color 
amarillo = (255, 250, 0)
azul = (0, 0, 255)
rojo = (255, 0, 0)

# crear una superficie 
amarillo_Superficie = pygame.Surface((400,200))
azul_Superficie = pygame.Surface((400,100))
rojo_Superfice = pygame.Surface((400,100))

# rellenamos la superficie de azul
amarillo_Superficie.fill(amarillo)
azul_Superficie.fill(azul)
rojo_Superfice.fill(rojo)



# inserto o muevo  la superficie de la ventana 
ventana.blit(amarillo_Superficie, (0,0))
ventana.blit(azul_Superficie, (0,200))
ventana.blit(rojo_Superfice, (0,300))


# actualiza la visualizacion de la ventana
pygame.display.flip()

# bucle del juego 
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()
