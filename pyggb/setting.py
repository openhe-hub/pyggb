import json

import numpy as np
import matplotlib.pyplot as plt

from pyggb.PyGeogebra import PyGeogebra


def init(setting=None):
    if setting is None:
        with open('./settings.json') as f:
            setting = json.load(f)
    figure = plt.figure(figsize=[setting["size"][0], setting["size"][1]])

    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

    x_ticks = np.arange(setting["x-label"][0], setting["x-label"][1] + setting["x-label-step"], setting["x-label-step"])
    y_ticks = np.append(np.arange(setting["y-label"][0], 0, setting["y-label-step"]),
                        np.arange(setting["y-label-step"], setting["y-label"][1] + setting["y-label-step"],
                                  setting["y-label-step"]))
    plt.xticks(x_ticks)
    plt.yticks(y_ticks)  # 设置坐标轴标签
    plt.axis('equal')  # 强制单位距离等长
    return PyGeogebra(plt, figure, setting)


def config():
    with open('./settings.json') as f:
        settings = json.load(f)
        return settings
