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

    def remove_slice(self, index: int|list):
        self.x = np.delete(self.x, index)
        self.y = np.delete(self.y, index)
        self.dx = np.delete(self.dx, index)
        self.dy = np.delete(self.dy, index)
        self.mass = np.delete(self.mass, index)

        self.n -= 1
        self.traingle_coord = np.triu_indices(self.n, k=1)


    def update_velocity(self):
        # Adjust subtraction order to match your dist_between(i, j) sign
        dist_x = self.x[None, :] - self.x[:, None]
        dist_y = self.y[None, :] - self.y[:, None]

        r_dist = np.square(dist_x) + np.square(dist_y) + self.soft2
        r_dist = r_dist * np.sqrt(r_dist)
        

        ratio = self.mass[None, :] / r_dist

        self.dx += np.sum(dist_x * ratio, axis=1) * self.gravity
        self.dy += np.sum(dist_y * ratio, axis=1) * self.gravity


    def update_position(self):
        self.x += self.dx * self.dt
        self.y += self.dy * self.dt
        self.collision()

    def collide(self, p1: int, p2: int):
        mass1, mass2 = self.mass[p1], self.mass[p2]
        
        # Determine winner and loser based on mass (or speed if tied)
        if mass1 > mass2:
            winner, loser = p1, p2
        elif mass1 < mass2:
            winner, loser = p2, p1
        else:
            p1_speed = math.sqrt(self.dx[p1]**2 + self.dy[p1]**2)
            p2_speed = math.sqrt(self.dx[p2]**2 + self.dy[p2]**2)
            winner, loser = (p1, p2) if p1_speed >= p2_speed else (p2, p1)

        # --- CONSERVE MOMENTUM & ADD MASS ---
        mw = self.mass[winner]
        ml = self.mass[loser]
        total_mass = mw + ml

        # New velocity = weighted average based on momentum
        self.dx[winner] = (self.dx[winner] * mw + self.dx[loser] * ml) / total_mass
        self.dy[winner] = (self.dy[winner] * mw + self.dy[loser] * ml) / total_mass
        
        # Winner absorbs the loser's mass
        self.mass[winner] = total_mass
        
        return loser

    def collision(self):
        dist_x = self.x[None, :] - self.x[:, None]
        dist_y = self.y[None, :] - self.y[:, None]
        
        to_remove = set()
        
        for p1, p2 in zip(*self.traingle_coord):
            if p1 in to_remove or p2 in to_remove:
                continue
                
            dist_sq = dist_x[p1][p2]**2 + dist_y[p1][p2]**2
            
            radius = 0.01
            r1 = radius * math.sqrt(self.mass[p1])
            r2 = radius * math.sqrt(self.mass[p2])
            # (R * (mass1+mass2))**2
            # R^2 = (sqrt(m1)+sqrt)
            collision_dist = radius * (r1 + r2) ** 2
            
            if dist_sq < collision_dist:
                print(f"Points {p1} and {p2} have collided")
                loser = self.collide(p1, p2)
                to_remove.add(loser)
        
        if len(to_remove):
            for index in sorted(list(to_remove), reverse=True):
                self.remove_slice(index)

    # def collide(self, p1: int, p2: int):
    #     mass1, mass2 = self.mass[p1], self.mass[p2]
    #     # remove smaller mass
    #     if mass1 > mass2:
    #         return p2   
    #     elif mass1 < mass2:
    #         return p1
    #     else:
    #         # remove slower one
    #         p1_velocity = self.dx[p1] + self.dy[p1]
    #         p2_velocity = self.dx[p2] + self.dy[p2]
    #         return p1 if p1_velocity < p2_velocity else p2
    
    # def collision(self):
    #     dist_x = self.x[None, :] - self.x[:, None]
    #     dist_y = self.y[None, :] - self.y[:, None]
    #     collision_dist = 0.1
    #     for p1, p2 in zip(*self.traingle_coord):
    #         x_dist, y_dist = abs(dist_x[p1][p2]), abs(dist_y[p1][p2])
    #         if  x_dist < collision_dist and y_dist < collision_dist:
    #             print(f"Points {p1} and {p2} have collided")
    #             self.remove_slice(self.collide(p1, p2))

    def apply_central_gravity(self):
        if not self.center:
            return
        
        r2 = np.square(self.x) + np.square(self.y) + self.soft2
        r_dist = r2 * np.sqrt(r2)  # r^3 in denominator
        
        dir_x = -self.x
        dir_y = -self.y
        
        # 3. Compute acceleration ratio
        ratio = self.center_mass / r_dist
        
        # 4. Apply to velocity (or displacement)
        self.dx += dir_x * ratio * self.dt
        self.dy += dir_y * ratio * self.dt
    


