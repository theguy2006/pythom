import turtle
# window configuration
wn = turtle.Screen()
wn.title("Pong by @trashcode")
wn.bgcolor(("darkblue"))
wn.setup(width=800, height=600)
wn.tracer(0)

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("#f1f1f1")
paddle_a.shapesize(stretch_wid=4, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("#f1f1f1")
paddle_b.shapesize(stretch_wid=4, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("#f1f1f1")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.05
ball.dy = -0.05
#function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_a.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_a.sety(y)
#keyboard_biding
wn.listen()
wn.onkeypress(paddle_a_up, "Up")
wn.onkeypress(paddle_a_down, "Down")
wn.onkeypress(paddle_b_up, "w")
wn.onkeypress(paddle_b_down, "s")
# Main game loop
while True:
    wn.update()

#MOVE THE BALL
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
#BORDER CHECKING
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
    if ball.xcor() <  -390:
        ball.goto(0, 0)
        ball.dx *= -1
    #PADDLE AND BALL COLLISIONS:
    if ball.xcor
