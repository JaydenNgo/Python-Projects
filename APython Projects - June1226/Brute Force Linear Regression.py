import matplotlib.pyplot as plt
import numpy as np
import random

size = 5
points = []
num_points = 10

iterate = 0
while iterate < num_points:
  point = (random.random()*size,random.random()*size)
  if point in points:
    continue
  points.append(point)
  iterate += 1

x_values = [point[0] for point in points]
y_values = [point[1] for point in points]
#print(points)

margin = 10**5
goodA = 0
goodB = 0
steps = 100
# 1. Generate data points for the functions
func_x = np.linspace(-1, 1.5*size, 100)
for b in range(5):
  for a in range(-5*steps,5*steps):
    a /= steps
    
    func_y = a*func_x+b
    distances = [abs((a*p[0]+b)-p[1]) for p in points]
    total_loss = sum(distances)
    # print(f"{a}x+{b}:{total_loss}")
    if total_loss < margin:
      goodA = a
      goodB = b
      margin = total_loss
  
  
good_func = goodA*func_x+goodB
print(f"{goodA}x+{goodB}: {margin}")
# 2. Create the plot
fig, ax = plt.subplots() #
ax.plot(func_x, good_func, 'r-')
ax.scatter(x_values, y_values)
ax.grid(True)
plt.show()




