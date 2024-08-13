import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light green")
screen.title("Catch The Turtle")
FONT = ('Arial',15,'bold')
score = 0

#turtle list

turtle_list = []

#score turtle
score_turtle = turtle.Turtle()
def setup_score_turtle():
    global score_turtle
    score_turtle.hideturtle()
    score_turtle.color("black")
    score_turtle.penup()

    top_height = screen.window_height()/2
    y = top_height * 0.9

    score_turtle.setpos(0,y)
    score_turtle.write(arg="score = 0", move = False, align="center", font = FONT)

grid_size = 10
def make_turtle(x,y):

    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        global score_turtle
        score_turtle.clear()
        score_turtle.write(arg="score = {}".format(score), move=False, align="center", font=FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x * grid_size,y * grid_size)
    turtle_list.append(t)

x_coordinates = [-20,-10,0,10,20]
y_coordinates = [-20,-10,0,10,20]

def setup_turtles():

    for i in x_coordinates:
        for j in y_coordinates:
            make_turtle(i,j)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

#recursive bir fonksiyonun içerisinde kendini çağırmak
def show_turtles_randomly():
    hide_turtles()
    random.choice(turtle_list).showturtle()
    screen.ontimer(show_turtles_randomly,500)

turtle.tracer(0)
setup_score_turtle()
setup_turtles()
hide_turtles()
show_turtles_randomly()
turtle.tracer(1)
turtle.mainloop()

