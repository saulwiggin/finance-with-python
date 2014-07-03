"""
  Name     : 4375OS_03_20_IRRs_f.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/25/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def IRRs_f(cash_flows):
    """
     Objective: find mutiple IRRs
       e.g,
        >>>x=[55,-50,-50,-50,100]
        >>>IRRs_f(x)
        [0.072, 0.337]
    """
    n=1000
    r=range(1,n)
    n_cash_flow=len(cash_flows)
    epsilon=abs(mean(cash_flows)*0.01)
    irr=[-99.00]
    j=1
    npv=[]
    for i in r: npv.append(0)
   #print("len(r)", len(r))
    #print("len(npv)",len(npv))
    lag_sign=sign(npv_f(float(r[0]*1.0/n*1.0),cash_flows))
    for i in range(1,n-1):
                  #print("r[i]",r[i])
                  interest=float(r[i]*1.0/n*1.0)
                  npv[i]=npv_f(interest,cash_flows)
                  s=sign(npv[i])
                  if s*lag_sign<0:
                      lag_sign=s
                      if j==1:
                          irr=[interest]
                          j=2
                      else:
                          irr.append(interest)
    return irr
