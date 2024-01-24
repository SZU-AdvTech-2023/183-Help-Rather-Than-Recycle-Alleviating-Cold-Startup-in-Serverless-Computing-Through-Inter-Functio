import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import gridspec

matplotlib.rcParams['font.sans-serif'] = ['SimHei']

# generate Fig 9
fig, ax = plt.subplots()
fig.set_size_inches(14, 8)
plt.rcParams.update({'font.size': 20})
ax.set_ylim(0, 1)
ax.set_yticks([0, 20, 40, 60, 80, 100])
ax.set_yticklabels(["0%", "20%", "40%", "60%", "80%", "100%"], fontsize=20)
ax.set_xlim(0, 1)
ax.set_xticks([0, 3600, 7200, 10800, 14400, 18000, 21600, 25200, 28800])
ax.set_xticklabels(["0", "1", "2", "3", "4", "5", "6", "7", "8"], fontsize=20)

res = pd.read_csv('azure_result/Memory/openwhisk/Memory.csv')
x = res["time"].values
y1 = res["mem_load"].values
ax.plot(x, y1, label='OpenWhisk', color="#F0E68C", linewidth=3, ms=12)


res = pd.read_csv('azure_result/Memory/pagurus/Memory.csv')
x = res["time"].values
y2 = res["mem_load"].values
ax.plot(x, y2, label='Pagurus', color="#87CEEB", linewidth=3, ms=12)

y3 = res["mem_load"].values;
for i in range(len(y2)):
    y3[i] = y2[i] - y1[i]
ax.plot(x, y3, label='差值', color="#c82423", linewidth=3, ms=12)

plt.ylabel('内存使用率', fontsize=20)
plt.xlabel('时间(h)', fontsize=20)

ax.legend(fontsize=16, loc="upper right")
fig.savefig("azure_result/fig_10.pdf", bbox_inches='tight')
