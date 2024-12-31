import turtle
import time
import random

def draw_star():
    """Draw a star for decoration."""
    star = turtle.Turtle()
    star.penup()
    star.goto(-100, 150)
    star.pendown()
    star.color("yellow")
    star.begin_fill()
    for _ in range(5):
        star.forward(200)
        star.right(144)
    star.end_fill()
    star.hideturtle()

def write_message():
    """Write a Happy New Year message."""
    message = turtle.Turtle()
    message.hideturtle()
    message.penup()
    message.goto(0, 50)
    message.color("blue")
    message.write("🎉 Happy New Year 2025! 🎉", align="center", font=("Lucida Calligraphy", 24, "bold"))
    message.goto(0, -30)
    message.color("white")
    message.write("Wishing you joy, health, and success in the year ahead!", align="center", font=("Arial", 18, "italic"))

def fireworks():
    """Create simple fireworks animations."""
    firework = turtle.Turtle()
    firework.hideturtle()
    colors = ["red", "blue", "green", "purple", "orange", "pink"]
    firework.speed(0)

    for _ in range(20):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        firework.penup()
        firework.goto(x, y)
        firework.pendown()
        firework.color(random.choice(colors))
        for _ in range(36):
            firework.forward(50)
            firework.right(170)
        firework.clear()

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Happy New Year 2025")

# Draw decorations and write the message
draw_star()
write_message()

# Show fireworks for a while
fireworks()

time.sleep(5)
screen.clear()

# Close the turtle graphics window
turtle.done()
