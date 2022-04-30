import numpy as np

from parte1 import runge_kutta

Lb = 0.5
Rb = 20
C = 0.002
La = 0.01
Ra = 200

def f(t,Y,q):
    """ 
    devolve o valor das derivadas de i1, i2 e o valor q acumulado 
    no vetor np.array(i1p,i2p)
    """
    i1 = Y[0]
    i2 = Y[1]
    e = np.cos(t*600)/La
    Y[0] = (e - Ra*(i1 - i2) - q/C)/La
    Y[1] = (q/C + Ra*(i1 - i2) - Rb*i2)/Lb

    return Y






def main():
    print(runge_kutta(f,np.array([0.0,0.0]),0.001,0.0 ,30,0.0))


if __name__ == '__main__':
    main()