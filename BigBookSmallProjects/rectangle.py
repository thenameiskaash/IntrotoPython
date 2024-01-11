import turtle
  
t = turtle.Turtle()
r = int(input("Enter the length of the side of square: "))
 
for _ in range(4):
  t.forward(r) # Forward turtle by s units
  t.left(90) # Turn turtle by 90 degree