def generate_points(n):
    rng = np.random.default_rng()
    x = rng.uniform(-1.0, 1.0, size=n) * 1
    y = rng.uniform(-1.0, 1.0, size=n) * 1
    dx = rng.uniform(-1.0, 1.0, size=n) / 5
    dy = rng.uniform(-1.0, 1.0, size=n) / 5
    mass = rng.uniform(-1.0, 1.0, size=n) ** 0
    return n, x, y, dx, dy, mass

# points = Points(n=3,
#                 x=[-1, 0, 1],
#                 y=[1, -1, 1],
#                 dx=[0, 1, -1],
#                 dy=[-1, 0, 0],
#                 mass=[1,1,1]
#                 )


num_points = 15
points = Points(*generate_points(num_points))
points.set_settings(dt=0.05, gravity=1, soft=0.05, center=None)













#---------------------------------------------------------------------
plt.ion() 
fig, ax = plt.subplots(figsize=(6, 6))
# Pre-calculate masses if they don't change over time

n = 3
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

dislay_masses = 20 * points.mass
# three_color = ['red', 'blue', 'green']
# colors = [random.choice(three_color)
#           for _ in range(points.n)]

scat = ax.scatter(x_init, y_init, s=dislay_masses, color="blue")
ax.scatter(0, 0, color='black', marker='X', s=10)

quiv = ax.quiver(x_init, y_init, dx_init, dy_init, 
                 angles='xy', scale_units='xy', scale=1, 
                 color='gray', alpha=0.3, width=0.003)
title = ax.set_title("Real-Time Gravity Simulation")


# --- Live Continuous Loop ---
start = time.perf_counter()

try:
    frame = 0
    while plt.fignum_exists(fig.number):
        
        # Keep track of how many points we had before physics update
        old_n = points.n

        # 1. Physics Calculations (collisions happen inside update_velocity)
        points.update_velocity()
        points.apply_central_gravity()
        
        x_old = points.x 
        y_old = points.y 
        
        points.update_position()
        
        x_new = points.x 
        y_new = points.y 

        # --- CHECK IF A COLLISION OCCURRED ---
        if points.n != old_n:
            # Trim or recreate your color array to match the new point count
            #colors = [random.choice(three_color) for _ in range(points.n)]
            display_masses = 20 * points.mass
            
            # Remove old artists from the axis so they don't ghost
            scat.remove()
            quiv.remove()

            scat = ax.scatter(x_new, y_new, s=display_masses, color="blue")
            quiv = ax.quiver(x_new, y_new, points.dx, points.dy, 
                             angles='xy', scale_units='xy', scale=1, 
                             color='gray', alpha=0.3, width=0.003)
        else:
            # Normal update when no collision happened
            scat.set_offsets(list(zip(x_new, y_new)))
            quiv.set_offsets(list(zip(x_old, y_old)))
            quiv.set_UVC(points.dx, points.dy)

        # Dynamic axis scaling
        min_x, max_x = np.min(x_new), np.max(x_new)
        min_y, max_y = np.min(y_new), np.max(y_new)
        padding = 3.0
        ax.set_xlim(min_x - padding, max_x + padding)
        ax.set_ylim(min_y - padding, max_y + padding)

        end = time.perf_counter()
        t_time = end - start
        title.set_text(f"Real-Time Gravity Simulation - Frame {frame} (Particles: {points.n})\n{t_time:.3f}s\nAvg fps {frame/t_time:.1f}")

        fig.canvas.draw()
        #input()
        fig.canvas.flush_events()
        frame += 1

except KeyboardInterrupt:
    pass
finally:
    plt.ioff()