from turtle import *

def draw_rect(width, height, colour):
  # Finish the function to draw a rectangle:
  pensize(3)
  pencolor(colour)
  pendown()
  
  forward(width)
  left(90)
  forward(height)
  left(90)
  forward(width)
  left(90)
  forward(height)
  left(90)
  

# Draw the first building:
draw_rect(30, 120, 'royalblue')
goto(-10, 0)
draw_rect(80, 30, 'cornflowerblue')
goto(-30, 0)
draw_rect(80, 60, 'coral')
goto(-45, 0)
draw_rect(50, 80, 'plum')
