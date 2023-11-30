import numpy as np

num = int(np.round(float(input('输入输出数列元素的个数')), 3))
if num == 1:
    array1 = [1]
else:
    array1 = [1, 1]
    for i in range(1, num - 1):
        array1.append(array1[i] + array1[i - 1])
print(array1)
