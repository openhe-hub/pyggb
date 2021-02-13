import numpy as np
from sympy import *

from pyggb.Equation import Equation
from pyggb.utils import toLatex
from pyggb.Function import Function
from pyggb.Point import Point


class PyGeogebra:
    O = Point(0, 0, 'O')

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
        self.plt.title(title, loc="left")

    def plotFunction(self, text='', x=None, y=None, f=None, x_limit=None, line_style='-'):
        if x_limit is None:
            x_limit = []
        if y is None:
            y = []
        if x is None:
            x = []
        if len(x) != 0 and len(y) != 0:
            self.plt.plot(x, y, label=toLatex(text), linestyle=line_style)
        elif f is not None and len(x_limit) != 0:
            x = np.arange(x_limit[0], x_limit[1] + self.setting['x-step'], self.setting['x-step'])
            length = x.shape
            y = np.zeros(length)
            for i in range(length[0]):
                y[i] = f(x[i])
            self.plt.plot(x, y, label=toLatex(text), linestyle=line_style)
            function_prototype = Function(x_limit=x_limit, data=[x, y], text=toLatex(text), f=f)
            return function_prototype

    def plotEquation(self, equation, param_limit, text='', line_style='-'):
        param = np.arange(param_limit[0], param_limit[1] + self.setting['x-step'], self.setting['x-step'])
        length = param.shape
        x, y = np.zeros(length), np.zeros(length)
        for i in range(length[0]):
            (x[i], y[i]) = equation(param[i])
        self.plt.plot(x, y, label=toLatex(text), linestyle=line_style)
        equation_prototype = Equation(equation, param_limit, text)
        return equation_prototype

    def drawPoint(self, x, y, text='', point_style='o'):
        self.plt.scatter(x, y, self.setting["point-radius"], marker=point_style)
        self.plt.text(x + self.setting["x-text-offset"], y + self.setting["y-text-offset"], toLatex(text),
                      fontsize=self.setting["font-size"])
        point_prototype = Point(x, y, text=toLatex(text))
        return point_prototype

    def drawMidPoint(self, A, B, text='', point_style=','):
        return self.drawPoint((A.x + B.x) / 2, (A.y + B.y) / 2, text=text, point_style=point_style)

    def drawSegment(self, A, B, line_style='-'):
        x_begin = min(A.x, B.x)
        x_end = max(A.x, B.x)
        x = np.arange(x_begin, x_end + self.setting['x-step'], self.setting['x-step'])
        k = (B.y - A.y) / (B.x - A.x)
        y0 = A.y if x_begin == A.x else B.y
        y = np.zeros(x.shape)
        for i in range(x.shape[0]):
            y[i] = y0 + (x[i] - x_begin) * k
        self.plt.plot(x, y, linestyle=line_style)

    def drawLine(self, A, B, x_limit, text='', line_style='-'):
        x_begin = x_limit[0]
        x_end = x_limit[1]
        x = np.arange(x_begin, x_end + self.setting['x-step'], self.setting['x-step'])
        k = (B.y - A.y) / (B.x - A.x)
        x0 = A.x if min(A.x, B.x) == A.x else B.x
        y0 = A.y if min(A.x, B.x) == A.x else B.y
        y0 -= (x0 - x_begin) * k
        y = np.zeros(x.shape)
        for i in range(x.shape[0]):
            y[i] = y0 + (x[i] - x_begin) * k
        self.plt.plot(x, y, label=toLatex(text), linestyle=line_style)
        return Function(x_limit=x_limit, data=[x, y], text=text)

    # x_limit must in x_limit of prototypes
    def fill(self, F1, F2, x_limit):
        deviation = self.setting["deviation"]
        x_begin, x_end = x_limit[0], x_limit[1]
        y1, y2 = F1.data, F2.data
        _x = x = np.arange(x_begin, x_end + self.setting['x-step'], self.setting['x-step'])
        x_begin_index, x_end_index = np.where(abs(y1[0] - x_begin) < deviation), np.where(
            abs(y1[0] - x_end) < deviation)
        _y1 = y1[1][x_begin_index[0][0]:x_end_index[0][0] + 1]
        x_begin_index, x_end_index = np.where(abs(y2[0] - x_begin) < deviation), np.where(
            abs(y2[0] - x_end) < deviation)
        _y2 = y2[1][x_begin_index[0][0]:x_end_index[0][0] + 1]
        self.plt.fill_between(x=_x, y1=_y1, y2=_y2, alpha=self.setting['shadow-alpha'])

    def drawZero(self, fx, x_limit, text=''):
        x, y = symbols('x,y')
        res = solve(fx.f(x), x)
        ans_x, ans_y = [], []
        for i in res:
            if x_limit[0] <= i <= x_limit[1]:
                ans_x.append(i)
                ans_y.append(fx.f(i))
        for i in zip(ans_x, ans_y):
            self.drawPoint(i[0], i[1], f'(${i[0]},${i[1]})')
