"""
  Name     : 4375OS_12_03_shapiro_normality_tes.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
             
             
    shapiro(x, a=None, reta=False)
    Perform the Shapiro-Wilk test for normality.
    The Shapiro-Wilk test tests the null hypothesis that the
    data was drawn from a normal distribution.
   
    Parameters
    ----------
    x : array_like
        Array of sample data.
    a : array_like, optional
        Array of internal parameters used in the calculation.  If these
        are not given, they will be computed internally.  If x has length
        n, then a must have length n/2.
    reta : bool, optional
        Whether or not to return the internally computed a values.  The
        default is False.
    
    Returns
    -------
    W : float
        The test statistic.
    p-value : float
        The p-value for the hypothesis test.
    a : array_like, optional
        If `reta` is True, then these are the internally computed "a"
        values that may be passed into this function on future calls.
"""
from scipy import stats
from matplotlib.finance import quotes_historical_yahoo
import numpy as np
ticker='IBM'
begdate=(2009,1,1)
enddate=(2013,12,31)
p = quotes_historical_yahoo(ticker, begdate, enddate,asobject=True, adjusted=True)
ret = (p.aclose[1:] - p.aclose[:-1])/p.aclose[1:]
print 'ticker=',ticker,'W-test, and P-value'
print stats.shapiro(ret)
