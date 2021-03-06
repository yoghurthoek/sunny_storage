import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.ticker as ticker
import os


def visualize(b, h, wijk, command, price=0):
    """
    Helper-algorithm that is needed to visualize grid configurations in
    a plot. Is only called when a configuration with the best price is found.
    """

    fig, ax = plt.subplots()

    colors = ["#1f78b4", "#e31a1c", "#ff7f00",  "gold", "#33a02c", "#fb9a99",
              "#fdbf6f", "#a6cee3", "#cab2d6", "#6a3d9a", "#ffff99", "#b15928",
              "black", "#b2df8a", "#B1A8A1", "FF0000", "FF00F9"]
    i = 0
    cmarker = Path([(-0.5, -0.5), (-0.5, 0.5), (0., 1.), (0.5, 0.5),
                    (0.5, -0.5), (-0.5, -0.5), ],
                   [Path.MOVETO, Path.LINETO, Path.LINETO,
                    Path.LINETO, Path.LINETO, Path.CLOSEPOLY, ])

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

    for k in h:
        if h[k].pluggedin is False:
            ax.plot(h[k].posx, h[k].posy, color='k', marker=cmarker,
                    markersize=15)

    ax.set_xlim((-1, 51))
    ax.set_ylim((-1, 51))

    minorspace = ticker.MultipleLocator()
    ax.xaxis.set_minor_locator(minorspace)
    ax.yaxis.set_minor_locator(minorspace)

    majorspace = ticker.MultipleLocator(10)
    ax.xaxis.set_major_locator(majorspace)
    ax.yaxis.set_major_locator(majorspace)

    ax.grid(b=True, which='major', linewidth=1.5)
    ax.grid(b=True, which='minor', linewidth=0.5)

    # Set title
    fig.suptitle(f"Wijk{wijk}_{command}")
    if price != 0:
        ax.set_title(f"Price: {price}")

    output = os.path.dirname(os.getcwd(
        ))+f"\\sunny_storage\\Output_Data\\bestwijk{wijk}_{command}.png"
    plt.savefig(output)
    plt.show()
