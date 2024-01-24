import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
# from brokenaxes import brokenaxes
from matplotlib import gridspec

matplotlib.rcParams['font.sans-serif'] = ['SimHei']

# generate Fig.3

data_prewarm = pd.read_csv('aws_result/startup_time.csv')
openwhisk = list(data_prewarm['openwhisk'].values)
pagurus = list(data_prewarm['pagurus'].values)
prewarm = list(data_prewarm['prewarm'].values)
# random = list(data_prewarm['random'].values)
sock = list(data_prewarm['sock'].values)


tick_labels = ['bot', '   tok', ' ', ' ', 'etl', ' ',
               'ddns', ' ', 'rek', ' ', 'rep', ' ',
               'file', ' ', ' ', '   pod', ' ', ' ', ' ', ' ',
               '   cart', ' ', ' ', ' ', ' ',  ' ', ' ', ' ',' ',
               ' ', '', 'eco', ' ', ' ', ' ', ' ', ' ', ' ']

plt.rcParams.update({'font.size': 24})
fig, ax = plt.subplots()
fig.set_size_inches(30, 15)
x = np.arange(38)

ax.axvline(x=0.5, color='tab:gray', linestyle='--', linewidth=3)
ax.axvline(x=2.5, color='tab:gray', linestyle='--', linewidth=3)
ax.axvline(x=5.5, color='tab:gray', linestyle='--', linewidth=3)
ax.axvline(x=6.5, color='tab:gray', linestyle='--', linewidth=3)
ax.axvline(x=9.5, color='tab:gray', linestyle='--', linewidth=3)
ax.axvline(x=10.5, color='tab:gray', linestyle='--', linewidth=3)
ax.axvline(x=13.5, color='tab:gray', linestyle='--', linewidth=3)
ax.axvline(x=17.5, color='tab:gray', linestyle='--', linewidth=3)
ax.axvline(x=23.5, color='tab:gray', linestyle='--', linewidth=3)
ax.axhline(y=0.22, color='tab:red', linestyle='--', linewidth=3)

ax.set_ylim(0,1.7)
ax.set_xlim(-0.8, 37.5)
ax.set_xticklabels(tick_labels, fontsize=28)
plt.xticks(x, tick_labels)

ax.plot(x, openwhisk, color='#DA70D6',linewidth=3,label='OpenWhisk(禁用预热)',marker='x', ms=12)
ax.plot(x, prewarm, color='#C0C0C0',linewidth=3,label='OpenWhisk(启用预热)',marker='*', ms=12)
# ax.plot(x, random, color='#c82423',linewidth=3,label='Pagurus-WRS',marker='s', ms=12)
ax.plot(x, pagurus, color='#87CEEB',linewidth=3,label='Pagurus',marker='o', ms=12)
ax.plot(x, sock, color='#90EE90',linewidth=3,label='SOCK',marker='^', ms=12)

plt.xlabel('应用程序名称', fontsize = 28)
plt.ylabel('平均启动延迟/s',fontsize = 28)
ax.legend(ncol=2, fontsize=24,loc = 'upper left',handlelength=1.5)
fig.savefig("aws_result/fig_3.pdf",bbox_inches='tight')