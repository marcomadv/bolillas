import pygame as pg
from figura_class import Rectangulo, Bolillas

#inicializar todos los modulos de pygame: pantallas, objetos, sonidos, teclados, etc.
pg.init()

#crear la pantalla o surface
pantalla = pg.display.set_mode( (800, 600) ) #definicion de tamaño de pantalla
pg.display.set_caption( "Bolillas" ) #agregar un titulo a mi ventana

game_over = False

#rectangulo1 = Rectangulo(400, 300) #rect blanco
#rectangulo2 = Rectangulo(300, 200, (192, 6, 211), 30, 30) #rect violeta

circulo1 = Bolillas(400, 300)
circulo2 = Bolillas(300, 200, (192, 6, 211), radio = 30)

while not game_over:

    for eventos in pg.event.get(): #capturar todos los eventos mientras el bucle se ejecute
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = True
    
    pantalla.fill((33, 14, 119))#asignar un color a la pantalla

    #rectangulo1.mover(800, 600)
    #rectangulo2.mover(800, 600)
    circulo1.mover(800, 600)
    circulo2.mover(800, 600)

    #la pantalla o surface, color en tupla de rgb, posiciones(posicionAncho,posicionLargo,tamaño del rec. largo, tamaño del rec. ancho)
    #pg.draw.rect(pantalla, rectangulo1.color, (rectangulo1.pos_x, rectangulo1.pos_y, rectangulo1.w, rectangulo1.h))#dibujar un rectangulo 
    #pg.draw.rect(pantalla, rectangulo2.color, (rectangulo2.pos_x, rectangulo2.pos_y, rectangulo2.w, rectangulo2.h))#dibujar un rectangulo 
    pg.draw.circle(pantalla,circulo1.color, (circulo1.pos_x, circulo1.pos_y), circulo1.radio)
    pg.draw.circle(pantalla,circulo2.color, (circulo2.pos_x, circulo2.pos_y), circulo2.radio)
    
    pg.display.flip()#funcion para cargar toda la configuracion que va dentro de la pantalla

pg.quit()

