"""
  Name     : 4375OS_12_23_Heston_statistical_volatility.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 1/28/2014
  email    : yany@canisius.edu
             paulyxy@hotmail.com

Wilson Freitas
https://github.com/wilsonfreitas/heston-model/blob/master/Python/heston.py             
          
"""
from numpy import meshgrid, sqrt, diff
from scipy import inf, pi, exp, linspace, zeros, real, imag, array, log
from scipy.stats import norm
from scipy.integrate import quad

def heston_phi(k, tau, *parms):
        """Heston's model characteristic function
        parms have the parameters in this order: lambd, rho, eta, vbar
        """
        v, vbar, lambd, eta, rho = parms
        b = lambd + 1j*rho*eta*k
        d = sqrt( b**2 + (eta**2)*k*(k-1j) )
        g = (b - d)/(b + d)
        T_m = (b - d)/(eta**2)
        T = T_m * ( 1 - exp(-d*tau) )/( 1 - g*exp(-d*tau) )
        W = lambd * vbar * ( tau*T_m - 2*log( ( 1 - g*exp(-d*tau) )/( 1 - g ) )/(eta**2) )
        return exp(W + v*T)

def heston_phi_transform(tau, x, *parms):
        integrand = lambda k: 2 * real( exp(-1j*k*x) * heston_phi(k + 0.5*1j, tau, *parms) )/(k**2 + 1.0/4.0)
        return quad(integrand, 0, 50)[0]

def heston_ucall(F, K, tau, *parms):
        '''Heston call'''
        x = log(F/K)
        return F - (sqrt(K*F)/(2*pi)) * heston_phi_transform(tau, x, *parms)

def heston_call(S, K, tau, r, q, *parms):
        '''Heston call'''
        F = S*exp((r-q)*tau)
        x = log(F/K)
        integral = heston_phi_transform(tau, x, *parms)
        return S * exp(-q*tau) - K * exp(-r*tau) * integral
        
        