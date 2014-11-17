#!/usr/bin/env python
import pandas as pd
import numpy as np


fnames = {'Karate (Non-adaptive)': 'karate_hires.csv'
        , 'Karate (Adaptive)': 'karate_rahuls.csv'
        , 'Karate (Ours)': 'karate_vd.csv'
        , 'Solo (Non-adaptive)': 'solo_hires_1.csv'
        , 'Solo (Adaptive)': 'solo_rahuls_1.csv'
        , 'Solo (Ours)': 'solo_vd_1.csv'
        , 'Dancers (Non-adaptive)': ['solo_hires_1.csv'] * 10
        , 'Dancers (Adaptive)': ['solo_rahuls_1.csv'] * 5 + ['solo_rahuls_2.csv'] * 5
        , 'Dancers (Ours)': ['crowd_vd_%d.csv' % i for i in range(10)]
        }
cols_to_use = ['Faces', 'Verts', 'Time/Frame']
stats_to_use = ['min', 'max', 'mean']


def read_data(fnames):
    df = None
    if type(fnames) is list:
        for fname in fnames:
            df2 = pd.read_csv(fname, index_col='FrameNum'
                    , dtype={'Faces': np.int, 'Verts': np.int})
            if df is None:
                df = df2
                continue
            #import pdb; pdb.set_trace()
            df = df.add(df2, fill_value=0)
            #print df['Faces'][:10]
    else:
        df = pd.read_csv(fnames, index_col='FrameNum')
    return df[cols_to_use]


if __name__ == '__main__':
    dfs = []
    for fname in fnames.itervalues():
        dfs.append(read_data(fname))

    stats = []
    for df in dfs:
        desc = df.describe().loc[stats_to_use, :]
        desc.loc['sum', :] = df.sum()
        stats.append(desc)

    data_types = ['Karate', 'Solo', 'Dancers']
    data_names = fnames.keys()
    speed_ups = []
    for datum_name, datum in zip(data_names, stats):
        baseline = None
        for data_type in data_types:
            if datum_name.startswith(data_type):
                j = data_names.index(data_type + ' (Adaptive)')
                baseline = stats[j]
                break
        speed_ups.append(baseline['Time/Frame']['sum'] / datum['Time/Frame']['sum'])

    for i in xrange(len(stats)):
        stats[i] = stats[i].loc[stats_to_use, :].unstack()
        stats[i]['Speed-up'] = speed_ups[i]

    df = pd.DataFrame(stats, index=fnames.keys())
    df = df.sort_index(axis=0)
    df.rename(columns={'Verts': 'Num. Vertices', 'Faces': 'Num. Faces', 'Time/Frame':
        'Time / Frame (seconds)'}, inplace=True)

    def float_formatter(x):
        if False:
            x_int = int(round(x))
            return '{0:,d}'.format(x_int)

        x_int = int(x)
        if x == x_int:
            return '{0:,d}'.format(x_int)
        return '{0:,.2f}'.format(x)

    latex = df.to_latex(float_format=float_formatter)
    print df
    print latex

    with open('timings_raw.tex', 'w') as f:
        f.write(latex)
