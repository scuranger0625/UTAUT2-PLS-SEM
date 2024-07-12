import pandas as pd
import matplotlib.pyplot as plt

# 创建 DataFrame，包含性别和不同年龄段的估计值
data = {
    'Variable': ['PE', 'EE', 'SI', 'FC', 'HM', 'PV', 'HT'],
    'Male_Estimate': [0.403807, -1.630465, 0.605016, 0.950203, 0.826761, 0.105533, -0.663625],
    'Female_Estimate': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    'Age_20_and_below': [0.5, 0.2, 0.4, 0.6, 0.3, 0.5, 0.2],
    'Age_21_30': [0.4, -0.1, 0.5, 0.7, 0.2, 0.3, -0.1],
    'Age_31_40': [0.3, -0.5, 0.6, 0.8, 0.4, 0.2, -0.2],
    'Age_41_50': [0.5, -1.2, 0.4, 1.0, 0.5, 0.4, -0.3],
    'Age_51_and_above': [0.6, -0.8, 0.3, 0.9, 0.3, 0.3, -0.5],
}

df = pd.DataFrame(data)

# 设置画布和子图
fig, axs = plt.subplots(2, 1, figsize=(15, 10))  # 调整图形大小

# 性别对行为意图的影响比较
axs[0].plot(df['Variable'], df['Male_Estimate'], marker='o', linestyle='-', color='blue', label='Male')
axs[0].plot(df['Variable'], df['Female_Estimate'], marker='s', linestyle='--', color='red', label='Female')
axs[0].set_title('Comparison of Gender Effects on Behavioral Intention (BI)', fontsize=16, pad=20)  # 增加标题和图之间的间距

axs[0].set_ylabel('Estimate', fontsize=14)
axs[0].legend(fontsize=12)
axs[0].tick_params(axis='both', which='major', labelsize=12)
axs[0].grid(True)

# 不同年龄段对行为意图的影响比较
axs[1].plot(df['Variable'], df['Age_20_and_below'], marker='o', linestyle='--', color='green', label='Age 20 and below')
axs[1].plot(df['Variable'], df['Age_21_30'], marker='s', linestyle='--', color='purple', label='Age 21-30')
axs[1].plot(df['Variable'], df['Age_31_40'], marker='^', linestyle='--', color='orange', label='Age 31-40')
axs[1].plot(df['Variable'], df['Age_41_50'], marker='D', linestyle='--', color='brown', label='Age 41-50')
axs[1].plot(df['Variable'], df['Age_51_and_above'], marker='x', linestyle='--', color='pink', label='Age 51 and above')
axs[1].set_title('Comparison of Age Effects on Behavioral Intention (BI)', fontsize=16, pad=20)  # 增加标题和图之间的间距

axs[1].set_ylabel('Estimate', fontsize=14)
axs[1].legend(fontsize=12)
axs[1].tick_params(axis='both', which='major', labelsize=12)
axs[1].grid(True)

# 调整子图之间的间距
plt.tight_layout(pad=4.0)
plt.show()





