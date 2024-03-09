import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Game")
screen.bgcolor("white")
screen.bgpic("ocean2.png")



# Create the turtle player
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.speed(0)
player.penup()
player.goto(0, 0)

# Create a list to store fish turtles and their corresponding circles
fish_list = []
circle_list = []

# Function to create a new fish
def create_fish():
    fish = turtle.Turtle()
    fish.shape("circle")
    fish.color(random.choice(["red", "orange", "yellow", "green", "blue", "purple"]))  # Random color
    fish.speed(1)
    fish.penup()
    fish.goto(random.randint(-200, 375), random.randint(-200, 375))

    # Create a corresponding circle
    circle = turtle.Turtle()
    circle.speed(0)
    circle.shape("circle")
    circle.color("white")
    circle.shapesize(stretch_wid=0.6, stretch_len=0.6)  # Adjust size if needed
    circle.penup()
    circle.goto(fish.xcor(), fish.ycor())

    fish_list.append(fish)
    circle_list.append(circle)

# Function to move the player turtle
def move_up():
    y = player.ycor()
    y += 20
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= 20
    player.sety(y)

def move_left():
    x = player.xcor()
    x -= 20
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    player.setx(x)

# Keyboard bindings
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")

# Create initial fish
for _ in range(5):
    create_fish()

# Score variable
score = 0

# Scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("black")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Timer
start_time = time.time()
time_limit = 20  # in seconds

# Main game loop
while time.time() - start_time < time_limit:
    remaining_time = int(time_limit - (time.time() - start_time))
    
    for i in range(len(fish_list)):
        fish = fish_list[i]
        circle = circle_list[i]

        # Move fish
        fish.setx(fish.xcor() - 2)
        circle.setx(fish.xcor())

        # Check for collision with player
        if player.distance(fish) < 20:
            # Increase score
            score += 1
            scoreboard.clear()
            scoreboard.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

            # Remove fish and its circle from the screen
            fish.hideturtle()
            circle.hideturtle()
            fish_list.remove(fish)
            circle_list.remove(circle)

            # Create a new fish
            create_fish()

        # Check if fish is out of screen and remove it
        if fish.xcor() < -300:
            fish.hideturtle()
            circle.hideturtle()
            fish_list.remove(fish)
            circle_list.remove(circle)

    # Update the timer display
    scoreboard.clear()
    scoreboard.write("Score: {}\nTime: {}s".format(score, remaining_time), align="center", font=("Courier", 24, "normal"))

# Display final score
final_score_display = turtle.Turtle()
final_score_display.speed(0)
final_score_display.color("black")
final_score_display.penup()
final_score_display.hideturtle()
final_score_display.goto(0, 0)
final_score_display.write("Game Over\nFinal Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Close the window when clicked
turtle.done()



