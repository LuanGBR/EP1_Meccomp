
import numpy as np

def integration_step(i_result,iresult_prev,h):
    return (i_result+iresult_prev)*h/2

        
def runge_kutta_step(f,t,y,i,h,q):
    k1 = f(t[i],y[i,:],q)
    k2 = f(t[i]+h/2,y[i,:]+h/2*k1,q)
    k3 = f(t[i]+h/2,y[i,:]+h/2*k2,q)
    k4 = f(t[i]+h,y[i,:]+h*k3,q)
    y[i+1,:] = y[i,:] + h/6*(k1+2*k2+2*k3+k4)
    return y

def runge_kutta(f,y0,h,t0,n,q0):
    t = np.arange(t0,t0+n*h,h)
    Y = np.zeros((n+1,2))
    Q = np.zeros(n+1)
    Y[0,:] = y0
    Q[0] = q0
    for i in range(0,n):
        Y = runge_kutta_step(f,t,Y,i,h,Q[i])
        Q[i+1] = Q[i] + integration_step(Y[i,0]-Y[i,1],Q[i],h)
    return Y