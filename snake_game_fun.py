
#this is jeremy the snek
#------------------------

import turtle
import random

turtle.tracer(1, 0)

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)
turtle.penup()

SQUARE_SIZE = 25
START_LENGTH= 4

#lists
pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]

snake=turtle.clone()
snake.shape("square")

turtle.hideturtle()

#####################################################

for i in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos=x_pos+SQUARE_SIZE

    my_pos=(x_pos, y_pos)
    snake.goto(x_pos, y_pos)
    pos_list.append(my_pos)

    stamp_ID=snake.stamp()
    stamp_list.append(stamp_ID)

#####################################################

UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
TIME_STEP=100

SPACEBAR="space"

UP=0
DOWN=1
LEFT=2
RIGHT=3
direction=UP

#edges and edge lines

UP_EDGE = 360
DOWN_EDGE = -360
RIGHT_EDGE = 550
LEFT_EDGE = -550
edgy_turtle=turtle.clone()
edgy_turtle.hideturtle()
edgy_turtle.penup()
edgy_turtle.goto(550, 360)
edgy_turtle.pendown()
edgy_turtle.pensize(15)
edgy_turtle.goto(-550, 360)
edgy_turtle.goto(-550, -360)
edgy_turtle.goto(550, -360)
edgy_turtle.goto(550, 360)


def up():
    global direction
    direction=UP
    print("You pressed the ^ KEY!")

def down():
    global direction
    direction=DOWN
    print("You pressed the v KEY!")    

def left():
    global direction
    direction=LEFT
    print("You pressed the <- KEY!")

def right():
    global direction
    direction=RIGHT
    print("You pressed the -> KEY!")

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()

def make_food():
    
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food_ID=(food_x, food_y)
    food_pos.append(food_ID)
    food.goto(food_x, food_y)
    food_stamp=food.stamp()
    food_stamps.append(food_stamp)
def move_snake():
    my_pos=snake.pos()
    x_pos=my_pos[0]
    y_pos= my_pos[1]

    if direction==RIGHT:
         snake.goto(x_pos+SQUARE_SIZE, y_pos)
         print("You moved Right")
        
    elif direction==LEFT:
         snake.goto(x_pos-SQUARE_SIZE, y_pos)
         print("You moved Left")

    elif direction==DOWN:
         snake.goto(x_pos, y_pos - SQUARE_SIZE)
         print("You moved Down")

    elif direction==UP:
         snake.goto(x_pos, y_pos + SQUARE_SIZE)
         print("You moved UP")

#this shows the tail after the squares move

    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)

    global food_stamps,food_pos
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("You have eaten the food!")
        make_food()
#this gets rid of the tail at the end
    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)

#edges
    
    
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()

    if new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()

    if new_y_pos >= UP_EDGE:
        print("You hit the upper edge! Game over!")
        quit()

    if new_y_pos <= DOWN_EDGE:
        print("You hit the lower edge! Game over!")
        quit()

    #eat urself command thing
    if pos_list[-1] in pos_list[:-1]:
        print("You ate yourself, yum!")
        quit()

    turtle.ontimer(move_snake,TIME_STEP)
move_snake()

turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif")
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

for this_food_pos in food_pos:
    x = this_food_pos [0]
    y = this_food_pos [1]
    food.goto(x, y)
    food_stamp=food.stamp()
    food_stamps.append(food_stamp)
