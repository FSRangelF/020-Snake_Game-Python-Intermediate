from turtle import Turtle, Screen
import random
import time

# setup screen
screensize = 600
screen = Screen()
screen.setup(width=screensize, height=screensize)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# setup snake
snake_segments = []
starting_position = [(0,0), (-20, 0), (-40, 0)]

# setup food
food_x = 0
food_y = 0
food = Turtle(shape="circle")
food.color("blue")

def rotate_right():
    snake_segments[0].right(90)

def rotate_left():
    snake_segments[0].left(90)

def increase_snake_size():
    segment = Turtle(shape="square")
    segment.color("white")
    segment.penup()
    segment.setposition(snake_segments[-1].pos())
    snake_segments.append(segment)

def position_food():
    global food_x 
    global food_y
    global food
    food_x = 20*random.randint(int(-1*(screensize-20)/40), int((screensize-20)/40))
    food_y = 20*random.randint(int(-1*(screensize-20)/40), int((screensize-20)/40))
    food.teleport(x=food_x, y=food_y)

# create the snake
for index in range(3):
    segment = Turtle(shape="square")
    segment.color("white")
    segment.penup()
    segment.setposition(starting_position[index])
    snake_segments.append(segment)

position_food()

# Create a scoreboard
score = 0
print(score)

# move the snake
game_over = False
while not game_over:
    screen.update()
    for index in range (len(snake_segments)-1, 0, -1):
        new_position = snake_segments[index-1].position()
        snake_segments[index].setposition(new_position)
    snake_segments[0].forward(20)

    # Control direction
    screen.listen()
    screen.onkey(key="d", fun=rotate_right)
    screen.onkey(key="a", fun=rotate_left)

    # Detect collision with the food
    if round(snake_segments[0].xcor(),0) == round(food_x, 0) and round(snake_segments[0].ycor(), 0) == round(food_y, 0):
        score += 1
        position_food()
        increase_snake_size()
        print(score)
   
    # Detect collision with the wall
    if round(snake_segments[0].xcor(),0) == -screensize/2 or round(snake_segments[0].xcor(),0) == screensize/2 or round(snake_segments[0].ycor(),0) == -screensize/2 or round(snake_segments[0].ycor(),0) == screensize/2:
        game_over = True

    # # detect collision with tail/body
    for index in range(1, len(snake_segments)-1):
        if round(snake_segments[0].xcor(),0) == round(snake_segments[index].xcor()) and round(snake_segments[0].ycor(), 0) == round(snake_segments[index].ycor()):
            game_over = True

    # increase speed as the score increases
    if score < 10:
        speed_factor = 1
    else:
        speed_factor = score // 5
    time.sleep(0.1/speed_factor)

screen.exitonclick()