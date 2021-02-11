import numpy as np
from sympy import *

from pyggb.utils import toLatex
from pyggb.Function import Function


class PyGeogebra:
    def __init__(self, plt, figure, setting):
        self.plt = plt
        self.figure = figure
        self.setting = setting

    def show(self):
        self.plt.legend()
        self.plt.plot()

    def save(self):
        self.plt.legend()
        self.plt.plot()
        self.plt.savefig(self.setting['output'])

    def addTitle(self, title):
        self.plt.title(title)

    def plotFunction(self, text='', x=None, y=None, f=None, x_limit=None, f_str=''):
        if x_limit is None:
            x_limit = []
        if y is None:
            y = []
        if x is None:
            x = []
        if len(x) != 0 and len(y) != 0:
            self.plt.plot(x, y, label=toLatex(text))
        elif f is not None and len(x_limit) != 0:
            x = np.arange(x_limit[0], x_limit[1], self.setting['x-step'])
            y = [f(i) for i in x]
            self.plt.plot(x, y, label=toLatex(text))
            function_prototype = Function(x_limit=x_limit, text=toLatex(text), f=f)
            return function_prototype
        elif len(f_str) != 0 and len(x_limit) != 0:
            x = np.arange(x_limit[0], x_limit[1], self.setting['x-step'])
            y = [eval(f_str) for x in x]
            self.plt.plot(x, y, label=toLatex(text))
            function_prototype = Function(x_limit=x_limit, text=toLatex(text), f_str=f_str)
            return function_prototype

    def drawPoint(self, x, y, text=''):
        self.plt.scatter(x, y, self.setting["point-radius"])
        self.plt.text(x + self.setting["x-text-offset"], y + self.setting["y-text-offset"], toLatex(text),
                      fontsize=self.setting["font-size"])
        point_prototype = Point(x, y, text=toLatex(text))
        return point_prototype

    def drawSegment(self, A, B, text=''):
        x_begin = min(A.x, B.x)
        x_end = max(A.x, B.x)
        x = np.arange(x_begin, x_end, self.setting['x-step'])
        k = (B.y - A.y) / (B.x - A.x)
        y0 = A.y if x_begin == A.x else B.y
        y = [(y0 + (i - x_begin) * k) for i in x]
        self.plt.plot(x, y)
