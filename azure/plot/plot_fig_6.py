import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import gridspec

matplotlib.rcParams['font.sans-serif'] = ['SimHei']

# generate Fig 14a
fig, ax1 = plt.subplots()
fig.set_size_inches(7, 6)
plt.rcParams.update({'font.size': 20})

res = pd.read_csv('azure_result/cold_start.csv')

y2 = res["openwhisk"].values
for i in range(1, len(y2)):  # 累增部分
    y2[i] += y2[i - 1]
# y3 = []
# for i in range(1, 2800):
#     if i <= 2800 - len(y2):
#         y3.append(1)
#     else:
#         y3.append(y2[i - 2800 + len(y2)])
# for i in range(1, len(y3)):  # 累增部分
#     y3[i] += y3[i - 1]


# print(len(y2), y2[len(y2) - 1])
x2 = np.arange(0, len(y2))
plt.plot(x2 * 2, y2, label='OpenWhisk', color="#F0E68C", linewidth=5)
plt.axhline(y=y2[1506], color='tab:red', linestyle='--', linewidth=3)



y1 = res["pagurus"].values
for i in range(1, len(y1)):  # 累增部分
    y1[i] += y1[i - 1]

# y3 = []
# for i in range(1, 2800):
#     if i <= 300:
#         y3.append(0)
#     elif i <= 2800 - len(y1):
#         y3.append(1)
#     else:
#         y3.append(y1[i - 2800 + len(y1)])
#
# for i in range(1, len(y3)):  # 累增部分
#     y3[i] += y3[i - 1]


x1 = np.arange(0, len(y1))
plt.plot(x1 * 2, y1, label='Pagurus', color="#9370DB", linewidth=5)

plt.ylabel('总冷启动次数', fontsize=20)
plt.xlabel('函数ID', fontsize=20)

plt.axhline(y=y1[1506], color='tab:red', linestyle='--', linewidth=3)

ax1.set_xlim(0, 3000)
ax1.set_xticks([0, 500, 1000, 1500, 2000, 2500, 3000])
ax1.set_xticklabels(["0", "500", "1000", "1500", "2000", "2500", "3000"], fontsize=16)
ax1.set_ylim(0, 1)
ax1.set_yticks([0, y1[1506], 2000, 4000, 6000, 8000, y2[1506], 10000])
ax1.set_yticklabels(["0", str(y1[1506]), "2000", "4000", "6000", "8000", str(y2[1506]), "10000"], fontsize=16)
plt.legend(fontsize=20, loc="upper left")
fig.savefig("azure_result/fig_6.pdf", bbox_inches='tight')
