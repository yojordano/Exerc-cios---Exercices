from turtle import *
sleepers = int(input('How many sleepers? '))


pencolor('gray')
penup()
backward(160)
pendown()
left(90)

for i in range(sleepers): 
    pensize(10)
    forward(100)
    backward(100)
    right(90)
    penup()
    forward(40)
    pendown()
    left(90)
    
