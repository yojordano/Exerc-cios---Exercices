from turtle import *

def draw_petal(colour):
  pencolor(colour)
  for i in range(4):
    forward(60)
    left(90)

# Write your code below!
bgcolor('lightgreen')
fillcolor('hotpink')
begin_fill()
pensize(5)

x = int(input('How many petals? '))
code = (x)

angle = 360 / x

for i in range(x):
  draw_petal('purple')
  left(angle)

end_fill()
  

