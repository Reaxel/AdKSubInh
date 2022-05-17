import numpy as np
import itertools
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import ticker, cm

rc('font',**{'style':'normal','size':8})
rc('axes',**{'titlesize':8})
rc('mathtext',**{'default':'regular'})
rc(('xtick','ytick'),**{'labelsize':6,'direction':'in','major.pad':1})
rc(('axes'),**{'labelsize':8,'labelpad':1,'linewidth':1})
rc(('legend'),**{'fontsize':6,'frameon':False,'handlelength':1.8,'markerscale':1.0})

my_dpi=300
rect=[0.18,0.15,0.75,0.75]

dvlist=[0,7,16,10,2,14]
pclose=[0.28,0.003,0.01,0.12,0.77,0.994]
pdict=dict(zip(dvlist,pclose))
colors = ['k','r','b','pink','wheat','palegreen','paleturquoise']

atp=[1000]

ymin,ymax=0.5,2.5

tmax=10000

dvlist=[
        0,
        16,
        14
        ]

fig=plt.figure(figsize=(2,2),dpi=my_dpi)
fign = 'Fig3B.png'
ax=fig.add_axes(rect)
ax.set_prop_cycle(color=colors)
ax.set_ylabel('MFPT',fontsize=8)
ax.set_xlabel('[AMP] ($\mu M$)')
ax.set_ylim(ymin,ymax)
ax.set_yticks(np.linspace(ymin,ymax,5))
ax.set_xticks(np.arange(0,1200,200))

for i in dvlist:
    fn='Fig3B_data_dv%d.npz'%i
    data=np.load(fn)
    amp,fptav=data['amp'],data['av']
    mask=np.isin(amp,amp)
    amp,fptav=amp[mask],fptav[mask]
    p=pdict[i]
    ax.plot(amp,fptav,'s-',label='$P_{close}$=%.2f'%p,lw=1.5,ms=4)

ax.legend(loc='best',markerscale=1.0,fontsize=8)

fig.text(0.0,0.91,'B',fontsize=16)
fig.savefig(fign,dpi=my_dpi)
print(fign)
