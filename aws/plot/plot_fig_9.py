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
ax.set_ylim(-0.4, 2.8)
ax.set_yticks([-4, 0, 4, 8, 12, 16, 20, 24, 28])
ax.set_yticklabels(["-4%", "0%", "4%", "8%", "12%", "16%", "20%", "24%", "28%"], fontsize=20)
ax.set_xlim(0, 1)
ax.set_xticks([0, 1200, 2400, 3600, 4800, 6000, 7200])
ax.set_xticklabels(["0", "1200", "2400", "3600", "4800", "6000", "7200"], fontsize=20)

'''
res = pd.read_csv('aws/Memory/openwhisk/Memory.csv')
x = res["time"].values
y1 = res["mem_load"].values
ax.plot(x, y1, label='OpenWhisk', color="#F0E68C", linewidth=3, ms=12)
'''
# plt.axhline(y=y2[1506], color='tab:red', linestyle='--', linewidth=3)

res = pd.read_csv('aws/Memory/pagurus/Memory.csv')
x = res["time"].values
y2 = res["mem_load"].values
ax.plot(x, y2, label='Pagurus', color="#87CEEB", linewidth=3, ms=12)

res = pd.read_csv('aws/Memory/prewarm/Memory.csv')
y3 = res["mem_load"].values
ax.plot(x, y3, label='OpenWhisk', color="#C0C0C0", linewidth=3, ms=12)

'''
res = pd.read_csv('aws/Memory/sock/Memory.csv')
y4 = res["mem_load"].values
ax.plot(x, y4, label='Sock', color="#90EE90", linewidth=3, ms=12)
'''

ax.plot(x, y2 - y3, label='差值', color="#c82423", linewidth=3, ms=12)
plt.ylabel('内存使用率', fontsize=20)
plt.xlabel('时间(s)', fontsize=20)


ax.legend(fontsize=16, loc="upper right")
fig.savefig("aws_result/fig_9.pdf", bbox_inches='tight')
