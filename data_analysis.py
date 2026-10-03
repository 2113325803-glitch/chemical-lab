import pandas as pd

# 👇 加上这两行，专门解决 Pandas 中文对齐问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
from storage import load_experiments

# 1. 从数据库加载数据
experiments = load_experiments()

# 2. 把对象列表转成 Pandas 的 DataFrame（相当于一张 Excel 表）
data = []
for exp in experiments:
    data.append({
        "实验编号": exp.exp_id,
        "温度(℃)": exp.temperature,
        "压力(MPa)": exp.pressure,
        "催化剂": exp.catalyst,
        "收率(%)": exp.yield_rate
    })

df = pd.DataFrame(data)
print("===== 原始数据 =====")
print(df.to_markdown(index=False))
# 3. 数据清洗：剔除收率异常的记录（比如收率小于0或大于100的实验）
df_clean = df[(df["收率(%)"] >= 0) & (df["收率(%)"] <= 100)]
print("\n===== 清洗后的数据（剔除异常值） =====")
print(df_clean)

# 4. 统计分析：计算关键指标
print("\n===== 统计结果 =====")
print(f"平均温度：{df_clean['温度(℃)'].mean():.2f} ℃")
print(f"最高收率：{df_clean['收率(%)'].max()} %")
print(f"平均收率：{df_clean['收率(%)'].mean():.2f} %")

# 5. 筛选：只看使用“铂催化剂”的实验
print("\n===== 铂催化剂实验记录 =====")
pt_experiments = df_clean[df_clean["催化剂"] == "铂催化剂"]
print(pt_experiments)