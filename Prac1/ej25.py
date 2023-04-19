from turtle import Screen, Turtle

x = int(input('Radio:'))

pantalla = Screen()
pantalla.setup(x,x)
pantalla.screensize(400,400)
tortuga = Turtle()
tortuga.circle(1)
tortuga.circle(x)

pantalla.exitonclick()
