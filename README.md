# Estructura de un juego en pygame

## inicialización
 - como todo programa en python, se deben importar los modulos o librerias a utilizar 

```import pygame```

- inicializar pygame usando la función init(). inicializa todos los modulos de pygame importados.

```pygame.init```

## visualizacion de la ventana 

```ventana = pygame.display.set_mode((600,400))```

- set_mode es la funcion encargada de definir el tamaño de la ventana. En el ejemplo, se esta definiendo una ventana de 600 px de ancho, 400 px de alto.

`pygame.display.set_caption("mi ventana)`
- set_caption es la funcion que añade  un titulo a la ventana.

### funcion set_mode
`set_mode(size =(o,o), flags = 0, deph = 0,      display = 0)`

- size =(600,400) : define el tamaño de la ventana.

- flags: define uno o mas comportamientos para la ventana.
    - valores
        - pygame.FULLSCREEN
        - pygame.RESIZAVLE
    
    
    - ejemplo
        - flags = pygame.FULLSCREEN | pygame.RESIZABLE: pantalla completa.
        dimensiones modificables.


## bucle del juego - game loop 

- bucle infinito que se interrumpira al cumplir ciertos criterios 

- reloj interno del juego 

- en cada iteracion del bucle del juego podemos mover a un personaje, o tener en cuenta que un objeto a alcanzado a otro o que se cruzo la linea de llegada, lo que quiere decir que la partida termino.

- cada iteracion es una oportunidad para actualizar todsos los datos relacionados con el estado actual de la partida.

- en cada iteracion se realizan las siguientes tareas:
    1. comprbar que no se alcanzan las condiciones de parada, en cuyo caso se interrumpe el bucle.
    
    2. actualizar los recursos necesarios para la interacion actual.
    
    3. obtener las entradas del sistema, o de interaccion con el jugador.
    
    4. actualizar todas las entidades que caracterizan el juego.
    
    5. refrescar la pantalla


## superficies pygame

- superficie: 
    - elemento geometrico.
    - linea, poligono, imagen, texto que se muestra en la pantalla 
    - el poligono se puede o no rellenar de color. 
    - las superficies se crean de diferente manera dependiendo del tipo:
        - imagen: image.load() 
        - texto: font.render()
        - superficie generica: pygame.surface()
        - ventana del juego: pygamen.display.set_mode()


# Ejemplo bandera_colombia
``` # importamos la libreria pygamme
import pygame 

# inicializamos los modulos de pygame
pygame.init()

# establecer titulo a la ventana
pygame.display.set_caption("Nesticor.py")

# establecemos las dimenciones de la ventana 

ventana = pygame.display.set_mode((400,400))


# definnimmos un color 
amarillo = (255, 251, 0)
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
```
![diagrama de flijo](screen.png)
    






