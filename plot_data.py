import matplotlib.pyplot as plt
import pandas as pd

# ⚠️ 极其关键的一步：解决 Matplotlib 中文显示乱码的问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号

# 1. 模拟 6 条化工实验数据（温度 vs 收率）
data = {
    "温度(℃)": [100, 120, 140, 160, 180, 200],
    "收率(%)": [60,  70,  85,  91,  88,  80]
}
df = pd.DataFrame(data)

# 2. 画图
plt.figure(figsize=(8, 5))  # 设置画布大小（宽8，高5）
# marker='o' 是让数据点显示为圆点，color='blue' 是蓝色
plt.plot(df["温度(℃)"], df["收率(%)"], marker='o', color='blue', linewidth=2, label='实验数据')

# 3. 添加标题和坐标轴标签
plt.title("反应温度与收率关系图", fontsize=14)
plt.xlabel("温度 (℃)", fontsize=12)
plt.ylabel("收率 (%)", fontsize=12)

# 4. 添加网格线（虚线，透明度0.7）
plt.grid(True, linestyle='--', alpha=0.7)

# 5. 显示图例
plt.legend()

# 6. 显示图表，并保存为图片
plt.show()
plt.savefig("temperature_vs_yield.png")
print("图表已生成并保存为 temperature_vs_yield.png")