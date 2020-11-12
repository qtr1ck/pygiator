import turtle

wn = turtle.Screen()
wn.bgcolor("black")
t = turtle.Turtle()
t.shape("turtle")
t.color("white")

t.penup()
size=20
for i in range(30):
    t.stamp()
    size = size + 3
    t.forward(size)
    t.right(24)