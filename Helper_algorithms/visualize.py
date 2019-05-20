import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.ticker as ticker
import os


def visualize(b, h, wijk, command):
    fig, ax = plt.subplots()

    # Use different colors depending on battery connection
    colors = ["r", "b", "g", "gold", "m"]
    i = 0
    cmarker = Path([(-0.5, -0.5), (-0.5, 0.5), (0., 1.), (0.5, 0.5),
                    (0.5, -0.5), (-0.5, -0.5), ],
                   [Path.MOVETO, Path.LINETO, Path.LINETO,
                    Path.LINETO, Path.LINETO, Path.CLOSEPOLY, ])

    # Plot battery and connected houses, then go to next battery
    for k in b:
        ax.plot(b[k].posx, b[k].posy, color=colors[i],
                marker='P', markersize=10, markeredgecolor='k')
        for house in b[k].connected:
            ax.plot(house.posx, house.posy, color=colors[i],
                    marker=cmarker, markersize=10)
            ax.plot([b[k].posx, b[k].posx], [b[k].posy, house.posy],
                    color=colors[i], linestyle='-', linewidth=1)
            ax.plot([b[k].posx, house.posx], [house.posy, house.posy],
                    color=colors[i], linestyle='-', linewidth=1)
        i += 1

    # Plot unconnected houses if they are there
    for k in h:
        if h[k].pluggedin is False:
            ax.plot(h[k].posx, h[k].posy, color='k', marker=cmarker,
                    markersize=15)

    # Set grid limits
    ax.set_xlim((-1, 51))
    ax.set_ylim((-1, 51))

    # Set ticks for minor gridlines
    minorspace = ticker.MultipleLocator()
    ax.xaxis.set_minor_locator(minorspace)
    ax.yaxis.set_minor_locator(minorspace)

    # Set ticks for major gridlines
    majorspace = ticker.MultipleLocator(10)
    ax.xaxis.set_major_locator(majorspace)
    ax.yaxis.set_major_locator(majorspace)

    # Draw in gridlines
    ax.grid(b=True, which='major', linewidth=1.5)
    ax.grid(b=True, which='minor', linewidth=0.5)

    output = os.path.dirname(os.getcwd())+f"\\sunny_storage\\Output_Data\\bestwijk{wijk}_{command}.png"
    plt.savefig(output)
    plt.show()
