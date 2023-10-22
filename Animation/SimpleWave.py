import matplotlib.pyplot as mpl
import matplotlib.animation as man
import numpy as np
import math

''' BEGIN simple wave sin function animation '''
t = np.linspace(0, 10, 1000)
frequency_values = np.array((0., 30., 45., 60., 90.))
fig, ax = mpl.subplots(1, 1, figsize = (16, 9), dpi = 300)
ax.set_facecolor("black")
ax.axis(False)
fig.set_facecolor("black")
line, = ax.plot(t, np.sin(frequency_values[0] * t), lw=5, color = "white")
ax.set_ylim(-5, 5)

def animate(playhead):
    colors = ['r', 'g', 'b']
    mask = t <= playhead
    line.set_color(colors[0])
    line.set_dashes([1, 2, 3])
    line.set_data(t[mask], np.sin(4*t[mask]))

anim = man.FuncAnimation(fig, animate, t[::10], interval = 30)
mpl.show()
#anim.save("SimpleWave.mp4")

''' END simple wave sin function animation '''
########------------------------------------##########