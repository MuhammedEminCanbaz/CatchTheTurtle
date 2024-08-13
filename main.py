import turtle

screen = turtle.Screen()
screen.bgcolor("light green")
screen.title("Catch The Turtle")
FONT = ('Arial',15,'bold')



#score turtle

def setup_score_turtle():
    score_turtle = turtle.Turtle()
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
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x * grid_size,y * grid_size)

x_coordinates = [-20,-10,0,10,20]
y_coordinates = [-20,-10,0,10,20]

for i in x_coordinates:
    for j in y_coordinates:
        make_turtle(i,j)

setup_score_turtle()


turtle.mainloop()