x = 0.0
v = 1.0
dt = 0.5

t = 0.0        # start time (seconds)
t_end = 2.5    # end time (seconds)

while t < t_end:
    x = x + v * dt
    t = t + dt
    print("Time:", t, "Position x:", x)
