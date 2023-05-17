import turtle
from random import randint
imp = []

# use any image to desmos program which returns output in the form of an equation like (x or y) = value\left\{value\le y \value\right\}, run the program then paste it in
# https://jinay.dev/pic2graph/ is a good open source one

while True:
    inp = input()
    if inp != "done":
        te = []
        temp = ""
        for e in inp:
            if e.isdigit() or e == "." or e == "-":
                temp += e
            else:
                te.append(temp) if temp != '' else None
                temp = ""
        te.append(inp[0])
        imp.append(te)
    else:
        te = []
        break
turtle.colormode(255)
turtle.screensize(400,400,bg=None)
turtle.speed(0)
turtle.tracer(0,0)
for e in range(0,len(imp)-1,1):
    turtle.up()
    #uncomment this for rainbow colour
    #turtle.pencolor(int(randint(0, 255)),int(randint(0, 255)),int(randint(0, 255)))
    turtle.pencolor("orange")
    if e == len(imp)-1:
        break
    if imp[e][3] == "y":
        turtle.up()
        turtle.goto(float(imp[e][1]),float(imp[e][0]))
        turtle.down()
        turtle.goto(float(imp[e][2]),float(imp[e][0]))
        turtle.up()
    else:
        turtle.up()
        turtle.goto(float(imp[e][0]),float(imp[e][1]))
        turtle.down()
        turtle.goto(float(imp[e][0]),float(imp[e][2]))
        turtle.up()
    if randint(0,3) == 1:
        turtle.update() # make go fast by commenting this and the one above
turtle.update() 
turtle.hideturtle()
turtle.delay(999999999)
input()
