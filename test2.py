from pyggb.setting import init


def f(x): return -x+1


def g(x): return 0


def h(x): return x


if __name__ == '__main__':
    ggb = init()
    ggb.addTitle('Graph 1')
    fx = ggb.plotFunction(f=f, x_limit=[-2, 2], text='f(x)=-x')
    gx = ggb.plotFunction(f=g, x_limit=[-2, 2], text='g(x)=x^2')
    hx = ggb.plotFunction(f=h, x_limit=[-2, 2], text='h(x)=x')
    ggb.fill(hx, gx, x_limit=[0, 0.5])
    ggb.fill(gx, fx, x_limit=[0.5, 1])
    ggb.save()
