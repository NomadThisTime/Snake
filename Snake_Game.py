import turtle
import random
import time


# turtle screen
screen = turtle.Screen()
screen.title('SNAKE')
screen.setup(width = 1000, height = 1000)
screen.tracer(0)
turtle.bgcolor('yellow')


# border
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-450,450)
turtle.pendown()
turtle.color('black')
turtle.forward(900)
turtle.right(90)
turtle.forward(900)
turtle.right(90)
turtle.forward(900)
turtle.right(90)
turtle.forward(900)
turtle.penup()
turtle.hideturtle()


# score
score = 0
delay = 0.1


# snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color("black")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'


# size of the snake to be used later in the main loop
size = []
size.append(snake)


# food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(60, 60)


# scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 450)
scoring.write("Score :", align="center", font=("Courier", 24, "bold"))


# movement
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"


def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"


def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"


def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"


def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


# Keyboard bindings
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

# ending screen
def end():
    time.sleep(1)
    screen.clear()
    screen.bgcolor('yellow')
    scoring.goto(0, 0)
    scoring.write("    GAME OVER \n Your Score is {}".format(score),
                  align="center", font=("Courier", 30, "bold"))


# main loop
while True:
    screen.update()

    # snake and food collision
    if snake.distance(food) == 0:
        x = random.randrange(-440, 440, 20)
        y = random.randrange(-440, 440, 20)
        food.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("Score:{}".format(score), align="center", font=("Courier", 24, "bold"))
        delay -= 0.001

        # creating snake segments
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape('square')
        segment.color('gray')
        segment.penup()
        size.append(segment)

    # adding segments to snake
    for index in range(len(size) - 1, 0, -1):
        a = size[index-1].xcor()
        b = size[index-1].ycor()
        size[index].goto(a, b)
    snake_move()

    # snake and border collision
    if snake.xcor() > 450 or snake.xcor() < -450 or snake.ycor() > 450 or snake.ycor() < -450:
        end()

    # snake collision
    for ball in size[2:]:
        if ball.distance(snake) == 0:
            end()

    time.sleep(delay)


turtle.Terminator()
