from turtle import*
from random import randrange
from freegames import squar,vector
food=vector(0,0)
snake=[vector(10,0)]
aim=vector(0-10)
def change(x,y):
    ami.x=x
    aim.y=y
    
def inside(head):
    return-200<head.x<190and-200<head.y<190
def move():
    head=snake[-1].copy()
    head.move(aim)
    
if not inside(head)or head in snake:
    squar(head.x,head.y,9,"red")
update()
return
snake.append()
if head ==food:
    print('snake',len(snake))
    food.x=randrange(-15,15)*10
    food.y=randrange(-15,15)*10
    
else:
    snake.pop(0)
    clear()
    for body in snake:
        square(food.x,food.y,9,'green')
        square(food.x,food.y,9,'red')
        update()
        ontimer(move,100)
        hideturtle()
        tracer(false)
        listen()
        onkey(lambda:changes(10,0),'right')
        onkey(lambda:changes(-10,0),'left')
        onkey(lambda:changes(0,10),"up")
        onkey(lambda:changes(0,-10),"down")
        move()
        done()
