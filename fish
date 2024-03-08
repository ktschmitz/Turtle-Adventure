import tkinter as tk
import turtle
import random
from PIL import Image, ImageTk

# Initialize Tkinter
root = tk.Tk()
root.title("Blue Aquarium")

# Set up canvas
canvas = tk.Canvas(root, width=800, height=600, bg="lightblue")
canvas.pack()

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


# Open the image file
original_image = Image.open("floor.png")

# Resize the image
resized_image = original_image.resize([800, 400])

# Convert the resized image to a PhotoImage object
backgroundImage = ImageTk.PhotoImage(resized_image)

sharkImage = ImageTk.PhotoImage(Image.open("dancingShark.gif").resize([125, 200]))
jellyfishImage = ImageTk.PhotoImage(Image.open("jellyfish.png").resize([60, 100]))

# Bubble properties
bubbles = []


# Function to move the fish
def move_fish(fish):
    fish["x"] += fish["speed"]
    if fish["x"] - fish["size"] >= 800:  # Reset fish position when it reaches the right edge
        fish["x"] = - fish["size"]

# Draw the fish with eyes and a smile
def draw_fish(x, y, size, color):
    canvas.create_oval(x, y, x + size, y + size, fill=color)  # Body
    canvas.create_polygon(x - size / 2 + 32, y + size / 2, x-36, y + size/ 5 - 1, x-36, y + size * 4 / 5 + 1, fill="black") # Tail Outline
    canvas.create_polygon(x - size / 2 + 30, y + size / 2, x-35, y + size/ 5, x-35, y + size * 4 / 5, fill=color) # Tail Fill
    canvas.create_oval(x + size / 4, y + size / 4, x + size / 4 + 5, y + size / 4 + 5, fill="black")  # Left eye
    canvas.create_oval(x + size / 4 * 3, y + size / 4, x + size / 4 * 3 + 5, y + size / 4 + 5, fill="black")  # Right eye
    canvas.create_arc(x + size / 4, y + size / 2, x + size / 4 * 3, y + size / 4 * 3, start=180, extent=180, style=tk.ARC)  # Smile



# Function to draw the aquarium
def draw_aquarium():
    canvas.delete("all")
    
    # Pic's upper-left corner (NW) on the canvas is at x=50 y=10.
    canvas.create_image(400, 400, image=backgroundImage)

    canvas.create_image(400, 400, image=sharkImage)
    canvas.create_image(200, 400, image=jellyfishImage)
    canvas.create_image(100, 300, image=jellyfishImage)
    canvas.create_image(700, 100, image=jellyfishImage)
    # Draw the fish
    for fish in fishList:
        draw_fish(fish["x"], fish["y"], fish["size"], fish["color"])
    
    # Generate random bubbles
    if random.randint(0, 100) < 5:
        bubble_size = random.randint(5, 15)
        bubble_x = random.randint(0, 800)
        bubble_y = 600
        bubbles.append((bubble_x, bubble_y, bubble_size))
    
    # Move bubbles upward
    for i in range(len(bubbles)):
        x, y, size = bubbles[i]
        y -= random.randint(0, 100) / 200  # Adjust the speed of bubbles here
        bubbles[i] = (x, y, size)
    
    # Draw bubbles
    for bubble_x, bubble_y, bubble_size in bubbles:
        canvas.create_oval(bubble_x, bubble_y, bubble_x + bubble_size, bubble_y + bubble_size, fill="white")
    
    root.update()

while True:
    # Start moving the fish
    for fish in fishList:
        move_fish(fish)

    draw_aquarium()

# Run the Tkinter event loop
root.mainloop()
