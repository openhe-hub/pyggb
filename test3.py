from sympy import sin, pi

from pyggb.setting import init


def f(x):
    return -x ** 2 + 1


if __name__ == '__main__':
    ggb = init()
    ggb.addTitle('Graph 1')
    fx = ggb.drawFunction(f=f, x_limit=[-2, 2], text='f(x)=x^3-x')
    ggb.drawZero(fx, x_limit=[-2, 2], text='A')
    ggb.drawMax(fx, x_limit=[-2, 2], text='B')
    ggb.drawMin(fx, x_limit=[-2, 2], text='C')
    ggb.save()
