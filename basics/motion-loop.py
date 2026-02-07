x = 0.0

v = 1.0     #velocity

dt = 0.5  #time step (seconds)


for step in range(5):
    
    x = x + v * dt 
    print("Step:", step, "Position x:", x)
