#!/usr/bin/env python
from matplotlib import rc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def read_time(fname):
    df = pd.read_csv(fname, index_col='FrameNum')
    return df['Time/Frame']


if __name__ == '__main__':
    ## for Palatino and other serif fonts use:
    rc('font', **{'family': 'serif', 'serif': ['Palatino']})
    rc('text', usetex=True)

    def w(x):
        if x >= 0.0:
            return max(0.0, 1.0 - (abs(x) / 5.0))
        return 0.0

    plt.grid()
    plt.axis([-5.5, 5.5, 0, 1.1])
    plt.xlabel(r'$\tau$')
    plt.ylabel(r'$w(\tau)$')

    x = np.linspace(0, 6, 7)
    y = map(w, x)
    plt.plot(x, y)
    plt.savefig('window_function.pdf', format='pdf')#, bbox_inches='tight', pad_inches=0.01)
    plt.show()

    rahuls = read_time('karate_rahuls.csv')
    vd = read_time('karate_vd.csv')

    df = pd.DataFrame({'Adpative': rahuls
        , 'Ours': vd
        , 'Adaptive (total)': rahuls.cumsum()
        , 'Ours (total)': vd.cumsum()})
    df.index.name = 'Frame'

    ax = df.plot(xlim=(df.first_valid_index(), df.last_valid_index()),
            secondary_y=['Adaptive (total)', 'Ours (total)'],
            linewidth=1,
            mark_right=False)
    ax.grid()
    ax.set_ylabel('Time / Frame (seconds)')
    ax.right_ax.set_ylabel('Total time (seconds)')
    ax.get_legend().get_frame().set_alpha(0.25)

    plt.savefig('timings.pdf', format='pdf', bbox_inches='tight', pad_inches=0.01)
    plt.show()
