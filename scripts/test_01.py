# import os
# import sys
#
# from scripts.plot_multi_data import catalyst
#
# #sys:是一个内置的模块，用于与Python解释器进行交互。它提供了许多功能，例如获取命令行参数、执行系统命令、访问环境变量等。
# #os:是一个内置的模块，用于与操作系统进行交互。它提供了许多功能，例如获取当前工作目录、创建和删除文件和目录、读取和写入文件等。
#
# # 把项目根目录加入系统路径，这样 scripts 里面的脚本就能 import storage 模块了项目
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)     #这句话的作用是把BASE_DIR目录添加到系统的Python路径中，这样就可以在项目中导入BASE_DIR目录下的模块了。
#
# # 确保 images 文件夹存在 （如果不存在，就创建一个）
# images_dir = os.path.join(BASE_DIR,'images')     #这里的images是BASE_DIR目录下的images文件夹。
# #dir是一个内置的函数，用于获取当前工作目录。os.path.join是os.path模块中的一个函数，用于将多个路径片段连接成一个完整的路径。
#
# #======================获取与清洗数据===================
# import pandas as pd
# from storage import load_experiments
#
#
# #获取数据
# experiments = load_experiments()          #将load_experiments()函数的返回值赋值给experiments变量。
#
# #转换为 pandas DataFrame        将experiments列表转换为pandas DataFrame格式。
# data =[]      #定义一个空列表，用于存储转换后的数据。
#
# for exp in experiments:      #遍历experiments列表中的每个元素。
#     data.append(
#         {
#            "温度":exp.temperature,
#           "压力":exp.pressure,
#           "催化剂":exp.catalyst,
#           "反应速率":exp.yield_rate
#         }
#     )
# df = pd.DataFrame(data)      #将data列表转换为pandas DataFrame格式。
# #pd.DataFrame:是将pd里的DataFrame类导入的，用于创建DataFrame对象。
# #而pd又是从pandas模块中导入的，所以需要先导入pandas模块。
#
# print("=========原始数据==========")
#
# # 数据清洗：剔除收率＜0 或者 >100 的异常值
# df_clean = df[(df['反应速率'] >= 0) & (df['反应速率'] <= 100)]
# #df[()&()]:是pandas DataFrame对象的切片操作，用于筛选出符合条件的行。
# #里面是推导式，用于筛选出符合条件的行。df_clean是df的副本，用于存储清洗后的数据。
# print("=========清洗后的数据==========")
# print(df_clean)
#
#
# df_clean = df_clean.sort_values(by="温度")      #将df_clean按反应速率降序排序。
# #sort_values():是pandas DataFrame对象的排序操作，用于按指定的列进行排序。
# #by="温度":是按温度列进行排序。
#
# #======================数据可视化=======================
# import matplotlib.pyplot as plt
# #matplotlib:是用来绘制图表的库
# #plt:是matplotlib.pyplot模块的导入，用于绘制图
# # #pyplot是matplotlib模块中的一个绘图接口，用于绘制图表。
#
# #解决中文乱码，必须加这两行
# plt.rcParams['font.sans-serif']=['SimHei']  #设置字体为SimHei
# plt.rcParams['axes.unicode_minus']=False  #设置负号显示正常
# #recparams:是matplotlib.rcParams的导入，用于设置matplotlib的参数。
#
# #1.先要创建画布
# plt.figure(figsize=(10,6))
#
# #2. 提取分组
# catalysts = df_clean["催化剂"].unique()      #提取df_clean中催化剂列的唯一值。
# #unique():是pandas Series对象的唯一值操作，用于提取Series对象中的唯一值。
# #de_clean[]：可以将df_clean中的某一列提取出来，用于后续的处理。
# colors = ['blue','red']          #[]里面的参数是颜色列表
#
# #3. 绘制折线图
# for i, cat in enumerate(catalysts):      #遍历每个催化剂     enumerate()：返回索引和值
#     group = df_clean[df_clean["催化剂"] == cat]      #如果cat等于df_clean["催化剂"]中的某个值，就提取出对应的行。
#     plt.plot(                      #plot:是开始绘图用的函数
#         group["温度"],      #x轴是温度       写的时候x在前面，y在后面。
#         group["反应速率"],      #y轴是反应速率
#         label=cat,      #标签是催化剂
#         color=colors[i],
#         marker='0',
#         linewidth=2
#
#     )   #颜色是colors列表中的第i个颜色
#
#
#
# #4.图标装饰
# plt.title("反应速率与温度的关系")      #设置标题
# plt.xlabel("温度(℃)",fontsize=12)      #设置x轴标签
# plt.ylabel("收率(%)",fontsize=12)      #设置y轴标签
# plt.legend()      #显示图例
# plt.grid(True,linstyle='--')      #显示网格
# plt.xticks(rotation=45)      #设置x轴标签旋转角度
# plt.tight_layout()      #调整布局
#
# #保存图片（必须使用我们刚才定义的images_dir路径）
# save_path = os.path.join(images_dir,'lab_comarison.png')      #将images_dir和保存路径拼接成一个完整的路径。
# plt.savefig(save_path)
#
# print(f"\n 对比图已经保存到：{save_path}")
# plt.show()

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np      # numpy:用于数值计算
from scipy.optimize import curve_fit # curve_fit:用于拟合曲线

