import numpy as np
import itertools
from scipy.optimize import curve_fit

def func(x,kc,ki,km):
    return kc*x/((1/ki)*x*x+x+km)

atpconc=[1000,600,300]

scale=2.0

kcatlist=[]
kcaterr=[]
KIlist=[]
KIerr=[]
KMlist=[]
KMerr=[]

for t in atpconc:
    fn='Fig1D_data_t%s.dat' % t
    x,y = np.loadtxt(fn)

    y *=scale

    p0=(50,1000,70)

    (kcat,KI,KM),pcov=curve_fit(func,x,y,p0)

    kcatlist.append(kcat)
    KIlist.append(KI)
    KMlist.append(KM)
    kcaterr.append(pcov[0,0]**0.5)
    KIerr.append(pcov[1,1]**0.5)
    KMerr.append(pcov[2,2]**0.5)

#output fitdata:atpconc,kcat,KI,KM
fnfit='Fig1D_data_k.dat'
np.savetxt(fnfit,(atpconc,kcatlist,kcaterr,KIlist,KIerr,KMlist,KMerr),fmt='%.3f')
