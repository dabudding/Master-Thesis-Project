import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from matplotlib.patches import ConnectionPatch

def acc_plot(data):
    fig, ax = plt.subplots(1, 1)
    ax.plot(data['LeftFootAcc']['x'])

    #控小圖
    axins = ax.inset_axes((0.06, 0.1, 0.2, 0.3))    #前2位置後2大小
    axins.plot(data['LeftFootAcc']['x'])    

    xlim0 = 400
    xlim1 = 500

    ylim0 = -45#data['LeftFootAcc']['x'][250]
    ylim1 = 40

    axins.set_xlim(xlim0, xlim1)
    axins.set_ylim(ylim0, ylim1)

    # 原圖框
    tx0 = xlim0
    tx1 = xlim1
    ty0 = ylim0
    ty1 = ylim1
    sx = [tx0,tx1,tx1,tx0,tx0]
    sy = [ty0,ty0,ty1,ty1,ty0]
    ax.plot(sx,sy,"black")

    # 接線
    xy = (xlim0,ylim0)
    xy2 = (xlim1,ylim1)
    con = ConnectionPatch(xyA=xy2,xyB=xy,coordsA="data",coordsB="data",
            axesA=axins,axesB=ax)
    axins.add_artist(con)

    plt.title('Accelerometer X')
    plt.show()

    fig,ax = plt.subplots(1,1,figsize=(12,7))
    # plt.plot(data['LeftFootAcc']['x'][250:350])
    # plt.title('Accelerometer X')
def gyro_plot(data):
    fig, ax = plt.subplots(1, 1)
    ax.plot(data['LeftFootGyro']['z'])

    #控小圖
    axins = ax.inset_axes((0.06, 0.5, 0.21, 0.3))    #前2位置後2大小
    axins.plot(data['LeftFootGyro']['z'])    

    xlim0 = 400
    xlim1 = 480

    ylim0 = -400
    ylim1 = 550

    axins.set_xlim(xlim0, xlim1)
    axins.set_ylim(ylim0, ylim1)

    # 原圖框
    tx0 = xlim0
    tx1 = xlim1
    ty0 = ylim0
    ty1 = ylim1
    sx = [tx0,tx1,tx1,tx0,tx0]
    sy = [ty0,ty0,ty1,ty1,ty0]
    ax.plot(sx,sy,"black")

    # 接線
    xy = (xlim0,ylim1)
    xy2 = (xlim1,ylim1)
    con = ConnectionPatch(xyA=xy2,xyB=xy,coordsA="data",coordsB="data",
            axesA=axins,axesB=ax)
    axins.add_artist(con)

    plt.title('Gyroscope Z')
    plt.show()

    fig,ax = plt.subplots(1,1,figsize=(12,7))
    plt.plot(data['LeftFootGyro']['z'])
