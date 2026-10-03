import turtle
import cv2
import numpy as np
import time
import os
            
# ========================SETTINGS====================================
IMAGE_FILE = "Radha.png"
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 790
DRAW_SIZE = 820
DRAW_DELAY = 0.005
UPDATE_EVERY = 1
LINE_WIDTH = 2.1
LINE_COLOR = "#00CFFF"
MIN_CONTOUR_LENGTH = 8  # Minimum contour size
APPROXIMATION = 0.5  # Smaller value = more image detail

# =============IMAGE LOADING===============================
if not os.path.exists(IMAGE_FILE):
    print("ERROR: IMAGE FILE NOT FOUND.\nYour image file must be named as Radha.png")
    print("Press Enter to close...")
    raise SystemExit 

image = cv2.imread(IMAGE_FILE)

if image is None:
    print("ERROR: COULD NOT OPEN IMAGE")
    input("Press Enter to close...")
    raise SystemExit
original_height, original_width = image.shape[:2]

# ===========CREATE COLOR MASK=========================
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_cyan = np.array([75, 40, 40])
upper_cyan = np.array([125, 255, 255])
mask = cv2.inRange(hsv, lower_cyan, upper_cyan)

# ===========REMOVE SMALL NOISE=============================
kernel = np.ones((2, 2), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)  #FIND CONTOURS
               
# =====================PREPARE DRAWING PATHS=================
paths = []
for contour in contours:
    length = cv2.arcLength(contour, False)
    if length < MIN_CONTOUR_LENGTH:
        continue
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

# ===============SORT PATHS BY LENGTH =======================
paths.sort(
    key=lambda p: len(p),
    reverse=True
)
    
# ============ TURTLE WINDOW====================
screen = turtle.Screen()
screen.title("Radha")
screen.bgcolor("black")
screen.setup( width = WINDOW_WIDTH, height = WINDOW_HEIGHT)

# ===========CENTER THE WINDOW===================================
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_x = int((screen_width - WINDOW_WIDTH) / 2)
window_y = int((screen_height - WINDOW_HEIGHT) / 2)
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{window_x}+{window_y}")
root.resizable(False, False)
 
# ===============CREATE TURTLE=============================
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()
t.pensize(LINE_WIDTH)
t.pencolor(LINE_COLOR)
  
# =============CALCULATE IMAGE SCALE========================
scale = min(
    DRAW_SIZE / original_width,
    DRAW_SIZE / original_height
)
new_width = original_width * scale
new_height = original_height * scale
             
# ===========CONVERT IMAGE TO TURTLE==================
def image_to_turtle(x, y):
    turtle_x = ((x * scale) - (new_width / 2))
    turtle_y = ((new_height / 2) - (y * scale))
    return turtle_x, turtle_y
screen.tracer(0, 0)  #DRAWING ANIMATION
point_counter = 0

# =============MAIN DRAWING LOOP========================
for path_number, path in enumerate(paths):
    if len(path) < 2:
        continue
    first_x, first_y = image_to_turtle(path[0][0],path[0][1])
    t.penup()
    t.goto(first_x, first_y)
    t.pendown()

    for i in range(1, len(path)):  # Draw every point in the path
        px = path[i][0]
        py = path[i][1]
        turtle_x, turtle_y = image_to_turtle(px, py)
        t.goto(turtle_x, turtle_y)
        point_counter += 1
        if point_counter % UPDATE_EVERY == 0:
            screen.update()
            time.sleep(DRAW_DELAY)
    t.penup()
    screen.update()
screen.update()
turtle.done()