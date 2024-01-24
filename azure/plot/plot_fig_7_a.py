import numpy as np  # 引入numpy库
import pandas as pd
import matplotlib.pyplot as plt  # 引入matplotlib库的pyplot函数
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# 添加标题

# 设置正圆显示

res = pd.read_csv('azure_result/cold_start.csv')
y1 = res["openwhisk"].values
times = [0, 0, 0, 0, 0]

# 构造数据
labels = '1次以内', '2-5次', '6-10次', '11-30次', '大于30次'  # 设置显示标签

# 设置突出显示的标签
explode = [0, 0, 0, 0, 0]

# 设置标签颜色，浅黄，橙，绿，红，紫，青
colors = ['#FFC0CB','#FFFACD','#7FFFD4', '#87CEFA', '#DA70D6']

# generate fig_7_a
for i in range(0, len(y1)):
    if y1[i] <= 1:
        times[0] += 1
    elif y1[i] <= 5:
        times[1] += 1
    elif y1[i] <= 10:
        times[2] += 1
    elif y1[i] <= 30:
        times[3] += 1
    else:
        times[4] += 1
size = [times[0], times[1], times[2], times[3], times[4]]  # 设置每个标签对应的值
plt.xlabel("不同冷启动次数对应的函数占比", fontsize = 14)
# 开始绘制
plt.pie(size,  # 加载绘图数据
        explode=explode,  # 突出显示的项
        labels=labels,  # 各球队标签
        colors=colors,  # 颜色属性
        radius=1.0,  # 设置饼图半径
        counterclock=False,  # 设置为顺时针方向开始绘图
        labeldistance=1.1,  # 设置标签位置
        autopct='%.2f%%',  # 设置百分比格式，这里保存两位小数
        textprops={'fontsize': 12, 'color': 'black'},  # 设置文本属性,字体大小为12，颜色为黑
        wedgeprops={'linewidth': 0.7, 'edgecolor': 'black'},  # 设置边框，宽度为0.7，颜色为黑
        shadow=True,  # 添加阴影
        startangle=90  # 设置开始绘图的角度
        )
plt.savefig("azure_result/fig_7_a.pdf", bbox_inches='tight')
