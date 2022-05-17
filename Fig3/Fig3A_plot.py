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

dvlist = [0, 16, 14, 15, 10, 1, 2 ]
pclose = [0.28, 0.01, 0.99, 0.02, 0.12, 0.58, 0.77]
pdict=dict(zip(dvlist,pclose))
pimportant=[0.28, 0.01, 0.99]
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
fign = 'Fig3A.png'
ax=fig.add_axes(rect)
ax.set_prop_cycle(color=colors)
# ax.set_title('$\O \O$ open->TM closed')
# ax.set_ylabel('MFPT/MFPT([AMP]=200$\mu$M)',fontsize=7.5)
ax.set_ylabel('MFPT',fontsize=8)
ax.set_xlabel('[AMP] ($\mu M$)')
# ax.set_xlim([0,1000])
ax.set_ylim(ymin,ymax)
ax.set_yticks(np.linspace(ymin,ymax,5))
ax.set_xticks(np.arange(0,1200,200))
# ax.set_xscale('log')


for i in dvlist:
    fn='Fig3A_data_dv%d.npz'%i
    data=np.load(fn)
    amp,fptav=data['amp'],data['av']
    mask=np.isin(amp,amp)
    amp,fptav=amp[mask],fptav[mask]
    p=pdict[i]
    zorder = 2
    if p in pimportant:
        zorder = 5
        print(p)
    ax.plot(amp,fptav,'s-',label='$P_{close}$=%.2f'%p,lw=1.5,ms=4,zorder=zorder)

ax.legend(loc='best',markerscale=1.0,fontsize=8)

fig.text(0.0,0.91,'A',fontsize=16)
fig.savefig(fign,dpi=my_dpi)
print(fign)
