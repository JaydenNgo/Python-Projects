import matplotlib.pyplot as plt
import math
import random
import matplotlib.animation as animation
import time
from IPython.display import clear_output, display

class Point:
    def __init__(self, x, y, dx=0, dy=0, mass=3):
        self.mass = mass

        self.x = x
        self.y = y

        self.dx = dx
        self.dy = dy

    def move_point(self, dt):
        self.x += self.dx * dt
        self.y += self.dy * dt

def dist_between(point1: Point, point2: Point):
    dist_x = point2.x - point1.x
    dist_y = point2.y - point1.y
    diag = math.sqrt(dist_x**2 + dist_y**2)

    return dist_x, dist_y, diag

def update_velocity(points, gravity=1, dt=1, soft=0.5):
    for point in points:
        ddx, ddy = 0, 0
        for other_point in points:
            dist_x, dist_y, full_dist = dist_between(point, other_point)
            r_dist = (full_dist**2 + soft**2) ** 1.5
            
            ratio = gravity * other_point.mass / r_dist

            ddx += dist_x * ratio
            ddy += dist_y * ratio

        point.dx += ddx * dt
        point.dy += ddy * dt

def update_position(points, dt):
    for point in points:
        point.move_point(dt)

def generate_point_data():
    return  random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1)/2, random.uniform(-1,1)/2, 1 #random.uniform(1,3)


# points = [Point(-1, 1,  0.1, 0),
#           Point(1,  1, 0,  0), 
#           Point(1, -1,  0,  0),
#           Point(-1,-1,  0,  0)
#           ]

points = [Point(*generate_point_data()) for i in range(500)]

plt.ion() 

fig, ax = plt.subplots(figsize=(6, 6))
# Pre-calculate masses if they don't change over time
masses = [15 * point.mass for point in points] 
  
my_dt = 0.05

n = 5
ax.set_xlim(-n, n)
ax.set_ylim(-n, n)
ax.grid(True, linestyle="--", alpha=0.5)
ax.set_xlabel("X Coordinate")
ax.set_ylabel("Y Coordinate")

# Initialize artists
x_init = [p.x for p in points]
y_init = [p.y for p in points]
dx_init = [p.dx for p in points]
dy_init = [p.dy for p in points]

scat = ax.scatter(x_init, y_init, s=masses, color="blue")
quiv = ax.quiver(x_init, y_init, dx_init, dy_init, 
                 angles='xy', scale_units='xy', scale=1, 
                 color='gray', alpha=0.3, width=0.005)
title = ax.set_title("Real-Time Gravity Simulation")

# --- Live Continuous Loop ---
start = time.perf_counter()

try:
    frame = 0
    while plt.fignum_exists(fig.number): # Runs until you close the plot window
        # 1. Physics Calculations
        update_velocity(points=points, gravity=1, dt=my_dt)
        
        x_old = [point.x for point in points]
        y_old = [point.y for point in points]
        dx = [point.dx for point in points]
        dy = [point.dy for point in points]
        
        update_position(points, my_dt)
        
        x_new = [point.x for point in points]
        y_new = [point.y for point in points]

        min_x, max_x = min(x_new), max(x_new)
        min_y, max_y = min(y_new), max(y_new)
        
        #Add padding (e.g., 20% extra space or a fixed buffer like 3.0 units)
        padding = 3.0
        ax.set_xlim(min_x - padding, max_x + padding)
        ax.set_ylim(min_y - padding, max_y + padding)

        # 2. Update the visual artists dynamically
        scat.set_offsets(list(zip(x_new, y_new)))
        quiv.set_offsets(list(zip(x_old, y_old)))
        quiv.set_UVC(dx, dy)
        end = time.perf_counter()

        title.set_text(f"Real-Time Gravity Simulation - Frame {frame}  \n{end-start:.3f}s")

        if not frame % 100:
            print(end-start)
        # 3. Redraw the canvas and flush GUI events instantly
        fig.canvas.draw()
        fig.canvas.flush_events()
        frame += 1

except KeyboardInterrupt:
    # Safely exit if interrupted
    pass
finally:
    plt.ioff() # Turn interactive mode off when finished