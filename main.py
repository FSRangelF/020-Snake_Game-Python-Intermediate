from turtle import Turtle, Screen
import random

# 1. Create a Snake Body
screensize = 800

screen = Screen()
screen.setup(width=screensize, height=screensize)
screen.bgcolor("black")

snake = Turtle(shape="square")
snake.color("white")
snake.speed("slowest")
#snake.resizemode("user")
#snake.shapesize(stretch_wid=1,stretch_len=4,outline=4)

# 2.1 control the the snake
def rotate_right():
    snake.rt(90)

def rotate_left():
    snake.left(90)

def increase_snake_size():
    pass

# 3. Create snake food
food_x = 0
food_y = 0
def create_food():
    food = Turtle(shape="circle")
    food.color("blue")
    food.resizemode("user")
    food.shapesize(stretch_wid=1,stretch_len=1,outline=4)
    global food_x 
    food_x = random.randint(int(-screensize/2), int(screensize/2))
    global food_y
    food_y = random.randint(int(-screensize/2), int(screensize/2))

    food.teleport(x=food_x, y=food_y)

create_food()

# 5. Create a scoreboard
score = 0

# 2. Move the snake
game_over = False
while not game_over:
    snake.forward(10)
    screen.listen()
    screen.onkeypress(key="a", fun=rotate_right)
    screen.onkeypress(key="d", fun=rotate_left)
    # 4. Detect collision with food
    if snake.xcor() == food_x and snake.ycor() == food_y:
        score += 1
        increase_snake_size()
        create_food()




# 6. Detect collision with the wall
# 7. detect collision with tail/body

screen.exitonclick()