# Simple Snake Game
# By @DipadityaDas

import turtle
import time
import random

delay = 0.15

# Score
score = 0
high_score = 0

# Setup the screen
window = turtle.Screen()
window.title("Snake Game by @DipadityaDas")
window.bgcolor("purple")
window.setup(width=600, height=600)
window.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0 ", align="center", font=("Courier", 24, "normal"))

segments = []

# Snake Direction Functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


# Keybindings
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")

# Main Game Loop
while True:
    window.update()
    # Check for a collison with the border
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        # Hide the Segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score and delay
        delay = 0.15
        score = 0
        pen.clear()
        pen.write(
            "Score: {} High Score: {} ".format(score, high_score),
            align="center",
            font=("Courier", 24, "normal"),
        )

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to the random position
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add segments
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shortend the Delay
        delay -= 0.001

        # Increase The Score
        score = score + 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(
            "Score: {} High Score: {} ".format(score, high_score),
            align="center",
            font=("Courier", 24, "normal"),
        )

    # Move the end segment first
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the Segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score and delay
            delay = 0.15
            score = 0
            pen.clear()
            pen.write(
                "Score: {} High Score: {} ".format(score, high_score),
                align="center",
                font=("Courier", 24, "normal"),
            )

    time.sleep(delay)

window.mainloop()
