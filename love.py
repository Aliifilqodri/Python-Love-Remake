import turtle 

turtle.bgcolor("black")
turtle.pensize(3)

a = turtle.Turtle()
a.penup()
a.goto(-250, 60)
a.pendown()
a.color("#FF3E4D")
style = ('Arial', 40, 'italic')
a.write('', font=style, align='left')
a.hideturtle()

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

colors = ['#FF3E4D', '#FFBD2E', '#FF813E', '#3EFF92', '#3E7DFF']

turtle.speed(0)

for i in range(360):
    turtle.pencolor(colors[i % 5])
    turtle.width(i / 100 + 1)
    turtle.forward(i)
    turtle.left(59)

turtle.hideturtle()

a = turtle.Turtle()
a.penup()
a.goto(-40, 75)
a.pendown()
a.color("#FF3E4D")
style = ('Arial', 20, 'italic')
a.write('', font=style, align='left')
a.hideturtle()

a = turtle.Turtle()
a.penup()
a.goto(-2, 75)
a.pendown()
a.color("#FF3E4D")
style = ('Arial', 20, 'italic')
a.write('', font=style, align='left')
a.hideturtle()

a = turtle.Turtle()
a.penup()
a.goto(180, 60)
a.pendown()
a.color("#FF3E4D")
style = ('Arial', 20, 'italic')
a.write('', font=style, align='left')
a.hideturtle()

a = turtle.Turtle()
a.penup()
a.goto(-150, -130)
a.pendown()
a.color("#FF3E4D")
style = ('Arial', 30, 'italic')
a.write('', font=style, align='left')
a.hideturtle()

turtle.done()
