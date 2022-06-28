import turtle as t
import colorgram
# importing colorgram for extracting colors
import random

t.colormode(255)
colors = colorgram.extract('image.jpg', 40)
RgbColor = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
tim = t.Turtle()
tim.speed("fastest")  # to speed up the animation
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(500)
tim.setheading(0)
for times in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(RgbColor))
        tim.forward(50)
    tim.dot(20, random.choice(RgbColor))
    tim.setheading(90)
    tim.forward(50)
    if times % 2 == 0:
        tim.setheading(180)
    else:
        tim.setheading(0)
scr = t.Screen()
scr.exitonclick()
