import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 修复负号问题
t = np.arange(0, 10, 0.1)
y = np.sin(2 * np.pi * t)
y1 = np.cos(2 * np.pi * t)
xLabel1 = np.arange(0, t[-1], np.pi)
xLabel2 = ['%dΠ' % i for i in range(len(xLabel1))]
xLabel2[0] = 0
plt.figure(1)
plt.plot(t, y)
plt.xticks(xLabel1, xLabel2)

plt.figure(2)
plt.subplot(2, 1, 1)
plt.plot(t, y)
plt.xticks(xLabel1, xLabel2)
plt.subplot(2, 1, 2)
plt.plot(t, y1)
plt.xticks(xLabel1, xLabel2)

plt.figure(3)
plt.plot(t, t, 'r')
plt.show()
