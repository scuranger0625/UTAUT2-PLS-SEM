import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 根据 SEM 结果创建 DataFrame
data = {
    'Variable': ['PE', 'EE', 'SI', 'FC', 'HM', 'PV', 'HT', 'age', 'gender', 'age_PE', 'age_EE', 'age_SI', 'age_FC', 'age_HM', 'age_PV', 'age_HT', 'gender_PE', 'gender_EE', 'gender_SI', 'gender_FC', 'gender_HM', 'gender_PV', 'gender_HT'],
    'Estimate': [1.066379, -0.143884, -0.420159, 0.064230, 0.185842, 0.185705, 0.155736, 1.084411, -0.566516, -2.372393, 1.615392, -0.724662, 0.146900, -0.911195, -0.768638, 1.893401, 0.403807, -1.630465, 0.605016, 0.950203, 0.826761, 0.105533, -0.663625],
    'Std. Err': [0.278796, 0.278266, 0.355807, 0.317688, 0.238141, 0.464584, 0.463977, 0.454820, 0.506049, 0.621733, 0.769034, 0.747959, 0.557322, 0.809309, 0.970537, 0.899240, 0.620732, 0.621647, 0.466031, 0.745395, 0.581442, 0.618688, 0.364793],
    'p-value': [0.00013, 0.60511, 0.23766, 0.83978, 0.43516, 0.68936, 0.73713, 0.01711, 0.26293, 0.00014, 0.03568, 0.33262, 0.79210, 0.26021, 0.42838, 0.03524, 0.51535, 0.00872, 0.19421, 0.20239, 0.15505, 0.86456, 0.06888],
    't-value': [3.82, -0.52, -1.18, 0.20, 0.78, 0.40, 0.34, 2.38, -1.12, -3.82, 2.10, -0.97, 0.26, -1.13, -0.79, 2.11, 0.65, -2.62, 1.30, 1.27, 1.42, 0.17, -1.82]
}

df = pd.DataFrame(data)

# 提取男性和女性对行为意图的影响
gender_effects = df[df['Variable'].str.contains('gender_')]

# 提取不同年龄组对行为意图的影响
age_effects = df[df['Variable'].str.contains('age_')]

# 设置画布
plt.figure(figsize=(12, 6))

# 绘制男性和女性对行为意图的影响
plt.plot(gender_effects['Variable'], gender_effects['Estimate'], marker='o', linestyle='-', label='Gender Effects')

# 绘制不同年龄组对行为意图的影响
plt.plot(age_effects['Variable'], age_effects['Estimate'], marker='o', linestyle='-', label='Age Effects')

# 添加标题和标签
plt.title('Effects of Gender and Age on Behavioral Intention (BI)')
plt.xlabel('Effects')
plt.ylabel('Estimate')
plt.xticks(rotation=45)
plt.legend()

# 显示网格线
plt.grid(True)

# 显示图形
plt.tight_layout()
plt.show()
