import turtle

turtle1 = {'color': 'red', 'pensize': 1, 'fillcolor': 'yellow', 'squaresize': 50, 'x': 50, 'y': 100}
turtle2 = {'color': 'blue', 'pensize': 5, 'fillcolor': 'red', 'squaresize': 100, 'x': 300, 'y': 150}
turtle3 = {'color': 'green', 'pensize': 7, 'fillcolor': 'blue', 'squaresize': 150, 'x': 50, 'y': 400}
turtle4 = {'color': 'yellow', 'pensize': 10, 'fillcolor': 'green', 'squaresize': 200, 'x': 250, 'y': 450}

todd = turtle.Turtle()
tina = turtle.Turtle()
tyrell = turtle.Turtle()
talisha = turtle.Turtle()

turtles = {todd: turtle1, tina: turtle2, tyrell: turtle3, talisha: turtle4}

def turtle_maker(turtle, specs):
  turtle.color(specs['color'])
  turtle.pensize(specs['pensize'])
  turtle.fillcolor(specs['fillcolor'])
  turtle.penup()

def draw_square(turtle, size, x, y):
  turtle.goto(x, y)
  turtle.pendown()
  turtle.begin_fill()
  for i in range(4):
    turtle.forward(size)
    turtle.left(90)
  turtle.end_fill()

for turtle, specs in turtles.items():
  turtle_maker(turtle, specs)
  draw_square(turtle, specs['squaresize'], specs['x'], specs['y'])
  
  