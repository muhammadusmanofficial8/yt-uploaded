import turtle
import colorsys
import time
start = time.time()
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")
screen.title("Celestial Neon Spiral")
turtle.colormode(255)
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(99)
pen.width(0)
screen.tracer(99)
total_petals = 100
layers = 30
distance_step = 6
angle_step = 137.5
hue = 0.0
for i in range(total_petals * layers):
    rgb = colorsys.hsv_to_rgb(hue, 1, 1)
    r, g, b = int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255)
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(i * angle_step)
    pen.forward(i * distance_step / layers)
    pen.pendown()
    pen.pencolor(r, g, b)
    pen.fillcolor(r, g, b)
    pen.begin_fill()
    pen.circle(2.8)
    pen.end_fill()
    pen.pensize(0.5)
    pen.pencolor(r//3, g//3, b//3)
    pen.circle(6)
    hue += 0.003
    if hue > 1:
        hue = 0
screen.update()
print(f"Done in {round(time.time() - start, 2)} seconds.")
turtle.done()
