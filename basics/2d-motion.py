import math

x = 0.0
y = 0.0
theta = math.radians(45)

v = 1.0
dt = 0.5

t = 0.0
t_end = 2.5

while t < t_end :
    x = x + v * math.cos(theta) * dt
    y = y + v * math.sin(theta) * dt
    t = t + dt
    print(f"Time: {t:.1f} | x: {x:.2f}, y: {y:.2f}")




a = 0.0
b = 0.0
theta = math.radians(90)

v = 1.0
dt = 0.5

t = 0.0
t_end = 2.5

while t < t_end :
    a = a + v * math.cos(theta) * dt
    b = b + v * math.sin(theta) * dt
    t = t + dt
    print(f"Time: {t:.1f} | a: {a:.2f}, y: {b:.2f}")    




m = 0.0
n = 0.0
theta = math.radians(0)

v = 1.0
dt = 0.5

t = 0.0
t_end = 2.5

while t < t_end :
    m = m + v * math.cos(theta) * dt
    n = n + v * math.sin(theta) * dt
    t = t + dt
    print(f"Time: {t:.1f} | m: {m:.2f}, y: {n:.2f}")