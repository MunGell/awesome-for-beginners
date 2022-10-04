import turtle as t
import random
 
w = 500 # Width of box
h = 500 # Height of box
food_size = 10 # Size of food
delay = 100 # in millisecond

# Values by which snake will move in direction when given direction
offsets = {
    "up": (0, 20),
    "down": (0,-20),
    "left": (-20,0),
    "right": (20,0)
}
global SCORE
SCORE = 0
# Default postion of game scene
def reset():
    global snake, snake_dir, food_position, pen
 
    snake = [[0,0],[0,20],[0,40],[0,60],[0,80]]
    snake_dir = "up" #default snake direction
    food_position = get_random_food_position()
    food.goto(food_position) # render food on scene
    move_snake()

def move_snake():
    global snake_dir,SCORE
 
    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_dir][0]
    new_head[1] = snake[-1][1] + offsets[snake_dir][1]
    
     
    if new_head in snake[:-1]:
        print(SCORE)
        reset()
    else:
        snake.append(new_head)
 
     
        if not food_collision():
            snake.pop(0)
 
 
        if snake[-1][0] > w / 2:
            snake[-1][0] -= w
        elif snake[-1][0] < - w / 2:
            snake[-1][0] += w
        elif snake[-1][1] > h / 2:
            snake[-1][1] -= h
        elif snake[-1][1] < -h / 2:
            snake[-1][1] += h
 
 
        pen.clearstamps()
 
         
        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()
 
         
        screen.update()
 
        t.ontimer(move_snake, delay)
 
def food_collision():
    global food_position, SCORE
    if get_distance(snake[-1], food_position) < 20:
        SCORE += 10
        food_position = get_random_food_position()
        food.goto(food_position)
        return True
    return False
 
def get_random_food_position():
    x = random.randint(- w / 2 + food_size, w / 2 - food_size)
    y = random.randint(- h / 2 + food_size, h / 2 - food_size)
    return (x, y)
 
def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance
# Control
def go_up():
    global snake_dir
    if snake_dir != "down":
        snake_dir = "up"
def go_down():
    global snake_dir
    if snake_dir != "up":
        snake_dir = "down"
def go_left():
    global snake_dir
    if snake_dir != "right":
        snake_dir = "left"
def go_right():
    global snake_dir
    if snake_dir != "left":
        snake_dir = "right"



#define screen setup
screen = t.Screen()
screen.setup(w, h)
screen.title("Snake Game")
screen.bgcolor("lightgrey")
screen.tracer(0)

#define snake setup
pen = t.Turtle("square")
pen.penup()

#define food setup
food = t.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(food_size / 20)
food.penup()

#define control setup
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

reset()
t.done()
