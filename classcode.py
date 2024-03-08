import turtle
import random



# Set up the screen
screen = turtle.Screen()
screen.bgpic("ocean.png")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off automatic screen updates

'''
# Set up canvas
canvas = tk.Canvas(root, width=800, height=600, bg="lightblue")
canvas.pack()
'''



#Create turtle
turtle = turtle.Turtle()
turtle.shape('turtle')
turtle.fillcolor("green")
turtle.penup()
turtle.speed(0)
turtle.goto(-350, 100)

# Fish properties
fishList = [
    {
        "x": 60,
        "y": 300,
        "size" : 60,
        "speed" : random.randint(25, 75)/100,
        "color": "orange"
    },
    {
        "x": 60,
        "y": 100,
        "size" : 60,
        "speed" : random.randint(25, 75)/100,
        "color": "pink"
    },
    {
        "x": 60,
        "y": 500,
        "size" : 60,
        "speed" : random.randint(25, 75)/100,
        "color": "yellow"
    },
]

# Function to move the fish
def move_fish(fish):
    fish["x"] += fish["speed"]
    if fish["x"] - fish["size"] >= 800:  # Reset fish position when it reaches the right edge
        fish["x"] = - fish["size"]





'''
# Draw the fish with eyes and a smile
def draw_fish(x, y, size, color):
    canvas.create_oval(x, y, x + size, y + size, fill=color)  # Body
    canvas.create_polygon(x - size / 2 + 32, y + size / 2, x-36, y + size/ 5 - 1, x-36, y + size * 4 / 5 + 1, fill="black") # Tail Outline
    canvas.create_polygon(x - size / 2 + 30, y + size / 2, x-35, y + size/ 5, x-35, y + size * 4 / 5, fill=color) # Tail Fill
    canvas.create_oval(x + size / 4, y + size / 4, x + size / 4 + 5, y + size / 4 + 5, fill="black")  # Left eye
    canvas.create_oval(x + size / 4 * 3, y + size / 4, x + size / 4 * 3 + 5, y + size / 4 + 5, fill="black")  # Right eye
    canvas.create_arc(x + size / 4, y + size / 2, x + size / 4 * 3, y + size / 4 * 3, start=180, extent=180, style=tk.ARC)  # Smile
'''
    

def draw_aquarium():
 # Draw the fish
    for fish in fishList:
        draw_fish(fish["x"], fish["y"], fish["size"], fish["color"])


screen.update()
screen.mainloop()
