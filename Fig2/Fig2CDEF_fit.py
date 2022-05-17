import numpy as np
import itertools
from scipy.optimize import curve_fit

def func(x,kc,ki,km):
    return kc*x/((1/ki)*x*x+x+km)

pcloselist=[
            0.283,
            0.008,
            0.019,
            0.119,
            0.581,
            0.775,
            0.994
            ]
pre7="0.41".split()
xkai="0.50".split()

ampconc=[0,9,22,44,66,100,150,200,250,300,400,500,600,700,800,900,1000]
scale=2.0 # 2ADP for 1turnover

pclosefinal=[]
kcatlist=[]
kcaterr=[]
KIlist=[]
KIerr=[]
KMlist=[]
KMerr=[]

for n,pclose in enumerate(pcloselist):
    fn='Fig2CDEF_data_p%0.3f.dat' % pclose
    x,y = np.loadtxt(fn)

    y *=scale

    p0=(50,1000,70)
    (kcat,KI,KM),pcov=curve_fit(func,x,y,p0)

    pclosefinal.append(pclose)
    kcatlist.append(kcat)
    KIlist.append(KI)
    KMlist.append(KM)
    kcaterr.append(pcov[0,0]**0.5)
    KIerr.append(pcov[1,1]**0.5)
    KMerr.append(pcov[2,2]**0.5)

pclosefinal = np.array(pclosefinal)
kcatlist = np.array(kcatlist)
kcaterr = np.array(kcaterr)
KIlist = np.array(KIlist)
KIerr = np.array(KIerr)
KMlist = np.array(KMlist)
KMerr = np.array(KMerr)
foutn = 'Fig2CDEF_data_k.dat'
print(foutn)
isort = np.argsort(pclosefinal)
plist = pclosefinal[isort]
kcatlist = kcatlist[isort]
kcaterr = kcaterr[isort]
KIlist = KIlist[isort]
KIerr = KIerr[isort]
KMlist = KMlist[isort]
KMerr = KMerr[isort]
np.savetxt(foutn,(plist,kcatlist,kcaterr,KIlist,KIerr,KMlist,KMerr),fmt='%.3f')
