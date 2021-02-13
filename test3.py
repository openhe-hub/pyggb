from sympy import sin, pi

from pyggb.setting import init


def f(x):
    return x ** 3 - x


if __name__ == '__main__':
    ggb = init()
    ggb.addTitle('Graph 1')
    fx = ggb.plotFunction(f=f, x_limit=[-2, 2], text='f(x)=x^3-x')
    ggb.drawZero(fx, x_limit=[-2, 2])
    ggb.save()
