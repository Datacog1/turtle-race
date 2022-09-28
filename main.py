import random
import turtle 


is_race_on = False
colors = ["red","orange","yellow","green","blue","purple"]
y_axis = [-180,-120,-60,0,60,120,180]

all_turtles = []
my_screen = turtle.Screen()
my_screen.setup(500,400)
user_bet = my_screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")



for i in range(0,6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230,y_axis[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0,10)
        turtle.fd(random_distance)

my_screen.exitonclick()