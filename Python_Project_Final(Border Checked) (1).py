import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Borders
turtle.pensize(15)
turtle.penup()
turtle.goto(-400, 0)
turtle.pendown()
turtle.color("#BDC1C6")
turtle.left(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(793)
turtle.right(90)
turtle.forward(593)
turtle.right(90)
turtle.forward(793)
turtle.right(90)
turtle.forward(293)
turtle.penup()

# Score
score_1 = 0
score_2 = 0

# Paddle A
bat_1 = turtle.Turtle()
bat_1.speed(0)
bat_1.shape("square")
bat_1.color("#636363")
bat_1.shapesize(stretch_wid=7, stretch_len=1)
bat_1.penup()
bat_1.goto(-350, 0)

# Paddle B
bat_2 = turtle.Turtle()
bat_2.speed(0)
bat_2.shape("square")
bat_2.color("#636363")
bat_2.shapesize(stretch_wid=7, stretch_len=1)
bat_2.penup()
bat_2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#ffcb3e")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

# Pen
text = turtle.Turtle()
text.speed(0)
text.shape("square")
text.color("#B40014")
text.penup()
text.hideturtle()
text.goto(0, 260)
text.write("Player  A  :  0               Player  B  :  0", align="center", font=("ARCADECLASSIC", 24, "normal"))

# Functions
def bat_1_up():
    y = bat_1.ycor()
    y += 50
    bat_1.sety(y)

    if bat_1.ycor() > 250:
        bat_1.sety(250)


def bat_1_down():
    y = bat_1.ycor()
    y -= 50
    bat_1.sety(y)

    if bat_1.ycor() < -250:
        bat_1.sety(-250)

def bat_2_up():
    y = bat_2.ycor()
    y += 50
    bat_2.sety(y)

    if bat_2.ycor() > 250:
        bat_2.sety(250)

def bat_2_down():
    y = bat_2.ycor()
    y -= 50
    bat_2.sety(y)

    if bat_2.ycor() < -250:
        bat_2.sety(-250)

# Keyboard bindings
wn.listen()
wn.onkeypress(bat_1_up, "w")
wn.onkeypress(bat_1_down, "s")
wn.onkeypress(bat_2_up, "Up")
wn.onkeypress(bat_2_down, "Down")


# Main game loop
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1


    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1



    # Left and right
    if ball.xcor() > 350:
        score_1 += 1
        text.clear()
        text.write("Player  A  :  {}               Player  B  :  {}".format(score_1, score_2), align="center", font=("ARCADECLASSIC", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_2 += 1
        text.clear()
        text.write("Player  A  :  {}               Player  B   :  {}".format(score_1, score_2), align="center", font=("ARCADECLASSIC", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < bat_1.ycor() + 50 and ball.ycor() > bat_1.ycor() - 50:
        ball.dx *= -1


    
    elif ball.xcor() > 340 and ball.ycor() < bat_2.ycor() + 50 and ball.ycor() > bat_2.ycor() - 50:
        ball.dx *= -1


    if score_1 > 4 or score_2 > 4:
        ball.reset()
        bat_1.reset()
        bat_2.reset()
        text.clear()
        text.goto(0, 0)
        text.write("GAME OVER!!", align="center", font=("ARCADECLASSIC", 50, "bold"))


    


