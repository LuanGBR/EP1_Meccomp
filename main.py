import numpy as np

<<<<<<< HEAD
from runge_kutta import runge_kutta
Q_acumulado = [0]
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

    dY = np.zeros(3)
    dY[0] = e(t)+(-Ra*(i1-i2)-q/C)/La
    dY[1] = (+Ra*(i1-i2)-Rb*i2+q/C)/Lb
    dY[2] = i1-i2

    return dY
=======
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
>>>>>>> 3f0858c7707250b51d481d18f731ec710bb847a9






def main():
<<<<<<< HEAD
    print(runge_kutta(f, [0,0,0], 0, 0.0001, tf=0.03)[-1][-1])
=======
    print(runge_kutta(f,np.array([0.0,0.0]),0.001,0.0 ,30,0.0))
>>>>>>> 3f0858c7707250b51d481d18f731ec710bb847a9


if __name__ == '__main__':
    main()