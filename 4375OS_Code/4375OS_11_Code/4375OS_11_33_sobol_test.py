# -*- coding: utf-8 -*-
"""
Created on Sat Jan 04 22:51:01 2014

@author: PaulYan
"""
import sobol_seq
n=40
x0=i4_sobol(n,12345)
y0=i4_sobol(n,12555)
x,y=[],[]
for i in xrange(n):
    x.append(x0[0][i])
    y.append(y0[0][i])
plot(x,y,'^r')
title('Sobol sequence')


y5=sp.random.uniform(0,1,40)
x5=sp.random.uniform(0,1,40)
plot(x5,y5,'ob')