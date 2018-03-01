import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def data_gen(t=0):
    cnt = 0
    while cnt < 1000:
        cnt += 1
        t += 0.1  # Control the step-size here.
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)


def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 10)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata )
    return line,

fig, ax = plt.subplots()

# Add the title "Exponential Decay" here.
plt.title("Exponential Decay")

line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []

line2, = ax.plot([], [], lw=2)
ax.grid()
xdata2, ydata2= [], []


def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)

    t2, y2 = data
    xdata2.append(t2)
    ydata2.append(y2)


    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    # line.set_data(xdata, ydata)
    line.set_data(xdata, ydata);
    return line,

ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10,
                              repeat=False, init_func=init)

plt.show()