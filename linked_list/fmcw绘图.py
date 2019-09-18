import matplotlib.pyplot as plt
import numpy as np
# X1 = np.linspace(0, 1600, 4000, endpoint=True)
# X2 = np.linspace(1600, 1700, 250, endpoint=True)
# Y1 = 0.025*X1
# Y2 = -0.4*X2 + 680
#
# X11 = np.linspace(33, 1633, 4000, endpoint=True)
# X22 = np.linspace(1633, 1733, 250, endpoint=True)
# Y3 = 0.025*X1
# Y4 = -0.4*X2 + 680
# plt.plot(X1, Y1)
# plt.plot(X2, Y2)
# plt.plot(X11, Y3)
# plt.plot(X22, Y4)
# Y5 = Y1-Y3
# plt.show()
# X111 = np.linspace(0, 1600, 400, endpoint=True)
# plt.plot(X111, Y5)
# plt.show()


def re_wave(x):
    while x >= 1700:
        x = x - 1700
    if x < 1600:
        a = 0.025*x
        return a
    else:
        b = -0.4*x + 680
        return b


def re_wave1(x):
    while x >= 1700:
        x = x - 1700
    if x < 1600:
        a = 0.025*x
        return a
    else:
        b = -0.4*x + 680
        return b


if __name__ == "__main__":
    i = 1
    a = 0
    b = 1600
    xx = []
    xx1 = []
    yy = []
    yy2 = []
    while i < 10:
        x = np.linspace(a, b+100, 400)
        x1 = np.linspace(a, b+100, 400)
        j = 0
        while j < 400:
            y = re_wave(x[j])
            yy1 = re_wave1(x1[j])
            xx.append(x[j])
            xx1.append(x1[j]+33)
            yy.append(y)
            yy2.append(yy1)
            j += 1
        i += 1
        a += 1700
        b += 1700

    plt.plot(xx, yy)
    plt.plot(xx1, yy2)
    plt.show()
