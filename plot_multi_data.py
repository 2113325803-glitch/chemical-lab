import matplotlib.pyplot as plt          #这句导入matplotlib.pyplot库，用于绘图
import pandas as pd                       #这句导入pandas库，用于数据处理
from storage import load_experiments       # 这句导入storage模块中的load_experiments函数，用于从数据库加载实验数据

# 1. 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']         # 设置字体为SimHei，解决中文乱码问题
plt.rcParams['axes.unicode_minus'] = False          # 解决负数的中文乱码问题

# 2. 从数据库加载数据
experiments = load_experiments()
data = []
for exp in experiments:              # 遍历每个实验数据，将数据转换为字典格式，便于后续处理
    data.append({            #
        "温度(℃)": exp.temperature,
        "收率(%)": exp.yield_rate,
        "催化剂": exp.catalyst
    })

df = pd.DataFrame(data)        # 将数据转换为DataFrame格式
#DataFrame格式：{'温度(℃)': [25, 30, 35, 40, 45], '收率(%)': [80, 85, 90, 95, 100], '催化剂': ['催化剂A', '催化剂A', '催化剂A']}

# 3. 画图准备
plt.figure(figsize=(10, 6))     # 设置图形大小
#figsize=(10, 6)：设置图形大小为10x6英寸

# 4. 按“催化剂”分组，分别画线          unique()：返回所有唯一的催化剂种类
catalysts = df["催化剂"].unique()  # 拿到所有催化剂的种类：['催化剂A', '催化剂B']
colors = ['blue', 'red']  # 为不同的线指定颜色

for i, catalyst in enumerate(catalysts):          # 遍历每个催化剂     enumerate()：返回索引和值
    # 筛选出当前催化剂的数据，并按温度排序
    group = df[df["催化剂"] == catalyst].sort_values(by="温度(℃)")

    # 画线
    plt.plot(
        group["温度(℃)"],
        group["收率(%)"],
        marker='o',
        color=colors[i],
        linewidth=2,
        label=catalyst  # 图例名称
    )

# 5. 配置图表
plt.title("不同催化剂的温度-收率对比图", fontsize=16)
plt.xlabel("温度 (℃)", fontsize=12)
plt.ylabel("收率 (%)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()  # 显示图例

# 6. 保存并展示
plt.savefig("catalyst_comparison.png")
plt.show()
print("对比图已生成并保存为 catalyst_comparison.png")