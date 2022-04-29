import numpy as np

from runge_kutta import runge_kutta
Q_acumulado = [0]
def f(t,Y,h):
    """ 
    devolve o valor das derivadas de i1, i2 e o valor q acumulado 
    no vetor np.array(i1p,i2p,qf)
    """
    Lb = 0.5
    Rb = 20
    C = 0.002
    La = 0.01
    Ra = 200
    i1=Y[0]
    i2=Y[1]
    e = np.cos(t*600)/La
    
    Q_acumulado[0] = Q_acumulado[0] + ( 0 if np.isnan( h * np.sin(i1-i2)/2) else h * np.sin(i1-i2)/2)
    qf = Q_acumulado[0]
    i1p = (e - Ra*(i1 - i2) - qf/C)/La
    i2p = (qf/C + Ra*(i1 - i2) - Rb*i2)/Lb
    return np.array([i1p,i2p,i1-i2])







def main():
    print(runge_kutta(f,0.001,0.0,np.array([0.0,0.0,0.0])  ,30))


if __name__ == '__main__':
    main()