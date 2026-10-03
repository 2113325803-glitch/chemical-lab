import matplotlib.pyplot as plt
import pandas as pd
from storage import load_experiments

# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1. 从数据库加载真实数据
experiments = load_experiments()

# 2. 转成 DataFrame
data = []
for exp in experiments:
    data.append({
        "温度(℃)": exp.temperature,
        "收率(%)": exp.yield_rate
    })
df = pd.DataFrame(data)

# ⚠️ 极其关键的一步：按温度排序！
# 数据库查出来的数据不一定是按温度升序排列的。
# 如果顺序是乱的，Matplotlib 画出来的折线会来回折返，变成“蜘蛛网”。
df = df.sort_values(by="温度(℃)")

print("排序后的数据：")
print(df)

# 3. 画图
plt.figure(figsize=(8, 5))
plt.plot(df["温度(℃)"], df["收率(%)"], marker='o', color='green', linewidth=2, label='数据库实验数据')

plt.title("化工实验：温度与收率关系图", fontsize=14)
plt.xlabel("温度 (℃)", fontsize=12)
plt.ylabel("收率 (%)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

plt.savefig("db_temperature_vs_yield.png") # 先保存
plt.show()                                 # 再展示
print("图表已保存为 db_temperature_vs_yield.png")