import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# generate Fig 8_a
plt.rcParams.update({'font.size': 24})
fig, ax = plt.subplots()
fig.set_size_inches(10, 8)
res = pd.read_csv('azure_result/e2e_latency.csv')

y1 = res["pagurus"].values
x = np.arange(0, len(y1))
#for index in range(len(y2)):
 #   y2[index] = np.log10(y2[index]) + 1
ax.set_xlim(0, 3000)
ax.set_ylim(0, 10.0)
plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], fontsize=26)
# ax.set_yticks([-4, 0, 4, 8, 12, 16, 20, 24, 28])
# ax.set_yticklabels(["-4%", "0%", "4%", "8%", "12%", "16%", "20%", "24%", "28%"], fontsize=20)
ax.scatter(x * 1.3, y1, label='Pagurus', color="#87CEEB", s=16)
plt.ylabel('端到端延迟(s)', fontsize=22)
plt.xlabel('函数ID', fontsize=22)
ax.legend(fontsize=20, loc="upper right")
fig.savefig("azure_result/fig_8_a.pdf", bbox_inches='tight')

# generate Fig 8_a
plt.rcParams.update({'font.size': 24})
fig, ax = plt.subplots()
fig.set_size_inches(10, 8)
res = pd.read_csv('azure_result/e2e_latency.csv')

y1 = res["openwhisk"].values
x = np.arange(0, len(y1))
#for index in range(len(y2)):
 #   y2[index] = np.log10(y2[index]) + 1
ax.set_xlim(0, 3000)
ax.set_ylim(0, 10.0)
plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], fontsize=26)
# ax.set_yticks([-4, 0, 4, 8, 12, 16, 20, 24, 28])
# ax.set_yticklabels(["-4%", "0%", "4%", "8%", "12%", "16%", "20%", "24%", "28%"], fontsize=20)
ax.scatter(x * 1.3, y1, label='OpenWhisk', color="#F0E68C", s=16)
plt.ylabel('端到端延迟(s)', fontsize=22)
plt.xlabel('函数ID', fontsize=22)
ax.legend(fontsize=20, loc="upper right")
fig.savefig("azure_result/fig_8_b.pdf", bbox_inches='tight')


# generate Fig 8_c
plt.rcParams.update({'font.size': 24})
fig, ax = plt.subplots()
fig.set_size_inches(10, 8)
res = pd.read_csv('azure_result/e2e_latency.csv')
y1 = res["openwhisk/pagurus"].values
x = np.arange(0, len(y1))
ax.set_xlim(0, 3000)
ax.set_ylim(0, 8.0)
plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8], fontsize=26)
# ax.set_yticks([-4, 0, 4, 8, 12, 16, 20, 24, 28])
# ax.set_yticklabels(["-4%", "0%", "4%", "8%", "12%", "16%", "20%", "24%", "28%"], fontsize=20)
ax.scatter(x * 1.3, y1, label='OpenWhisk/Pagurus', color="#F0E68C", s=16)
plt.ylabel('标准化后的端到端延迟', fontsize=22)
plt.xlabel('函数ID', fontsize=22)
ax.legend(fontsize=20, loc="upper right")
fig.savefig("azure_result/fig_8_c.pdf", bbox_inches='tight')
