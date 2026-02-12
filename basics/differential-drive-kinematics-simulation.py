import math

x = 0.0
y = 0.0
theta = 0.0

# differential drive parameters
L = 0.5          # wheelbase distance between wheels
v_l = 0.6        # left wheel speed (m/s)
v_r = 1.0        # right wheel speed (m/s)

dt = 0.1
t = 0.0
t_end = 5.0

while t < t_end:
    # convert wheel speeds -> body velocities
    v = (v_r + v_l) / 2.0
    omega = (v_r - v_l) / L

    # update orientation
    theta = theta + omega * dt

    # update position (move forward in heading)
    x = x + v * math.cos(theta) * dt
    y = y + v * math.sin(theta) * dt

    t = t + dt
    print(f"t={t:.1f}s | x={x:.2f}, y={y:.2f}, theta_deg={math.degrees(theta):.1f}, v={v:.2f}, omega={omega:.2f}")

