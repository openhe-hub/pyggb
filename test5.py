from pyggb.setting import init


def f(x, param=0):
    return param * (x ** 2)


if __name__ == '__main__':
    ggb = init()
    ggb.addTitle('Graph 1')
    a = ggb.buildSlider(-2, 2, 0.1, name="a")
    gif = ggb.drawAnimation(a, f, [-2, 2])
    ggb.saveAsGIF(gif)
