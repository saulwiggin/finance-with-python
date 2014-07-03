"""
#http://code.google.com/p/pysal/source/browse/trunk/pysal/spreg/diagnostics.py?r=1048
# author: Luc Anselin 
    Calculates the Breusch-Pagan test statistic to check for heteroscedasticity. 
    Parameters
    ----------
     reg     : regression object
               output instance from a regression model
     z       : array
             optional input for specifying an alternative set of variables (Z) 
             to explain the observed variance. By default this is a matrix of 
             the squared explanatory variables (X**2) with a constant added 
             to the first column if not already present. In the default case,
            the explanatory variables are squared to eliminate negative values. 
     Returns
     -------
     bp_result  : dictionary
                  contains the statistic (bp) for the test and the
                  associated p-value (p-value)
     bp         : Breusch-Pagan test statistic
     df         : degrees of freedom associated with the test (k)
     pvalue     : p-value associated with the statistic (chi^2 distributed with k df)
 
    References
     ----------
    .. [1] T. Breusch and A. Pagan. 1979. A simple test for
 
       heteroscedasticity and random coefficient variation. Econometrica:
 
       Journal of the Econometric Society, 47(5):1287-1294.
     Examples
     --------
     >>> import numpy as np
     >>> import pysal
     >>> import diagnostics
     >>> from ols import BaseOLS as OLS
     Read the DBF associated with the Columbus data.
     >>> db = pysal.open("pysal/examples/columbus.dbf","r")
     Create the dependent variable vector. 
     >>> y = np.array(db.by_col("CRIME"))
     >>> y = np.reshape(y, (49,1))
 
    Create the matrix of independent variables. 
     >>> X = []
     >>> X.append(db.by_col("INC"))
     >>> X.append(db.by_col("HOVAL"))
     >>> X = np.array(X).T
     Run an OLS regression.
     >>> reg = OLS(y,X)
     Calculate the Breusch-Pagan test for heteroscedasticity.
     >>> testresult = diagnostics.breusch_pagan(reg)
     Print the degrees of freedom for the test.
     >>> testresult['df']
    2
     Print the test statistic.
     >>> print("%12.12f"%testresult['bp'])
     7.900441675960
     Print the associated p-value. 
     >>> print("%12.12f"%testresult['pvalue'])
     0.019250450075
    """

def breusch_pagan(reg, z=None):
    e=reg.resid      #  e = reg.u
    e2 = e**2        # e2 = reg.u**2
    n=reg.nobs       # n = reg.n
    k=reg.k_constant # k = reg.k
    ete=np.dot(reg.resid,reg.resid)  #  ete = reg.utu
    den = ete/n
    g = e2/den - 1.0
    if z == None:
        x = reg.x
        constant = constant_check(x)
        if constant == False:
            z = np.hstack((np.ones((n,1)),x))**2
        else:
            z = x**2
    else:
        constant = constant_check(z)
        if constant == False: 
            z = np.hstack((np.ones((n,1)),z))
    n,p = z.shape
    # Check to identify any duplicate columns in Z
    omitcolumn = []
    for i in range(p):
        current = z[:,i]
        for j in range(p):
            check = z[:,j]
            if i < j:
                test = abs(current - check).sum()
                if test == 0:
                     omitcolumn.append(j)
    uniqueomit = set(omitcolumn)
    omitcolumn = list(uniqueomit)
    # Now the identified columns must be removed (done in reverse to
    # prevent renumbering)
    omitcolumn.sort()
    omitcolumn.reverse()
    for c in omitcolumn:
         z = np.delete(z,c,1)
    n,p = z.shape
    df = p-1
    # Now that the variables are prepared, we calculate the statistic
    zt = np.transpose(z)
    gt = np.transpose(g)
    gtz = np.dot(gt,z)
    ztg = np.dot(zt,g)
    ztz = np.dot(zt,z)
    ztzi = la.inv(ztz)
    part1 = np.dot(gtz, ztzi)
    part2 = np.dot(part1,ztg)
    bp_array = 0.5*part2
    bp = bp_array[0,0]
    pvalue=stats.chisqprob(bp,df)
    bp_result={'df':df,'bp':bp, 'pvalue':pvalue}
    return bp_result
 
import numpy as np
import pysal
import diagnostics
from ols import BaseOLS as OLS
#import statsmodels.api as sm
db = pysal.open("c:/ttt/columbus.dbf","r")
y = np.array(db.by_col("CRIME"))
y = np.reshape(y, (49,1))
X = []
X.append(db.by_col("INC"))
X.append(db.by_col("HOVAL"))
X = np.array(X).T
#reg = OLS(y,X)
reg=OLS(y,X)
#testresult = diagnostics.breusch_pagan(reg)
result=breusch_pagan(reg)




