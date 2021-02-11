from numpy import sin, cos, pi

from pyggb.setting import init, config


def g(x):
    return sin(x)


def eq1(zeta):
    return 2 * cos(zeta), 1 * sin(zeta)


def l1(x):
    return x + 1


if __name__ == '__main__':
    ggb = init()
    ggb.addTitle('Graph 1')
    ggb.plotEquation(eq1, [0, 2 * pi], r"\Gamma:\frac{x^2}{4}+\frac{y^2}{1}=1")
    A1 = ggb.drawPoint(-2, 0, r"A_1")
    B1 = ggb.drawPoint(0, 1, r"B_1")
    ggb.drawLine(A1, B1, [-3, 3], r"l_{A_1B_1}")
    ggb.plotFunction(f=l1, x_limit=[-2, 2], text=r"l_1:y=x+1")
    ggb.save()
