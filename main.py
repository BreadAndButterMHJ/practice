import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 修复负号问题
t = np.arange(0, 10, 0.1)
y = np.sin(2 * np.pi * t)
plt.figure(1)
plt.plot(t, y)
plt.show()
