import numpy as np
def runge_kutta(f,h,x0,y0,n):
    x=np.zeros(n+1)
    y=np.zeros((n+1,y0.shape[0]))
    x[0]=x0
    y[0,:]=y0
    for i in range(n):
        k1=f(x[i],y[i,:],0)
        k2=f(x[i]+h/2,y[i,:]+h*k1/2,h/2)
        k3=f(x[i]+h/2,y[i,:]+h*k2/2,h/2)
        k4=f(x[i]+h,y[i,:]+h*k3,h)
        y[i+1]=y[i,:]+h*(k1+2*k2+2*k3+k4)/6
        x[i+1]=x[i]+h
    return x,y