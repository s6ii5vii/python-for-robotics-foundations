import math

x = 0.0 
y = 0.0


v = 1.0
omega = math.radians(30)
dt = 0.1


theta = 0.0


t = 0.0
t_end = 5.0


while t < t_end:
    theta = theta + omega * dt

    x = x + v * math.cos(theta) * dt
    y = y + v * math.sin(theta) * dt

    t = t + dt

    print(f"t = {t:.1f}s | x = {x:.2f}, y = {y:.2f}, theta = {math.degrees(theta):.1f}")