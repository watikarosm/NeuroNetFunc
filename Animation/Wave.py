import matplotlib.pyplot as mpl
import matplotlib.animation as man
import numpy as np

''' BEGIN simple wave sin function animation '''
t = np.linspace(0, 10, 1000)
frequency_values = []

fig, ax = mpl.subplots(1, 1, figsize = (16, 9), dpi = 300)
ax.set_facecolor("black")
ax.axis(False)
fig.set_facecolor("black")
line = ax.plot(t, np.sin(frequency_values[0] * t, lw = 5, color = "white"))
ax.set_ylim(-5, 5)

def animate(playhead):
    mask = t <= playhead
    line.set_data(t[mask], np.sin(4*t[mask]))

anim = man.FuncAnimation(fig, animate, t[::10], interval = 30)
anim.save("SimpleWave.mp4")

''' END simple wave sin function animation '''
########------------------------------------##########
''' BEGIN wave sin with gradient color animation '''

def get_wave_with_variable_frequency(time, freq_array):
    ''' Returns an array sin(f(t)*t) '''
    dt = np.full_like(time, time[1] - time[0])
    phases = (freq_array * 2 * np.pi * dt).cumsum()
    return np.sin(phases), ((phases + np.pi) % (2 * np.pi) - np.pi)

N_points = 5000
t_start = 0
t_end = 5

time = np.linspace(t_start, t_end, N_points)    # Array of time points

# Generating a random frequency modulation patern
generator = np.random.default_rng(seed=322)
x_samples = np.linspace(t_start, t_end, 10)
freq_examples = generator.random(x_samples.shape) *6
interpolation = interpld(x_samples, freq_examples, kind='quadratic')

freq = interpolation(time)  # Array of frequencies (instantaneous rotation velocities)
wave, phase = get_wave_with_variable_frequency(time, freq) # Arrays containing the points of sinusoid and their phases

def setup_time_axes():
    # Setup a black Figure and Axes
    fig, ax = mpl.subplots(1, 1, figsize = (20, 4), dpi = 300)
    fig.set_facecolor("black")
    ax.set_facecolor("black")
    ax.set_xlim(t_start - 0.1, t_end + 0.1)
    ax.set_ylim(-1.1, 1.1)
    ax.grid(color = 'white', linewidth = 0.4, alpha = 0.3, zorder = 0)
    return fig, ax

phase_cmap = sns.color_palette("hls", as_cmap = True)   # Periodic color map to turn angles into colors

def angle2color(angle):
    return phase_cmap((angle % (2 * np.pi)) / (2 * np.pi))

fig, ax = setup_time_axes()

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[:1]], axis=1)    # Segments for LineCollection
lc = mpl.collections.LineCollection(segments, linewidth = 0)
lc.set_colors(angle2color(phase[:-1]))
lc.set_capstyle("round")
ax.add_collection(lc)

# Creating LineCollection
lc = mpl.collections.LineCollection(segments, linewidths = 6)
lc.set_colors(angle2color(phase[:-1]))
lc.set_capstyle("round")
ax.add_collection(lc)

#   Animation function
def animate_wave(t_current):
    lc.set_alpha(time <= t_current)
    return lc

#   Animation class via FuncAnimation
animWaveColorGradient = man.FuncAnimation(
    fig, animate_wave,
    frames = np.linspace(t_start, t_end, 5000),
    interval = 30
)

animWaveColorGradient.save("Wave.mp4")

''' END wave sin with color gradient animation '''
########------------------------------------##########
''' BEGIN wave sin with the under the curve is shaded '''

fig, ax = setup_time_axes() # Simlar code for the setting up figure and axis

lc = mpl.collections.LineCollection(make_segments(time, freq))
lc.set_colors("White")
fill = ax.fill_between(time, 0, freq, color = "white", alpha = 0.2)

def animate_frequency_with_fill(t_current):
    lc.set_alpha(time <= t_current) # Drawing curve
    ax.collections.clear()  # Removing old fill
    ax.add_collectin(lc)

# --- Creating new fill in specified limits (masked array)
    time_masked = np.ma.masked_where(time > t_current, time)
    freq_masked = np.ma.masked_where(time > t_current, freq)
    fill = ax.fill_between(
        time_masked, 0, freq_masked,
        color = "white",
        alpha = 0.2
    )
    return lc, fill
# Constructor
animWaveShadedUnderCurve = mpl.animation.FuncAnimation(
    fig, 
    animate_frequency_with_fill,
    frames = time,
    interval = 30
)

animWaveShadedUnderCurve.save("FrequencyFilledGraph.mp4")