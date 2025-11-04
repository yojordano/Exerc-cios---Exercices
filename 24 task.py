from turtle import *

# Define the dandelion function here:
def dandelion(x, y, length):
  penup()
  goto(x, -150)
  pendown()
  
  pensize(3)
  pencolor("#91F485")
  goto(x, y)
  
  angle = 360/40
  
  for _ in range(20):
    pencolor("#0085C7")
    forward(length)
    backward(length)
    left(angle)
    
    pencolor("#009F3D")
    forward(length)
    backward(length)
    left(angle)
    
if __name__ == "__main__":
  # Test the function
  bgcolor('#ECFAF5')
  dandelion(-0, 50, 60)
