"""
  Name     : 4375OS_11_40_barrier_up_call.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def up_call(s0,x,T,r,sigma,n_simulation,barrier):
    """
      Objective: output up_and_out_call and 
                        up_and_in_call
      
    """
    import scipy as sp
    import p4f
    n_steps=100.    
    dt=T/n_steps
    inTotal=0
    outTotal=0
    for j in range(0, n_simulation):
        sT=s0
        inStatus=False
        outStatus=True
        for i in range(0,int(n_steps)):
            e=sp.random.normal()
            sT*=sp.exp((r-0.5*sigma*sigma)*dt+sigma*e*sp.sqrt(dt))
            if sT>barrier:
                outStatus=False
                inStatus=True
                #print 'sT=',sT
        #print 'j=',j ,'out=',out
        if outStatus==True:
            outTotal+=p4f.bs_call(s0,x,T,r,sigma)
        else:
            inTotal+=p4f.bs_call(s0,x,T,r,sigma)
    return outTotal/n_simulation, inTotal/n_simulation


s0=40.           # today stock price 
x=40.            # exercise price
barrier=42       # barrier level
T=0.5            # maturity in years
r=0.05           # risk-free rate
sigma=0.2        # volatility (annualized)
n_simulation=100 # number of simulations 
upOutCall,upInCall=up_call(s0,x,T,r,sigma,n_simulation,barrier)
print 'upCall=', round(upOutCall,2),'upInCall=',round(upInCall,2)
print 'Black-Scholes call', round(p4f.bs_call(s0,x,T,r,sigma),2)



