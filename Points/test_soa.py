import matplotlib.pyplot as plt
import numpy as np
import math
import random
import matplotlib.animation as animation
import time
from IPython.display import clear_output, display

"""

• Eliminating full_dist: If self.dist_between(i, j) computes a square root (math.sqrt(dist_x**2 + dist_y**2)) only for you to square full_dist back on the next line, you can skip the square root entirely. Computing r_dist = (dist_x**2 + dist_y**2 + softie) ** 1.5 directly saves N² square root calls.
• Self-Interaction Check: When i == j, dist_x and dist_y are both 0, so ddx and ddy add 0 and the math remains safe (provided soft > 0 so you don't divide by zero). Skipping i == j avoids doing useless math for self-pairs.
• Symmetry (Newton's Third Law): Because the force of j on i is equal and opposite to the force of i on j, you only need to calculate each pair once (for j in range(i + 1, self.n)). This cuts the inner loop iterations in half.

"""
class Points:
    def __init__(self, n, x, y, dx=0, dy=0, mass=3):
        self.n= n
        self.mass = np.asarray(mass, dtype=np.float64)

        self.x = np.asarray(x, dtype=np.float64)
        self.y = np.asarray(y, dtype=np.float64)

        self.dx = np.asarray(dx, dtype=np.float64)
        self.dy = np.asarray(dy, dtype=np.float64)
        self.traingle_coord = np.triu_indices(n, k=1)

    def set_settings(self, dt=0.1, gravity=1, soft=0.5, center=None):
        self.gravity = gravity * dt
        self.dt = dt
        self.soft2 = soft**2
        self.center = center
        self.center_mass = center * gravity if center else None

    def update_velocity(self):
        # Adjust subtraction order to match your dist_between(i, j) sign
        dist_x = self.x[None, :] - self.x[:, None]
        dist_y = self.y[None, :] - self.y[:, None]

        collision_dist = 0.1
        for p1, p2 in zip(*self.traingle_coord):
            x_dist, y_dist = abs(dist_x[p1][p2]), abs(dist_y[p1][p2])
            if  x_dist < collision_dist and y_dist < collision_dist:
                print(f"Points {p1} and {p2} have collided")

        r_dist = np.square(dist_x) + np.square(dist_y) + self.soft2
        r_dist = r_dist * np.sqrt(r_dist)
        

        ratio = self.mass[None, :] / r_dist

        self.dx += np.sum(dist_x * ratio, axis=1) * self.gravity
        self.dy += np.sum(dist_y * ratio, axis=1) * self.gravity


    def update_position(self):
        self.x += self.dx * self.dt
        self.y += self.dy * self.dt

    def apply_central_gravity(self):
        if not self.center:
            return
        
        r2 = np.square(self.x) + np.square(self.y) + self.soft2
        r_dist = r2 / np.sqrt(r2)  # r^3 in denominator
        
        dir_x = -self.x
        dir_y = -self.y
        
        # 3. Compute acceleration ratio
        ratio = self.center_mass / r_dist
        
        # 4. Apply to velocity (or displacement)
        self.dx += dir_x * ratio * self.dt
        self.dy += dir_y * ratio * self.dt
    


def generate_points(n):
    rng = np.random.default_rng()
    x = rng.uniform(-1.0, 1.0, size=n)
    y = rng.uniform(-1.0, 1.0, size=n)
    dx = rng.uniform(-1.0, 1.0, size=n) / 10
    dy = rng.uniform(-1.0, 1.0, size=n) / 10
    mass = rng.uniform(1.0, 1.0, size=n)
    return n, x, y, dx, dy, mass

# points = Points(n=3,
#                 x=[-1, 0, 1],
#                 y=[1, -1, 1],
#                 dx=[0, 1, -1],
#                 dy=[-1, 0, 0],
#                 mass=[1,1,1]
#                 )


num_points = 10
points = Points(*generate_points(num_points))
points.set_settings(dt=0.025, gravity=3, soft=0.25, center=1)













#---------------------------------------------------------------------
plt.ion() 
fig, ax = plt.subplots(figsize=(6, 6))
# Pre-calculate masses if they don't change over time

n = 10
ax.set_xlim(-n, n)
ax.set_ylim(-n, n)
ax.grid(True, linestyle="--", alpha=0.5)
ax.set_xlabel("X Coordinate")
ax.set_ylabel("Y Coordinate")

# Initialize artists
x_init = points.x 
y_init = points.y 
dx_init = points.dx 
dy_init = points.dy 

dislay_masses = [20 for _ in range(points.n)]
three_color = ['red', 'blue', 'green']
colors = [random.choice(three_color)
          for _ in range(points.n)]

scat = ax.scatter(x_init, y_init, s=dislay_masses, c=colors)
ax.scatter(0, 0, color='black', marker='X', s=10)

quiv = ax.quiver(x_init, y_init, dx_init, dy_init, 
                 angles='xy', scale_units='xy', scale=1, 
                 color='gray', alpha=0.3, width=0.003)
title = ax.set_title("Real-Time Gravity Simulation")

# --- Live Continuous Loop ---
start = time.perf_counter()

try:
    frame = 0
    while plt.fignum_exists(fig.number): # Runs until you close the plot window
        # 1. Physics Calculations
        points.update_velocity()
        points.apply_central_gravity()
        
        x_old = points.x 
        y_old = points.y 
        
        points.update_position()
        
        x_new = points.x 
        y_new = points.y 

        min_x, max_x = np.min(x_new), np.max(x_new)
        min_y, max_y = np.min(y_new), np.max(y_new)
        
        #Add padding (e.g., 20% extra space or a fixed buffer like 3.0 units)
        padding = 3.0
        ax.set_xlim(min_x - padding, max_x + padding)
        ax.set_ylim(min_y - padding, max_y + padding)

        # 2. Update the visual artists dynamically
        scat.set_offsets(list(zip(x_new, y_new)))
        quiv.set_offsets(list(zip(x_old, y_old)))
        quiv.set_UVC(points.dx , points.dy)
        end = time.perf_counter()
        t_time = end-start
        title.set_text(f"""Real-Time Gravity Simulation - Frame {frame}\n {t_time:.3f}s\n Avg fps {frame/t_time:.1f}""")

        # if not frame % 100:
        #     print(end-start)
        # 3. Redraw the canvas and flush GUI events instantly
        fig.canvas.draw()
        #input()
        fig.canvas.flush_events()
        frame += 1

except KeyboardInterrupt:
    # Safely exit if interrupted
    pass
finally:
    plt.ioff() # Turn interactive mode off when finished