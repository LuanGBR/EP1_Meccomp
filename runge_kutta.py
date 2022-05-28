import numpy as np
def runge_kutta(f,Y0,t0,h,tf=None,n=None):
    """
    f: função a ser aplicada
    Y0: vetor inicial
    t0: tempo inicial
    h: passo de integração
    tf: tempo final
    n: número de passos
    """
    if tf is None:
        tf = t0 + n*h
    if n is None:
        n = int((tf-t0)/h)
    t = np.linspace(t0,tf,n+1)
    Y = np.zeros((n+1,len(Y0)))
    Y[0] = Y0
    for i in range(n):
        k1 = f(t[i],Y[i])
        k2 = f(t[i]+h/2,Y[i]+h*k1/2)
        k3 = f(t[i]+h/2,Y[i]+h*k2/2)
        k4 = f(t[i]+h,Y[i]+h*k3)
        Y[i+1] = Y[i] + h*(k1+2*k2+2*k3+k4)/6
    return t,Y