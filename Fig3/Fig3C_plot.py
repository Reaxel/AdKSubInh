import numpy as np
import itertools
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font',**{'style':'normal','size':8}) # 12
rc('axes',**{'titlesize':8})
rc('mathtext',**{'default':'regular'})
rc(('ytick'),**{'labelsize':6,'direction':'in','major.pad':1,'major.size':3})
rc(('xtick'),**{'labelsize':7,'direction':'in','major.pad':2,'major.size':3})
rc(('axes'),**{'labelsize':8,'labelpad':1,'linewidth':1}) # 10
rc(('legend'),**{'fontsize':4,'frameon':False,'columnspacing':1.0,'handletextpad':0.2,'handlelength':1.2,'markerscale':0.6}) # 8

colors=plt.rcParams['axes.prop_cycle'].by_key()['color']

my_dpi=300
rect=[0.18,0.15,0.75,0.75]

fn = 'Fig3C_data.npz'
data = np.load(fn)
amp = data['amp']
frustrated = data['frustrated']
canonical = data['canonical']
hybridDM = data['hybridDM']

fig = plt.figure(figsize=(2, 2), dpi=my_dpi)
fign = 'Fig3C.png'
ax = fig.add_axes(rect)
ax.set_ylim([-0.08, 1.08])
ax.set_xscale('log')
ax.set_xlim(9*10**(-0.2), 1000*10**(0.2))
ax.set_xlabel('[AMP] ($\mu M$)')
ax.set_ylabel('Probability')

ax.plot(amp, frustrated, 's-', label='Frustrated', color=colors[0], alpha=1)
ax.plot(amp, hybridDM, 's-', label='Hybrid DM', color=colors[0], mfc='w', alpha=1)
ax.plot(amp, canonical, 's-', label='Canonical', color='k')

ax.legend(loc='upper right', \
          fontsize=6.5,ncol=2,columnspacing=1.5,handletextpad=None, \
          markerscale=0.8)

fig.text(0.0,0.91,'C',fontsize=16)
fig.savefig(fign, dpi=my_dpi)
