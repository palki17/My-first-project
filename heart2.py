import turtle
import math

# ----- Screen Setup -----
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Heart for KUCHU PUCHU ❤️")

# ----- Turtle Setup -----
heart = turtle.Turtle()
heart.speed(0)
heart.color("red")
heart.width(3)
heart.hideturtle()

# ----- Heart Points Function -----
def heart_points():
    points = []
    for t in range(361):
        rad = math.radians(t)
        x = 16 * math.sin(rad)**3
        y = (13 * math.cos(rad)
             - 5 * math.cos(2 * rad)
             - 2 * math.cos(3 * rad)
             - math.cos(4 * rad))
        points.append((x * 15, y * 15))
    return points

points = heart_points()

# ----- Draw Heart and Fill Instantly -----
heart.penup()
heart.goto(points[0])
heart.pendown()
heart.fillcolor("red")
heart.begin_fill()
for point in points:
    heart.goto(point)
heart.end_fill()

# ----- Add Text Above Heart -----
heart.penup()
heart.goto(0, max(y for x, y in points) + 40)  # 40 pixels above top of heart
heart.color("red")
heart.write("I LOVE YOU KUCHU PUCHU ❤️",
            align="center",
            font=("Arial", 24, "bold"))

turtle.done()
