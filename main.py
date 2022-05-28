import numpy as np

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

    #Calculates the slope vector
    dY = np.zeros(3)
    dY[0] = e(t)+(-Ra*(i1-i2)-q/C)/La
    dY[1] = (+Ra*(i1-i2)-Rb*i2+q/C)/Lb
    dY[2] = i1-i2

    return dY


def main():
    print(runge_kutta(f, [0,0,0], 0, 0.0001, tf=0.03)[-1][-1])


if __name__ == '__main__':
    main()