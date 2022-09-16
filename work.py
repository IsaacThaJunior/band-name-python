from turtle import Turtle, Screen

c2 = Turtle()
# Draw a square


def draw_shape(number):
    angle = 360 / number
    for _ in range(number):
        c2.forward(100)
        c2.right(angle)


for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()


