import numpy as np
import itertools
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from matplotlib import rc
rc('font', **{'style': 'normal', 'size': 8})
rc('axes', **{'titlesize': 8})
rc('mathtext', **{'default': 'regular'})
rc(('xtick', 'ytick'), **{'labelsize': 6, 'direction': 'in', 'major.pad': 1})
rc(('axes'), **{'labelsize': 8, 'labelpad':1, 'linewidth': 1})
rc(('legend'), **{'fontsize': 6, 'markerscale': 1.0, 'handlelength':2.0, 'frameon': False})

plt.rcParams.update({'text.usetex':False})

my_dpi=300
rect=[0.15, 0.15, 0.75, 0.75]

def func(x,kc,ki,km):
    return kc*x/((1/ki)*x*x+x+km)

scale = 2
scaleback = 120

fign='Fig1D.png'
fig = plt.figure(figsize=(2,2),dpi=my_dpi)
ax = fig.add_axes(rect)
ax.set_xlabel(r'$[AMP](\mu M)$',labelpad=2)
ax.set_ylabel(u'Turnover rate ($ms^{\u2010 1})}$')
ax.set_xlim(0,1080)
ax.set_ylim(0,0.35)
ax.set_yticks(np.arange(0,0.35,0.1))
xfit=np.linspace(0,1000,100)

fnfit='Fig1D_data_k.dat'
atpconc,kcat,kcaterr,KI,KIerr,KM,KMerr=np.loadtxt(fnfit) # 2000ADP/min = 1/60 turnover/ms
kcat /= scaleback

for n,t in enumerate(atpconc):
    kc=kcat[n]
    ki=KI[n]
    km=KM[n]
    yfit=func(xfit,kc,ki,km)

    fn='Fig1D_data_t%d.dat' % t
    x,y = np.loadtxt(fn)

    ax.plot(x,y*scale/scaleback,'o',ms=4.0,label='[ATP]=%d$\mu M$' % t)
    ax.plot(xfit,yfit,'-',color=ax.lines[-1].get_color())

ax.legend(loc='lower center',handlelength=1.8,markerscale=1.0)

fig.savefig(fign)
