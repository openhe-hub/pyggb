import json

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

from pyggb.PyGeogebra import PyGeogebra


def init(setting=None):
    if setting is None:
        with open('./settings.json') as f:
            setting = json.load(f)
    figure = plt.figure(figsize=[setting["size"][0], setting["size"][1]])

    ax = axisartist.Subplot(figure, 111)
    figure.add_axes(ax)

    ax.axis[:].set_visible(False)  # 隐藏原来的实线矩形

    ax.axis["x"] = ax.new_floating_axis(0, 0, axis_direction="bottom")  # 添加x轴
    ax.axis["y"] = ax.new_floating_axis(1, 0, axis_direction="bottom")  # 添加y轴

    ax.axis["x"].set_axisline_style("-|>", size=1.0)  # 给x坐标轴加箭头
    ax.axis["y"].set_axisline_style("-|>", size=1.0)  # 给y坐标轴加箭头
    # ax.annotate(text='x', xy=(2, 0), xytext=(3, setting["y-text-offset"]))  # 标注x轴
    # ax.annotate(text='y', xy=(0, 2), xytext=(setting["x-text-offset"], 3))  # 标注y轴

    x_ticks = np.arange(setting["x-label"][0], setting["x-label"][1] + setting["x-label-step"], setting["x-label-step"])
    y_ticks = np.append(np.arange(setting["y-label"][0], 0, setting["y-label-step"]),
                        np.arange(setting["y-label-step"], setting["y-label"][1] + setting["y-label-step"],
                                  setting["y-label-step"]))
    plt.xticks(x_ticks)
    plt.yticks(y_ticks)  # 设置坐标轴标签
    plt.axis('equal')  # 强制单位距离等长
    return PyGeogebra(plt, figure, ax, setting)


def config():
    with open('./settings.json') as f:
        settings = json.load(f)
        return settings
