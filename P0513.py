import random

from matplotlib import pyplot as plt
import matplotlib

font = {'family': 'MicroSoft YaHei'}
matplotlib.rc("font", **font)

# x = range(2, 26, 2)
#
# y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]
#
#
# # 设置图片大小
# fig = plt.figure(figsize=(15, 6), dpi=80)
#
# # 绘图
# plt.plot(x, y)
#
# # 设置x轴的刻度
# plt.xticks(range(2, 25))
#
# # 保存图片
# plt.savefig("./sig_size.png")
#
# # 展示图形
# plt.show()

# ===============================================

# x = range(0, 120)
# y = [random.randint(20, 35) for i in range(120)]
#
# fig = plt.figure(figsize=(15, 6), dpi=80)
#
# plt.plot(x, y)
#
# # 调整x
# _x = list(x)
# _xtick_labels = ["10点{}分".format(i) for i in range(60)]
# _xtick_labels += ["11点{}分".format(i - 60) for i in range(60, 120)]
# # 取步长，数字与字符串一一对应，数据的长度一样
# plt.xticks(_x[::5], _xtick_labels[::5], rotation=45)  # rotation旋转的度数
#
# # 添加描述信息
# plt.xlabel("时间")
# plt.ylabel("温度/单位（摄氏度）")
# plt.title("10点到12点每分钟的气温变化情况")
#
# plt.show()

y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y_2 = [0, 0, 2, 5, 6, 4, 2, 2, 1, 1, 3, 5, 4, 6, 8, 0, 1, 2, 3, 4]
x = range(11, 31)

# 设置图形大小
plt.figure(figsize=(10, 6), dpi=80)

plt.plot(x, y_1, label="me")
plt.plot(x, y_2, label="mate")

# 设置x刻度
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x, _xtick_labels)
plt.yticks(range(0, 9))
# 绘制网格
plt.grid(alpha=0.3)

# 添加图例
plt.legend()

plt.show()
