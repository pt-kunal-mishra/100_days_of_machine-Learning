from turtle import *
width(4)
color('red')
fillcolor('yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos())<1:
        break
# for steps in range(1000):
#     for c in ("blue","red","green"):
#         color(c)
#         forward(steps)
#         right(30)
# forward(100)  
# left(90)
# forward(100)
# right(90)
# home()
# clearscreen()
# # up(20)
# # down(30)
