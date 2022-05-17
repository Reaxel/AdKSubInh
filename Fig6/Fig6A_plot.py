import numpy as np
import itertools
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib import rc
from matplotlib import ticker, cm

rc('font',**{'style':'normal','size':8})
rc('axes',**{'titlesize':8})
rc('mathtext',**{'default':'regular'})
rc(('xtick','ytick'),**{'labelsize':6,'direction':'in','major.pad':1})
rc(('axes'),**{'labelsize':8,'labelpad':1,'linewidth':1})
rc(('legend'),**{'fontsize':6,'frameon':False,'handlelength':1.8,'markerscale':1.0})

my_dpi=300
rect=[0.22,0.15,0.75,0.75]

atp=1000
amp=[
     200,
     44,
     1000
     ]

colors=plt.rcParams['axes.prop_cycle'].by_key()['color']
colordict = dict(zip(amp,colors))
fss = [
       'full',
       'full',
       'none',
       ]
fsdict = dict(zip(amp, fss))

xmax = 25

fign='Fig6A.png'
fig=plt.figure(figsize=(2,2),dpi=my_dpi)
ax=fig.add_axes(rect)
ax.set_ylim([0,0.3])
ax.set_yticks([0.0, 0.1, 0.2, 0.3])
ax.set_xlim([0,xmax])
ax.set_xlabel('Time (ms)')
ax.set_ylabel('Distibution')

for m in amp:
    fn = 'Fig6A_data_m%d.npz' % m
    data = np.load(fn)
    dt, p = data['dt'], data['p'] 
    ax.plot(dt, p, 'o',mew=0.5,ms=4,fillstyle=fsdict[m],label='[AMP]=%d$\mu M$' % m,color=colordict[m],zorder=0)
ax.legend(fontsize=6,handletextpad=0.0)
fig.text(0.0,0.91,'A',fontsize=16)
fig.text(0.52,0.4,'[ATP]=%d$\mu M$' % atp, fontsize=8)
fig.savefig(fign)
print(fign)
