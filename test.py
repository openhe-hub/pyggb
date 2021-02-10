from numpy import sin, pi

from pyggb.setting import init, config


def g(x):
    return sin(x)


if __name__ == '__main__':
    ggb = init()
    ggb.addTitle('Graph 1')
    ggb.plotFunction(text='f(x)=ln(x)', f_str='log(x)', x_limit=[1, 4])
    ggb.plotFunction(text='g(x)=sin(x)', f=g, x_limit=[-1 * pi, 1 * pi])
    ggb.plotFunction(text='h(x)=-x', x_limit=[-2, 2], f_str="-x")
    ggb.save()
