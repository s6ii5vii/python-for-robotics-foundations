import math
import random
import matplotlib.pyplot as plt

# ideal robot state
x_ideal = 0.0
y_ideal = 0.0
theta_ideal = 0.0

# noisy robot state
x_noisy = 0.0
y_noisy = 0.0
theta_noisy = 0.0

# robot parameters
L = 0.5

# true wheel speeds
v_l_true = 0.6
v_r_true = 1.0

# simulation settings
dt = 0.1
t = 0.0
t_end = 10.0

# ideal trajectory storage
ideal_x = []
ideal_y = []

# noisy trajectory storage
noisy_x = []
noisy_y = []

while t < t_end:
        # ideal robot update
    v_ideal = (v_r_true + v_l_true) / 2.0
    omega_ideal = (v_r_true - v_l_true) / L

    theta_ideal = theta_ideal + omega_ideal * dt

    x_ideal = x_ideal + v_ideal * math.cos(theta_ideal) * dt
    y_ideal = y_ideal + v_ideal * math.sin(theta_ideal) * dt

    ideal_x.append(x_ideal)
    ideal_y.append(y_ideal)

        # noisy wheel measurements
    noise_l = random.uniform(-0.05, 0.05)
    noise_r = random.uniform(-0.05, 0.05)

    v_l_measured = v_l_true + noise_l
    v_r_measured = v_r_true + noise_r

        # noisy robot update
    v_noisy = (v_r_measured + v_l_measured) / 2.0
    omega_noisy = (v_r_measured - v_l_measured) / L

    theta_noisy = theta_noisy + omega_noisy * dt

    x_noisy = x_noisy + v_noisy * math.cos(theta_noisy) * dt
    y_noisy = y_noisy + v_noisy * math.sin(theta_noisy) * dt

    noisy_x.append(x_noisy)
    noisy_y.append(y_noisy)

        # update simulation time
    t = t + dt

# create plot
plt.figure(figsize=(8, 6))

plt.plot(ideal_x, ideal_y, label="ideal trajectory")
plt.plot(noisy_x, noisy_y, label="noisy trajectory")

# format plot
plt.xlabel("x position")
plt.ylabel("y position")
plt.title("ideal vs noisy robot trajectories")
plt.grid(True)
plt.axis("equal")
plt.legend()

plt.show()
