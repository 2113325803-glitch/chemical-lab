# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#====================================================================================
# from models import Experiment
# from storage import save_experiments, load_experiments
#
# # 1. 准备化工实验数据
# exp1 = Experiment(exp_id="CHEM-2026-10-02", temperature=150.5, pressure=2.5, catalyst="铂催化剂", yield_rate=88.5)
# exp2 = Experiment(exp_id="CHEM-2026-10-03", temperature=180.0, pressure=3.0, catalyst="镍催化剂", yield_rate=91.2)
#
# # 2. 存入数据库
# save_experiments([exp1, exp2])
# print("数据已成功写入数据库！")
#
# # 3. 从数据库读取验证
# all_experiments = load_experiments()
# print(f"当前数据库里有 {len(all_experiments)} 条实验记录：")
# for exp in all_experiments:
#     print(exp)
#
#============================================================================================

from models import Experiment
from storage import save_experiments

data = [
    # 催化剂A：最佳温度在 160℃ 左右
    Experiment("A-120", 120.0, 2.0, "催化剂A", 65.0),
    Experiment("A-140", 140.0, 2.0, "催化剂A", 78.5),
    Experiment("A-160", 160.0, 2.0, "催化剂A", 92.0),
    Experiment("A-180", 180.0, 2.0, "催化剂A", 89.0),
    Experiment("A-200", 200.0, 2.0, "催化剂A", 75.0),
    # 催化剂B：最佳温度偏低，在 140℃ 左右
    Experiment("B-120", 120.0, 2.0, "催化剂B", 80.0),
    Experiment("B-140", 140.0, 2.0, "催化剂B", 95.0),
    Experiment("B-160", 160.0, 2.0, "催化剂B", 85.0),
    Experiment("B-180", 180.0, 2.0, "催化剂B", 70.0),
    Experiment("B-200", 200.0, 2.0, "催化剂B", 55.0),
]
save_experiments(data)
print("5条真实化工实验数据已写入数据库")