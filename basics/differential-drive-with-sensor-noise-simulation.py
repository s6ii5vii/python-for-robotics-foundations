import math
import random

# initial state
x = 0.0
y = 0.0
theta = 0.0

# robot parameters
L = 0.5

# ideal wheel speeds
v_l_true = 0.6
v_r_true = 1.0

dt = 0.1
t = 0.0
t_end = 5.0

while t < t_end:

    # simulate sensor noise
    noise_l = random.uniform(-0.05, 0.05)
    noise_r = random.uniform(-0.05, 0.05)

    v_l_measured = v_l_true + noise_l
    v_r_measured = v_r_true + noise_r

    # convert to body velocities
    v = (v_r_measured + v_l_measured) / 2.0
    omega = (v_r_measured - v_l_measured) / L

    # update orientation
    theta = theta + omega * dt

    # update position
    x = x + v * math.cos(theta) * dt
    y = y + v * math.sin(theta) * dt

    t = t + dt

    print(f"t={t:.1f}s | x={x:.2f}, y={y:.2f}, theta={math.degrees(theta):.1f}")