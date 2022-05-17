import numpy as np
import itertools
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import ticker, cm

plt.rcParams.update({'text.usetex':False})
rc('font',**{'style':'normal','size':8,'family':'sans-serif','sans-serif':['DejaVu Sans']})
rc('axes',**{'titlesize':8})
rc('mathtext',**{'default':'regular'})
rc(('xtick','ytick'),**{'labelsize':6,'direction':'in','major.pad':1})
rc(('axes'),**{'labelsize':8,'labelpad':1,'linewidth':1})
rc(('legend'),**{'fontsize':6,'frameon':False})

my_dpi=300
rect=[0.15,0.15,0.75*2.5/2.25,0.75]

for figi in ['A', 'B']:
    fn='Fig2%s_data.npz' % figi
    fign='Fig2%s.png' % figi
    data=np.load(fn)
    X, Y, z = data['X'], data['Y'], data['z']

    fig = plt.figure(figsize=(2.25,2),dpi=my_dpi)
    ax=fig.add_axes(rect)

    ax.set_xlabel('$R_{LID \u2010 CORE}(\AA)$')
    ax.set_ylabel('$R_{NMP \u2010 CORE}(\AA)$')

    ax.set_xlim([19,37])
    ax.set_ylim([17,25])
    ax.set_xticks([20,25,30,35])
    ax.set_yticks([18,20,22,24])

    vmin=0
    vmax=12
    levels=np.arange(vmin,vmax+0.5,step=1)

    cs = ax.contour(X,Y,z,vmin = vmin, vmax = vmax, levels=levels, colors='k', linestyles='-', linewidths=0.1)
    cntr = ax.contourf(X,Y,z,vmin = vmin, vmax = vmax, levels=levels, cmap=cm.RdYlBu_r)
    cbar = fig.colorbar(cntr,ax=ax,shrink=0.8, anchor=(0,0.2))
    cbar.ax.tick_params(axis='y', direction='out')

    fig.text(0.85,0.82,'$k_B T$',fontsize=8)
    fig.savefig(fign,dpi=my_dpi)
