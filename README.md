# Pagrus
源代码文件夹下的Pagurus文件夹包含了本实验所需要的代码、数据等内容。进行实验前将Pagurus目录移动到工作目录下，
其中，需要根据实际情况修改源代码中的路径。
## 代码文件
执行上述指令进入Pagurus目录
>cd Pagurus_code

experiment.sh文件是包含了配置各种软件依赖、创建镜像的指令，执行上述指令为实验配置好环境。
>sh experiment.sh

## 使用aws数据集进行实验：
进入aws目录，使用aws的数据进行测试。
>cd aws

开始进行第一组实验数据的测试，试验结束后会在不同系统对应的文件目录下生成结果文件result.csv
>python3 run_experiments.py 1

实验结束后，可以执行上述指令将得到的运行结果进行汇总，得到cold_start.csv、e2e_latency.csv、startup_time.csv以及memory.csv文件。
>python3 summary_from_results.py

进入plot目录，目录中包含了根据结果文件绘图的脚本，可以执行这些脚本进行绘图，得到分析结果。
>cd plot

## 使用azure数据集进行实验：
进入azure目录，使用azure的数据进行测试。
>cd azure

开始进行第一组实验数据的测试，试验结束后会在不同系统对应的文件目录下生成结果文件result.csv
>python3 run_experiments.py 1
> 
将得到的运行结果进行汇总，得到cold_start.csv、e2e_latency.csv以及memory.csv文件。
>python3 summary_from_results.py

进入plot目录，目录中包含了根据结果文件绘图的脚本，可以执行这些脚本进行绘图，得到分析结果。
>cd plot
