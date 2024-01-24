import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
#from brokenaxes import brokenaxes
from matplotlib import gridspec


matplotlib.rcParams['font.sans-serif']=['SimHei']


# generate Fig.11


fig, ax2 = plt.subplots()
width = 0.23      # the width of the bars: can also be len(x) sequence
fig.set_size_inches(20, 10)
plt.rcParams.update({'font.size': 28})


x = np.arange(4)
pagurus = 147
prewarm = 554
sock = 560
openwhisk = 721
tmpx = np.arange(4)

ax2.set_xlim(-0.5, 3.5)
width = 0.5
p0 = ax2.bar([0], prewarm, width,color = "#C0C0C0", label = '')
ax2.bar_label(p0, label_type='edge')
#ax.bar(x-width, random, width, color = "#c82423",label='Pagurus')
p1 = ax2.bar([1], openwhisk, width,color = "#DA70D6",label = '')
ax2.bar_label(p1, label_type='edge')
p2 = ax2.bar([2], pagurus, width,color = "#87CEEB",label = '')
ax2.bar_label(p2, label_type='edge')
p3 = ax2.bar([3], sock, width,color = "#90EE90",label = '')
ax2.bar_label(p3, label_type='edge')
ax2.set_yticks([200, 400, 600, 800])
ax2.set_yticklabels(["200", "400", "600", "800"], fontsize=28)

ax2.set_xticks(x)
ax2.set_xticklabels(['OpenWhisk(启用预热)', 'OpenWhisk(禁用预热)', 'Pagurus', 'SOCK'], fontsize=28, rotation = 0)

ax2.set_ylabel('平均端到端延迟(ms)',fontsize = 30)

plt.yticks(fontsize=28)
fig.legend(fontsize=30,ncol = 4,loc = 'upper center', bbox_to_anchor=(0.45, 1.07))

# plt.show()
fig.savefig("aws_result/fig_5.pdf",bbox_inches='tight')






