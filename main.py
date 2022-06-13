import numpy as np
import matplotlib.pyplot as plt

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
    dY=np.zeros((n+1,len(Y0)))
    Y[0] = Y0
    for i in range(n):
        k1 = f(t[i],Y[i])
        k2 = f(t[i]+h/2,Y[i]+h*k1/2)
        k3 = f(t[i]+h/2,Y[i]+h*k2/2)
        k4 = f(t[i]+h,Y[i]+h*k3)
        Y[i+1] = Y[i] + h*(k1+2*k2+2*k3+k4)/6
        dY[i] = k1
    dY[n]=f(t[n],Y[n])

    return t,Y,dY

def f(t,Y):
    #Constants
    Ra = 200
    Rb = 20
    La = 0.01
    Lb = 0.5
    C = 0.002
    e = lambda t: np.cos(t*600)/La

    #Variables
    i1 = Y[0]
    i2 = Y[1]
    q = Y[2]

    #Calculates the slope vector
    dY = np.zeros(3)
    dY[0] = e(t)+(-Ra*(i1-i2)-q/C)/La
    dY[1] = (+Ra*(i1-i2)-Rb*i2+q/C)/Lb
    dY[2] = i1-i2

    return dY

def plot(t,Y,dY):
    Y = np.concatenate((Y,dY),axis=1)
    OGs = [np.floor(np.log10(abs(x.min()-x.max()))) for x in Y.T]
    scaler = [max(OGs)-x for x in OGs]
    fig = plt.figure(figsize=(16,9))
    ax = fig.add_subplot(1,1,1)
    ax.plot(t,Y[:,0]*10**scaler[0],label=f'i1 (1e-{scaler[0]} A)')
    ax.plot(t,Y[:,1]*10**scaler[1],label=f'i2 (1e-{scaler[1]} A)')
    ax.plot(t,Y[:,2]*10**scaler[2],label=f'q (1e-{scaler[2]} C)')
    ax.plot(t,dY[:,0]*10**scaler[3],label=f'i1p ({scaler[3]} A/s)')
    ax.plot(t,dY[:,1]*10**scaler[4],label=f'i2p (1e-{scaler[4]} A/s)')
    ax.plot(t,dY[:,2]*10**scaler[5],label=f'qp (1e-{scaler[5]} C/s)')
    ax.legend()
    ax.grid()
    plt.show()

#passo pequeno
t,Y,dY = runge_kutta(f, [0,0,0], 0, (0.000001)/2, tf=0.03)
plot(t,Y,dY)
#passo medio
t,Y,dY = runge_kutta(f, [0,0,0], 0, 0.0001, tf=0.03)
plot(t,Y,dY)
#passo grande
t,Y,dY = runge_kutta(f, [0,0,0], 0, 0.01, tf=0.03)
plot(t,Y,dY)
