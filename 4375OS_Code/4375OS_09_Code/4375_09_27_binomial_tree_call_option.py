from math import exp,sqrt
def biomialCall(s,x,T,r,sigma,n=100):
    deltaT = T /n
    u = exp(sigma * sqrt(deltaT))
    d = 1.0 / u
    fs = [[0.0 for j in xrange(i + 1)] for i in xrange(n + 1)]
    a = exp(r * deltaT)
    p = (a - d) / (u - d)
    oneMinusP = 1.0 - p
    for j in xrange(i+1):
        fs[n][j] = max(s * u**j * d**(n - j) - x, 0.0)
    for i in xrange(n-1, -1, -1):
        for j in xrange(i + 1):
            fs[i][j]=exp(-r*deltaT)*(p*fs[i+1][j+1]+oneMinusP*fs[i+1][j])
    return fs[0][0]
