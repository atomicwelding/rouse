from parameters import *

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def animate(pos, step=5, interval=40):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    sc, = ax.plot([], [], [], 'o-', color="k", lw=2)

    ax.set_xlim(0, box_size)
    ax.set_ylim(0, box_size)
    ax.set_zlim(0, box_size)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    def update(frame):
        data = pos[frame]
        sc.set_data(data[:, 0], data[:, 1])
        sc.set_3d_properties(data[:, 2])
        return sc,

    ani = FuncAnimation(fig, update, frames=range(0, timesteps, step), interval=interval, blit=True)
    plt.show()
