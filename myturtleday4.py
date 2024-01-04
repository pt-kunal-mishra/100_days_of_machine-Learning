from turtle import *

# wn=Screen()
# star=Turtle()
# wn.bgcolor("blue")
# wn.title("Turtle")


# #for i in range(4):
# #    forward(150)
# #   right(90)


# # Turtle
# # right(75)
# # forward(100)

# # for i in range(4):
# #     right(144)
# #     forward(100)
   

# # hexagon

# # num_side=6
# # side_len=100
# # angle=360.0/num_side

# # for i in range(num_side):
# #     forward(side_len)
# #     right(angle)

# # star.speed(3)

# # for i in range(2):
# #     forward(100)
# #     left(60)
# #     forward(50)
# #     left(120)

# # circle

# star.speed(0)

# star.fillcolor("white")
# star.begin_fill()

# star.circle(30)
# star.end_fill()
# star.hideturtle()


# done()  

wn=Screen()
wn.bgcolor("orange")
tur=Turtle()
tur.color("blue")

tur.speed(2)

for i in range(100):
    circle(5*i)
    circle(-5*i)
    left(i)

exitonclick()    

# def sqrfunc(size):
#     for i in range(4):
#         tur.fd(size)
#         tur.left(90)
#         size=size+15

# sqrfunc(6)
# sqrfunc(26)
# sqrfunc(46)
# sqrfunc(66)
# sqrfunc(86)
# sqrfunc(106)
# sqrfunc(126)
# sqrfunc(146)          
