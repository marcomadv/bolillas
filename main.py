import pygame as pg
from figura_class import Figura
import random 


#inicializar todos los modulos de pygame: pantallas, objetos, sonidos, teclados, etc.
pg.init()

#crear la pantalla o surface
pantalla = pg.display.set_mode( (800, 600) ) #definicion de tamaño de pantalla
pg.display.set_caption( "Bolillas" ) #agregar un titulo a mi ventana

game_over = False

listaBolillas = []

for i in range(1, 101):
    listaBolillas.append(Figura(random.randint(0, 750), random.randint(0, 550), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), radio = random.randint(10, 40)))

while not game_over:

    for eventos in pg.event.get(): #capturar todos los eventos mientras el bucle se ejecute
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = True
    
    pantalla.fill((33, 14, 119))#asignar un color a la pantalla

    for bolillas in listaBolillas:
        bolillas.moverCirculo(800, 600)
    
    #la pantalla o surface, color en tupla de rgb, posiciones(posicionAncho,posicionLargo,tamaño del rec. largo, tamaño del rec. ancho)
   
    #pg.draw.circle(pantalla,circulo1.color, (circulo1.pos_x, circulo1.pos_y), circulo1.radio)
    #pg.draw.circle(pantalla,circulo2.color, (circulo2.pos_x, circulo2.pos_y), circulo2.radio)
   
        bolillas.dibujarCirculo(pantalla)

    pg.display.flip()#funcion para cargar toda la configuracion que va dentro de la pantalla
    
pg.quit()

