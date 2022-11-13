from turtle import*
from random import randint

finish = 200

t1 = Turtle()
t1.penup()
t1.goto(-200,-20)
t1.color('red')
t1.shape('turtle')

t2 = Turtle()
t2.penup()
t2.goto(-200,20)
t2.color('blue')
t2.shape('turtle')
t3 = Turtle()
t3.color('grey')
l = -200
t3.right(90)
for i in range(10):
    t3.penup()
    t3.goto(l,200)
    t3.pendown()
    t3.forward(400)
    l += 40
t3.hideturtle()    
while t1.xcor() < finish and t2.xcor() < finish:
    t1.forward(randint(2,7))
    t2.forward(randint(2,7))

winner = max(t1.xcor(),t2.xcor())
exitonclick()
