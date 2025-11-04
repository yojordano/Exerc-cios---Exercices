from turtle import *

# Define the draw_line function here:
colormode(255)
def draw_line(value):
  color((value, value, value))
  pensize(8)
  penup()
  forward(30)
  pendown()
  forward(40)
  penup()
  backward(70)

# Define the load_indicator function here:
def load_indicator(num_lines):
  colour_value = 0
  angle = 360 / num_lines
  
  for _ in range(num_lines):
    draw_line(colour_value)
    left(angle)
    colour_value = colour_value + 20

if __name__ == "__main__":
  # Write your tests here!
  # Anything indented inside this block will be ignored by the marker.
  # Test 
  load_indicator(12)
