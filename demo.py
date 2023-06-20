import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from figure_eight import FigureEight

fig8 = FigureEight(1.0, 0.5, 1.0, 2.0)

fig, ax = plt.subplots(layout="constrained")
(pt,) = ax.plot([], [], "ro", zorder=2)
(ln,) = ax.plot([], [], "-b", zorder=1)

line = []


def init():
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    return (pt, ln)


def update(t):
    print(f"percentage={t*100.0:.1f}%")

    global line
    pos = fig8.position(t).tolist().copy()
    line.append(pos)
    xdata = [pos[0]]
    ydata = [pos[1]]
    pt.set_data(xdata, ydata)

    ln.set_data([p[0] for p in line], [p[1] for p in line])
    return (pt, ln)


ani = FuncAnimation(
    fig, update, frames=np.linspace(0, 1.0, 100), init_func=init, blit=True
)
plt.show()
