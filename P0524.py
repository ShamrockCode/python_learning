# 绘制横着的条形图
from matplotlib import pyplot as plt
import matplotlib

font = {'family': 'MicroSoft YaHei'}
matplotlib.rc("font", **font)
a = ["战狼2", "速度与激情8", "功夫瑜伽"]
b = [56.01, 26.94, 17.53]

# 设置图形大小
plt.figure(figsize=(12, 8), dpi=80)

plt.barh(range(len(a)), b, height=0.1, color="orange")

plt.yticks(range(len(a)), a)

plt.grid(alpha=0.4)

plt.show()

# =========================================================
