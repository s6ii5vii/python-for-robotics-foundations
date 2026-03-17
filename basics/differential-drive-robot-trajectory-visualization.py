import math
import random
import matplotlib.pyplot as plt

#robot state
x = 0.0
y = 0.0
theta = 0.0

#robot parameters
L = 0.5

v_l_true = 0.6
v_r_true = 1.0
dt = 0.1
t = 0.0
t_end = 5.0

#store trajectory for visualization
trajectory_x = []
trajectory_y = []
while t < t_end:
    noise_l = random.uniform(-0.05, 0.05)
    noise_r = random.uniform(-0.05, 0.05)

    v_l_measured = v_l_true + noise_l
    v_r_measured = v_r_true + noise_r

    v = (v_r_measured + v_l_measured) / 2.0
    omega = (v_r_measured - v_l_measured) / L

    theta = theta + omega * dt
    x = x + v * math.cos(theta) * dt
    y = y + v * math.sin(theta) * dt

    trajectory_x.append(x)
    trajectory_y.append(y)

    t = t + dt



#visualize trajectory
plt.figure()
plt.plot(trajectory_x, trajectory_y, 'b-')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Differential Drive Robot Trajectory')
plt.grid(True)
plt.show()