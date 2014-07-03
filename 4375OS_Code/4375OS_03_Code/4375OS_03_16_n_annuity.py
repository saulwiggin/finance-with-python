"""
  Name     : 4375OS_03_16_n_annuity.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/25/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

def n_annuity(r,pv,pmt,fv):
    """
  Objective: esimate the number of period
        r  : discount rate
        fv : future value
        pv : present value
        pmt: payment per period
    formula: log((fv*r+pmt)/(pv*r+pmt))/log(1+r)
        e.g.,
        >>> n_annuity(0.0725,10050,5000,60000)
        6.999345696211027
    """
    return log((fv*r+pmt)/(pv*r+pmt))/log(1+r)