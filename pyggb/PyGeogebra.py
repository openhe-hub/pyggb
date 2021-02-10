import numpy as np
from sympy import *


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
            self.plt.plot(x, y, label='$' + text + '$')
        elif f is not None and len(x_limit) != 0:
            x = np.arange(x_limit[0], x_limit[1], 0.01)
            y = [f(i) for i in x]
            self.plt.plot(x, y, label='$' + text + '$')
        elif len(f_str) != 0 and len(x_limit) != 0:
            x = np.arange(x_limit[0], x_limit[1], 0.01)
            y = [eval(f_str) for x in x]
            self.plt.plot(x, y, label='$' + text + '$')
