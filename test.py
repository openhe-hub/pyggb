from numpy import sin, cos, pi

from pyggb.setting import init, config


def g(x):
    return sin(x)


def eq1(zeta):
    return 2 * cos(zeta), 1 * sin(zeta)


if __name__ == '__main__':
    ggb = init()
    ggb.addTitle('Graph 1')
    ggb.drawEquation(eq1, [0, 2 * pi], r"\Gamma:\frac{x^2}{4}+\frac{y^2}{1}=1")
    A = ggb.drawPoint(-1, 0, r"A")
    B = ggb.drawPoint(0, 1, r"B")
    ggb.drawLine(A, B, [-3, 3], r"l_{AB}")
    M = ggb.drawMidPoint(A, B, text='M', point_style="x")
    ggb.drawSegment(M, ggb.O, line_style='--')
    ggb.save()
