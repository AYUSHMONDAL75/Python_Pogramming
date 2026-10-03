import turtle
import cv2
import numpy as np
import time
import os

# ================ SETTINGS ================
IMAGE_FILE = "Krishna.jpg"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 785
DRAW_SIZE = 780
DRAW_DELAY = 0.03
UPDATE_EVERY = 1 # 1 = maximum smoothness
LINE_WIDTH = 2.5
LINE_COLOR = "#00BFFF"
MIN_CONTOUR_LENGTH = 15 # Ignore very tiny contours
APPROXIMATION = 0.8 # Image detail

# ================ IMAGE ================
if not os.path.exists(IMAGE_FILE):
    input("=======ERROR: IMAGE NOT FOUND=======\nPress Enter to close...")
    raise SystemExit

image = cv2.imread(IMAGE_FILE)

if image is None:
    input("Could not open the image.\nPress Enter to close...")
    raise SystemExit

original_height, original_width = image.shape[:2]
print("Showing Image")

# ================ CONVERT TO HSV ================
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#================ KRISHNA LINES ================
lower_cyan = np.array([75, 70, 60])
upper_cyan = np.array([115, 255, 255])
mask = cv2.inRange(hsv, lower_cyan, upper_cyan)

# ================ IMAGE ================
kernel = np.ones((2, 2), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# ================ FIND CONTOURS ================
contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# ================ PREPARE PATHS ================
paths = []
for contour in contours:
    # Calculate contour length
    length = cv2.arcLength(contour, False)

    # Remove tiny noise
    if length < MIN_CONTOUR_LENGTH:
        continue

    # Simplify contour slightly
    approx = cv2.approxPolyDP(contour, APPROXIMATION, False)

    if len(approx) < 2:
        continue
    path = []
    for point in approx:
        x = int(point[0][0])
        y = int(point[0][1])
        path.append((x, y))
    if len(path) >= 2:
        paths.append(path)

# ================ SORT DRAWING PATHS BY LENGTH ================
# Large/important lines first
paths.sort(
    key=lambda p: len(p),
    reverse=True
)

# ================ CREATE TURTLE ================
screen = turtle.Screen()
screen.title("❤️❤️❤️ Krishna ❤️❤️❤️")
screen.bgcolor("black")
screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

# ================ WINDOW ================
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()

root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width - WINDOW_WIDTH) / 2)
y = int((screen_height - WINDOW_HEIGHT) / 2)
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")
root.resizable(False, False)

# ================ CREATE TURTLE ================
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()
t.pensize(LINE_WIDTH)
t.pencolor(LINE_COLOR)

# ================ CALCULATE IMAGE SCALE ================
scale = min(DRAW_SIZE / original_width, DRAW_SIZE / original_height)
new_width = original_width * scale
new_height = original_height * scale

# ================ MOVING IMAGE CENTER TO CENTER ================
def image_to_turtle(x, y):
    turtle_x = ((x * scale) - (new_width / 2))
    turtle_y = ((new_height / 2) - (y * scale))
    return turtle_x, turtle_y

# ================ Animation ================
screen.tracer(0,0)
point_counter = 0

# ================ MAIN DRAWING LOOP ================
for path_number, path in enumerate(paths):
    if len(path) < 2:
        continue

    # ================ Move without drawing to beginning of line ================
    first_x, first_y = image_to_turtle(path[0][0], path[0][1])
    t.penup()
    t.goto(first_x, first_y)
    t.pendown()

    # ================ Draw line ================
    for i in range(1, len(path)):
        px = path[i][0]
        py = path[i][1]
        turtle_x, turtle_y = image_to_turtle(px, py)
        t.goto(turtle_x, turtle_y) # Draw one tiny section
        point_counter += 1
        if point_counter % UPDATE_EVERY == 0: # Update screen
            screen.update()
            time.sleep(DRAW_DELAY)
    t.penup() # separate lines
    screen.update()

# ================ FINISHED ================
screen.update()
print()
turtle.done()