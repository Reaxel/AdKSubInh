import numpy as np
import matplotlib.pyplot as plt
import itertools

from matplotlib import rc

rc('font',**{'style':'normal','size':8}) # 12
rc('axes',**{'titlesize':8})
rc('mathtext',**{'default':'regular'})
rc(('ytick'),**{'labelsize':6,'direction':'in','major.pad':1,'major.size':3})
rc(('xtick'),**{'labelsize':6,'direction':'in','major.pad':1,'major.size':3})
rc(('axes'),**{'labelsize':8,'labelpad':1,'linewidth':1}) # 10
rc(('legend'),**{'fontsize':6,'frameon':False,'labelspacing':0.5,'handletextpad':0.8}) # 8

cls=plt.rcParams['axes.prop_cycle'].by_key()['color']


my_dpi = 300
rect = [0.18,0.15,0.75,0.75]

scaleback = 60 * 2

def func(x,kc,ki,km):
    return kc*x/((1/ki)*x*x+x+km)

shape1=(6.1/3,2)
shape1=(2,2)

fin='Fig2CDEF_data_k.dat'

#plot fit params
pclose,kcat,kcaterr,KI,KIerr,KM,KMerr=np.loadtxt(fin) # 2000ADP/min = 1/60 turnover/ms
kcat /= scaleback
kcaterr /= scaleback

# ========================================================================
# plot kcat
fig = plt.figure(figsize=shape1,dpi=my_dpi)
fign = 'Fig2D.png'
ax = fig.add_axes(rect)
ax.set_xlabel('$P_{close}$')
ax.set_ylabel('$k_{cat}$ ($ms^{\u2010 1}$)')
c1,c2=0.2,0.6
ax.set_ylim(c1,c2)
ax.set_yticks(np.linspace(c1,c2,5))

# log
ax.set_xscale('log')
ax.set_xlim(0.008*10**(-0.2),1*10**(0.2))

ax.vlines(x=0.283,ymin=0,ymax=1000,linestyle='--',color="grey",lw=1.0)
line = ax.errorbar(pclose,kcat,kcaterr,color='k',capsize=2,lw=1.0)

fig.text(0.0,0.91,'D',fontsize=16)
fig.savefig(fign)
print(fign)
fig.savefig(fign)

# ========================================================================
# plot KM
fig = plt.figure(figsize=shape1,dpi=my_dpi)
fign = 'Fig2E.png'
ax = fig.add_axes(rect)
ax.set_xlabel('$P_{close}$')
ax.set_ylabel('$K_M$ ($\mu M$)')
m1,m2=0,200
ax.set_ylim(m1,m2)
ax.set_yticks(np.linspace(m1,m2,5))

# log
ax.set_xscale('log')
ax.set_xlim(0.008*10**(-0.2),1*10**(0.2))

ax.vlines(x=0.283,ymin=0,ymax=1000,linestyle='--',color="grey",lw=1.0)
line = ax.errorbar(pclose,KM,KMerr,color='k',capsize=2,lw=1.0)

fig.text(0.0,0.91,'E',fontsize=16)
fig.savefig(fign)
print(fign)
fig.savefig(fign)

# ========================================================================
# plot KI
fig = plt.figure(figsize=shape1,dpi=my_dpi)
fign = 'Fig2F.png'
ax = fig.add_axes(rect)
ax.set_xlabel('$P_{close}$')
ax.set_ylabel('$K_I$ (mM)')
i1,i2=0.0,4.0
ax.set_ylim(i1,i2)
ax.set_yticks(np.linspace(i1,i2,5))

# log
ax.set_xscale('log')
ax.set_xlim(0.008*10**(-0.2),1*10**(0.2))

ax.vlines(x=0.283,ymin=0,ymax=4000,linestyle='--',color="grey",lw=1.0)
line = ax.errorbar(pclose,KI/1000,KIerr/1000,color='k',capsize=2,lw=1.0)

fig.text(0.0,0.91,'F',fontsize=16)
fig.savefig(fign)
print(fign)
fig.savefig(fign)

# =======================================================================
#plot turnover_fit
pselect = np.array([0.283, 0.008, 0.994, 0.019, 0.119, 0.581, 0.775])
pimportant = np.array([0.283,0.008,0.994])
colors = ['k','r','b','pink','wheat','palegreen','paleturquoise']
colordict = dict(zip(pselect,colors))

fign='Fig2C.png'
fig = plt.figure(figsize=(2,2),dpi=my_dpi)
ax = fig.add_axes([0.18,0.15,0.75,0.75])
ax.set_xlim(0,1050)
ax.set_ylim(0,0.38)
# ax.set_ylim(0,0.45)
ax.set_yticks(np.arange(0, 0.4,0.1))
ax.set_xlabel('AMP $(\mu M)$',labelpad=2)
ax.set_ylabel('Turnover rate ($ms^{\u2010 1}$)')

xfit = np.linspace(0,1000,100)

for p in pselect:
    alpha = 0.8
    zorder = 2
    label = '%.2f' % p
    ms=4
    lw=1
    if p in pimportant:
        alpha = 1
        zorder = 5
        ms = 4.5
        lw = 1.5
    if p==0.283:
        label = ''
    datan='Fig2CDEF_data_p%.3f.dat' % p
    x,y = np.loadtxt(datan)
    y /= 60
    index = list(pclose).index(p)
    kc = kcat[index]
    ki = KI[index]
    km = KM[index]
    yfit=func(xfit,kc,ki,km)
    ax.plot(x,y,'o',ms=ms,mew=0,color=colordict[p],alpha=alpha,zorder=zorder,label=label)
    ax.plot(xfit,yfit,color=ax.lines[-1].get_color(),lw=lw,alpha=alpha,zorder=zorder)

prop = dict(arrowstyle="-|>,head_width=0.1,head_length=0.6",
        shrinkA=0,shrinkB=0,facecolor='k',lw=1)
ax.annotate('',xy=(520+150,0.29+0.05),xytext=(520,0.29),arrowprops=prop)
ax.text(670,0.32,'WT',fontsize=8)

ax.legend(loc='lower center',ncol=3,fontsize=5.5,handletextpad=-0.4)
fig.text(0.0,0.91,'C',fontsize=16)
fig.savefig(fign)
print(fign)
