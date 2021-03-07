import math as m

def comb(n, r):
    comb = m.factorial(n) / (m.factorial(r) * m.factorial(n-r))
    return comb

def AaBb(k, N):
    p = 0
    num = 2**k
    for i in range(N, num+1):
        p += comb(num, i) * (3**(num-i)) / (4**num)
    return p
    
print(AaBb(6, 17))
