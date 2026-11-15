import os
import turtle
import winsound

# Caminho do som (sempre na mesma pasta deste arquivo .py)
BASE = os.path.dirname(os.path.abspath(__file__))
SOM = os.path.join(BASE, "BOOM.wav")


def tocar_som():
    try:
        winsound.PlaySound(SOM, winsound.SND_FILENAME | winsound.SND_ASYNC)
    except RuntimeError:
        pass  # se o som falhar, o jogo continua normalmente


# Configuração da janela
wn = turtle.Screen()
wn.title("Pong by @trashcode")
wn.bgcolor("darkblue")
wn.setup(width=800, height=600)
wn.tracer(0)

# Placar
score_a = 0
score_b = 0

# Raquete A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("#f1f1f1")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Raquete B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("#f1f1f1")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("#f1f1f1")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.10
ball.dy = -0.10

# Texto do placar
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)


def atualizar_placar():
    pen.clear()
    pen.write(
        "Player A: {}  Player B: {}".format(score_a, score_b),
        align="center",
        font=("Courier", 24, "normal"),
    )


atualizar_placar()


# Movimento das raquetes (com limite para não sair da tela)
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        paddle_a.sety(y + 20)


def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:
        paddle_a.sety(y - 20)


def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        paddle_b.sety(y + 20)


def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        paddle_b.sety(y - 20)


# Teclado
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Loop principal
while True:
    wn.update()

    # Mover a bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bordas de cima e de baixo
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        tocar_som()

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        tocar_som()

    # Ponto para o Player A (bola saiu pela direita)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        atualizar_placar()

    # Ponto para o Player B (bola saiu pela esquerda)
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        atualizar_placar()

    # Colisão com a raquete B
    if (340 < ball.xcor() < 350) and (
        paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50
    ):
        ball.setx(340)
        ball.dx *= -1
        tocar_som()

    # Colisão com a raquete A
    if (-350 < ball.xcor() < -340) and (
        paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50
    ):
        ball.setx(-340)
        ball.dx *= -1
        tocar_som()