# ================= 1. 开天眼：路径修复 =================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
images_dir = os.path.join(BASE_DIR, "images")
os.makedirs(images_dir, exist_ok=True) # 创建images文件夹（如果不存在）并设置exist_ok=True，避免报错

from storage import load_experiments # 现在可以正常导入了

# ================= 2. 获取与清洗数据 =================
experiments = load_experiments()

data = []
for exp in experiments:
    data.append({"温度": exp.temperature, "收率": exp.yield_rate, "催化剂": exp.catalyst})
df = pd.DataFrame(data)

# 数据清洗：剔除异常值
df_clean = df[(df["收率"] >= 0) & (df["收率"] <= 100)]
# 排序：防折线图乱窜
df_clean = df_clean.sort_values(by="温度")

print("===== 清洗并排序后的数据 =====")
print(df_clean)

# ================= 3. 绘制多组对比图 =================
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(10, 6))
catalysts = df_clean["催化剂"].unique()
colors = ['blue', 'red']

for i, cat in enumerate(catalysts):
    group = df_clean[df_clean["催化剂"] == cat]
    plt.plot(group["温度"], group["收率"], marker='o', color=colors[i], linewidth=2, label=cat)

plt.title("催化剂 A vs B 温度-收率对比图", fontsize=16)
plt.xlabel("温度 (℃)", fontsize=12)
plt.ylabel("收率 (%)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# 保存图片（使用绝对路径）
save_path = os.path.join(images_dir, "lab_comparison.png")
plt.savefig(save_path)
print(f"\n✅ 对比图已保存到：{save_path}")

# ================= 4. Scipy 拟合预测 =================
# 提取催化剂B的数据
df_b = df_clean[df_clean["催化剂"] == "催化剂B"]
x_data = df_b["温度"].values
y_data = df_b["收率"].values

# 定义抛物线方程
def parabola(x, a, b, c):
    return a * x**2 + b * x + c

# 拟合
popt, pcov = curve_fit(parabola, x_data, y_data)      # curve_fit:用于拟合曲线(里面的参数是拟合函数、x数据、y数据)
a, b, c = popt      # popt:是拟合后的参数

# 计算极值点
optimal_temp = -b / (2 * a)
optimal_yield = parabola(optimal_temp, *popt)       # optimal_yield:是抛物线在极值点的值

print(f"\n===== 催化剂B 拟合结果 =====")
print(f"拟合方程: y = {a:.4f}x^2 + {b:.4f}x + {c:.4f}")
print(f"🎯 预测的最优温度: {optimal_temp:.2f} ℃")
print(f"🎯 理论最高收率: {optimal_yield:.2f} %")

plt.show()