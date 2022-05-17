import numpy as np
import mdtraj as md
import itertools
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from matplotlib import rc
from matplotlib.colors import LinearSegmentedColormap
import warnings
warnings.filterwarnings("ignore")

from scipy.stats import gaussian_kde

rc('font',**{'style':'normal','size':8}) # 12
rc('axes',**{'titlesize':8})
rc('mathtext',**{'default':'regular'})
rc(('ytick'),**{'labelsize':6.5,'direction':'in','major.pad':2,'major.size':2})
rc(('xtick'),**{'labelsize':6.5,'direction':'in','major.pad':2,'major.size':2})
rc(('axes'),**{'labelsize':8,'labelpad':2,'linewidth':1}) # 10
rc(('legend'),**{'fontsize':8,'frameon':True,'labelspacing':0.5, 'handletextpad':0}) # 8

my_dpi = 300
left, width = 0.24, 0.75
bottom, height = 0.14, 0.75
rect = [left, bottom, width, height]

# main
states = [
            'TD',
            'DD',
            'MD',
          ]

vmin, vmax = 0, 0.20
xmin, xmax = 0.05, 0.45
ymin, ymax = -1600, -700

for s in states:
    fn = 'Fig5_data_%s.npz' % s
    data = np.load(fn)
    x, y, z = data['x'], data['y'], data['z']

    left, width = 0.26, 1.5/2.1
    bottom, height = 0.14, 0.75
    rect = [left, bottom, width, height]
    zmin, zmax = None, None

    fign = 'Fig5_%s.png' % s
    fig = plt.figure(figsize=(2.1, 2), dpi=my_dpi)
    ax = fig.add_axes(rect)
    cmap = 'viridis'
    density = ax.scatter(x, y, c=z, marker='x', label=s, lw=0.5, s=2, zorder=2,
                cmap=cmap, vmin=vmin, vmax=vmax)
    ax.set_ylabel('Total Contact Energy (REU)')
    ax.set_xlabel('RMSD (nm)')

    ax.set_xlim(xmin, xmax)
    ax.set_xticks(np.arange(xmin, xmax, 0.05), minor=True)

    ax.set_ylim(ymin, ymax)
    ax.set_yticks(np.arange(ymin, ymax, 200))
    ax.set_yticks(np.arange(ymin, ymax, 100), minor=True)

    ax.grid(which='major', axis='both', linestyle='-', lw=0.5)
    ax.grid(which='minor', axis='both', linestyle='--', lw=0.5)

    fig.text(left + width - 0.1,  bottom + 0.1, '%s' % s, fontsize=12,
             ha='right', va='bottom',
             bbox=dict(boxstyle='round',
                       ec='white',
                       fc='white',
                       )
             )

    print('save png:', fign)
    fig.savefig(fign)

# plot standalone colorbar
fig = plt.figure(figsize=(0.4, 2), dpi=my_dpi)
img = plt.imshow([[0, 1]], cmap='viridis', vmin=vmin, vmax=vmax)
plt.gca().set_visible(False)
cax = fig.add_axes([0.01, 0.2, 0.25, 0.6])
cbar = fig.colorbar(img, orientation="vertical", cax=cax,
                    ticks=np.linspace(vmin, vmax, 6))
cbar.ax.tick_params(width=0.5, labelsize=6)
fign = 'Fig5_colorbar.png'
print(fign)
fig.savefig(fign)
