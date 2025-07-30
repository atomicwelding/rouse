# Simulation of the Rouse model for 2AG
# By Erwan Le Doeuff (weld)
from parameters import *
from viewer import animate
import numpy as np

# shortcut
X = 0
VX = X
Y = 1
VY = Y
Z = 2
VZ = Z

if __name__ == "__main__":
    pos  = np.zeros((timesteps, N, 3))

    for n in range(N):
        pos[:, n, X] = box_size / 2 + b * (n - N/2) * 3  # stretched config
        pos[:, n, Y] = box_size / 2
        pos[:, n, Z] = box_size / 2
    
    # dynamics
    for t in range(timesteps-1):
        for n in range(N):
            F = np.zeros(3)
            if n > 0:
                F += -k/zeta * (pos[t, n] - pos[t, n - 1])
            if n < N - 1:
                F += -k/zeta * (pos[t, n] - pos[t, n + 1])


            F += np.random.normal(0, sigma, size=3) # a revoir

            pos[t+1, n] = pos[t, n] + F * dt
            pos[t+1, n] %= box_size # pbc
            
    animate(pos)
