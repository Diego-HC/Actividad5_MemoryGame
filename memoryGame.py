from random import *
from turtle import *
from random import randint

from freegames import path

car = path('car.gif')
t = randint(1, 4)
click = 1
nclicks = []
writer = Turtle(visible=False)
states = {'contador': 0}

if t == 1:
    tiles = list(range(32)) * 2
elif t == 2:
    tiles = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F'] * 2
elif t == 3:
    tiles = ['!', '!!', '!!!', '!!!!', '#', '##', '###', '####', '$', '$$', '$$$', '$$$$', '%', '%%', '%%%', '%%%%',
             '&', '&&', '&&&', '&&&&', '?', '??', '???', '????', '+', '++', '+++', '++++', '-', '--', '---', '----'] * 2
elif t == 4:
    tiles = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI',
             'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX',
             'XXX', 'XXXI', 'XXXII'] * 2
state = {'mark': None}
hide = [True] * 64


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    forward(25) #Hacer que el cuadrado se empiece a dibujar desde el centro inferior
    for count in range(3):
        left(90)
        forward(50)
    left(90)
    forward(25)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 175, (count // 8) * 50 - 200 #La loseta se traslada 25 a la izquierda


    
def tap(x, y):
    
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    
    
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        
    if state['mark'] == spot or state['mark'] == None:
        
        
        nclicks.append(click)
        
        contador = len(nclicks)
    
        
        print(contador)
        
        
        writer.write(contador)
        
       
        

#def contador(): 
    
    
    #for tap in car:
        #clic = 1
        #con = clic
        #print(con)

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        if t == 1 or t == 2:
            write(tiles[mark], font=('Arial', 30, 'normal'), align="center") #Texto alineado en el centro
        elif t == 3:
            write(tiles[mark], font=('Arial', 15, 'normal'), align="center") #Texto alineado en el centro
        else:
            write(tiles[mark], font=('Arial', 13, 'normal'), align="center") #Texto alineado en el centro

    # Desplegar un texto cuando el jugador gane
    for i in hide:  # Checa la lista que lleva el recuento de las casillas descubiertas
        if i:
            break   # Si falta alguna de ser descubierta, sale del loop
    else:   # Si ya se descubrieron todas
        up()
        x, y = xy(66)   #Ir a una posición específica
        goto(x, y)
        down()
        color('black', 'white')
        begin_fill()
        for _ in range(2):  # Dibujar un rectángulo sobre la imagen del auto
            forward(200)
            right(90)
            forward(100)
            right(90)
        end_fill()
        up()
        x, y = xy(52)
        goto(x, y + 20)
        write('Ganaste', align='center', font=('Arial', 40, 'normal'))   # Escribir el texto dentro del cuadro

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
