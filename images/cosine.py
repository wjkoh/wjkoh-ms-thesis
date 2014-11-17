#!/usr/bin/env python
"""
    http://www.loria.fr/~rougier/teaching/matplotlib/
"""
from pylab import *  # Import everything from matplotlib (numpy is accessible via 'np' alias)
from matplotlib import rc

## for Palatino and other serif fonts use:
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)


# Constants
k_cos = 0.2


def widehat_cos(xs):
    def cos(x):
        y = np.cos(x)
        if y < 0:
            return k_cos * (y + 1.0)
        return k_cos + (1.0 - k_cos) * y
    return [cos(x) for x in xs]


if __name__ == '__main__':
    # Create a new figure of size 8x6 points, using 80 dots per inch
    figure(figsize=(8, 6), dpi=80)

    # Create a new subplot from a grid of 1x1
    subplot(1,1,1)

    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C, C_ = np.cos(X), widehat_cos(X)

    # Plot cosine using blue color with a continuous line of width 1 (pixels)
    plot(X, C, color="blue", linewidth=2.5, linestyle="-", label=r'$\cos\theta$')

    # Plot sine using green color with a continuous line of width 1 (pixels)
    plot(X, C_, color="red",  linewidth=2.5, linestyle="-", label=r'$\widehat{\cos}(\theta)$')

    # Guidelines
    t = np.pi/2
    plot([0, t],[k_cos, k_cos], color ='red', linewidth=2.5, linestyle="--")
    scatter([t],[k_cos], 50, color ='red')
    plot([t,t],[0, k_cos], color ='red', linewidth=2.5, linestyle="--")

    legend(loc='upper right')

    ax = gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))

    # Set x limits
    xlim(-0.15, X.max()*1.1)

    # Set x ticks
    xticks([0, np.pi/2, np.pi],
    [r'$0$', r'$\pi/2$', r'$\pi$'])

    # Set y limits
    ylim(C.min()*1.1, C.max()*1.1)

    # Set y ticks
    yticks([-1, k_cos, +1], [r'$-1$', r'$%s$' % k_cos,r'$+1$'])

    # Save figure using 72 dots per inch
    # Don't know why but eps looks better than pdf when printed.
    savefig("cosine.eps")

    # Show result on screen
    show()
