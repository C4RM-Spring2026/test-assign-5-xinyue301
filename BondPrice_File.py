import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    if ppy == 1:
        n=m
        rate=y
        c=couponRate*face
    else:
        n=m*ppy
        rate=y/ppy
        c=couponRate*face/ppy
    
    t=np.arrange(1,n+1)
    df=(1+rate)**(-t)

    price=np.sum(c*df)+face*df[-1]
    return float(price)
