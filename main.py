import turtle
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

turtle.screensize(1000,1000,bg=None)
turtle.speed(0)
for e in imp:
    turtle.up()
    if e[3] == "y":
        turtle.goto(float(e[1]),float(e[0]))
        turtle.down()
        turtle.goto(float(e[2]),float(e[0]))
    else:
        turtle.goto(float(e[0]),float(e[1]))
        turtle.down()
        turtle.goto(float(e[0]),float(e[2]))
input()
