import numpy as np
import time
import math

n = 3000
rng = np.random.default_rng()
x = rng.uniform(-5.0, 5.0, size=n)
y = rng.uniform(-5.0, 5.0, size=n)

soft = 0.5
softie = soft**2
softest = soft**3


start = time.perf_counter()
for i in range(n):
    for j in range(n):
        dist_x = x[j] - x[i]
        dist_y = y[j] - y[i]
        diag = math.sqrt(dist_x**2 + dist_y**2)
        r_dist = diag*diag*diag + softest

end = time.perf_counter()
print(end-start)
