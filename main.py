import pygame as pg
from figura_class import Rectangulo

#inicializar todos los modulos de pygame: pantallas, objetos, sonidos, teclados, etc.
pg.init()

#crear la pantalla o surface
pantalla = pg.display.set_mode( (800, 600) ) #definicion de tamaño de pantalla
pg.display.set_caption( "Bolillas" ) #agregar un titulo a mi ventana

game_over = False

rectangulo1 = Rectangulo(400, 300) #rect blanco
rectangulo2 = Rectangulo(300, 200, (192, 6, 211), 30, 30) #rect violeta
rectangulo1.velocidad(1, 1)
rectangulo2.velocidad(2, 2)

'''
x = 0
vx = 1
y = 300
vy = 1

x2 = 80
vx2 = 1
y2 = 30
vy2 = 1
'''
while not game_over:

    for eventos in pg.event.get(): #capturar todos los eventos mientras el bucle se ejecute
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = True
    
    pantalla.fill((33, 14, 119))#asignar un color a la pantalla

    rectangulo1.mover(800, 600)
    rectangulo2.mover(800, 600)
    '''
    y += vy
    x += vx
    if x >= 800 or x == 0: #los limites en X
        vx *= -1
    if y >= 600 or y == 0: #los limites de y
        vy *= -1

    y2 += vy2
    x2 += vx2
    if x2 >= 800 or x2 == 0: #los limites en X
        vx2 *= -1
    if y2 >= 600 or y2 == 0: #los limites de y
        vy2 *= -1
    '''
  
    #la pantalla o surface, color en tupla de rgb, posiciones(posicionAncho,posicionLargo,tamaño del rec. largo, tamaño del rec. ancho)
    pg.draw.rect(pantalla, rectangulo1.color, (rectangulo1.pos_x, rectangulo1.pos_y, rectangulo1.w, rectangulo1.h))#dibujar un rectangulo 
    pg.draw.rect(pantalla, rectangulo2.color, (rectangulo2.pos_x, rectangulo2.pos_y, rectangulo2.w, rectangulo2.h))#dibujar un rectangulo 



    pg.display.flip()#funcion para cargar toda la configuracion que va dentro de la pantalla

pg.quit()

