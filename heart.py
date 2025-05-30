import turtle
import time
import random
import math

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Animated Sparkling Heart")

# Heart turtle
heart = turtle.Turtle()
heart.pensize(2)
heart.color("red")
heart.speed(0)
heart.hideturtle()

# Sparkle turtle
sparkle = turtle.Turtle()
sparkle.hideturtle()
sparkle.speed(0)
sparkle.color("white")
sparkle.pensize(1)

# Function to draw a heart
def draw_heart(scale=1):
    heart.penup()
    heart.goto(0, -50 * scale)
    heart.setheading(140)
    heart.pendown()
    heart.begin_fill()
    heart.fillcolor("red")
    heart.forward(113 * scale)
    for _ in range(200):
        heart.right(1)
        heart.forward(1 * scale)
    heart.left(120)
    for _ in range(200):
        heart.right(1)
        heart.forward(1 * scale)
    heart.forward(112 * scale)
    heart.end_fill()

# Function to create sparkles
def create_sparkles():
    sparkle.penup()
    for _ in range(10):  # Number of sparkles
        x = random.randint(-150, 150)
        y = random.randint(-150, 150)
        sparkle.goto(x, y)
        sparkle.dot(random.randint(2, 6), "white")  # Random sparkle size

# Main animation loop
def animate_heart():
    scale = 1
    growing = True
    while True:
        heart.clear()
        draw_heart(scale)
        create_sparkles()
        time.sleep(0.05)

        # Adjust scale for pulsing effect
        if growing:
            scale += 0.02
            if scale >= 1.2:  # Max scale
                growing = False
        else:
            scale -= 0.02
            if scale <= 0.8:  # Min scale
                growing = True

# Run the animation
animate_heart()
