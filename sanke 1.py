
import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

#vamos a crear una ventana
wn=turtle.Screen()
wn.title("juego snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#aqui creamos un elemento turtle para que se vea algo en pantalla
cabeza=turtle.Turtle
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()#este se utiliza para que el movimiento del objeto no deje un rastro por pantalla
#el .goto es para establecer la posicion dentro del plano 
#con turtle el punto 0,0 esta en el centro
cabeza.goto(0,0)
cabeza.direccion="stop"

comida=turtle.Turtle
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)
#cuerpo
segmentos=[]




#funcion
def arriba():
    cabeza.direction="up"
def abajo():
    cabeza.direction="down"
    
def izquierda():
    cabeza.direction="left"
    
def derecha():
    cabeza.direction="rigth"

def mov():
    if cabeza.direction=="up":
        y=cabeza.ycor()
        cabeza.sety(y+20)
    if cabeza.direction=="down":
        y=cabeza.ycor()
        cabeza.sety(y-20)
    if cabeza.direction=="left":
        y=cabeza.xcor()
        cabeza.setx(y-20)
    if cabeza.direction=="rigth":
        y=cabeza.xcor()
        cabeza.setx(y+20)

#teclado
wn.listen()
wn.onkeypress(arriba,"up")
wn.onkeypress(abajo,"down")
wn.onkeypress(izquierda,"left")
wn.onkeypress(derecha,"rigth")
        


#bucle principal
while True:
    wn.update()
    if cabeza.distance(comida)<20:
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        comida.goto(x,y)
        
        nuevo_segmento=turtle.Turtle
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("green")
        nuevo_segmento.penup()
        nuevo_segmento.goto(0,100)
        segmentos.append(nuevo_segmento)
    totalseg=len(segmentos)
    for index in range (-1,0,-1):
        x=segmentos[index-1].xcor()
        y=segmentos[index-1].ycor()
        segmentos[index].goto(x,y)
        
    if totalseg> 0:
        x=cabeza.xcor
        y=cabeza.ycor
        segmentos[0].goto(x,y)
        
    
    mov()
    time.sleep(delay)

    