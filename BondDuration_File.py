import numpy as np

def getBondDuration(y, face, couponRate, m, ppy = 1):
    n=m*ppy
    rate=y/ppy
    c=couponRate*face/ppy

    t=np.arrange(1,n+1)
    df=(1+rate)**(-t)
    cf=np.full(n,c)
    cf[-1]=c+face

    pvcf=cf*df

    price=np.sum(pvcf)

    duration=np.sum((t/ppy)*pvcf/price)
    return (duration)
