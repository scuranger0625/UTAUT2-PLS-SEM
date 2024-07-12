import pandas as pd
import semopy
from sklearn.preprocessing import StandardScaler

# 读取 Excel 文件，确保正确设置列名
file_path = r"C:\Users\Leon\Desktop\SunoAI之消費者族群研究 (回覆) (2).xlsx"
df = pd.read_excel(file_path)

# 将 gender 转换为虚拟变量
df['gender'] = pd.get_dummies(df['gender'])['male']

# 使用已经编码好的年龄列
# 假设年龄列已经被编码为1-5的分类变量，名称为 'age'
# 如果有其他的列名，请根据实际情况修改
age_column_name = 'age'

# 计算各构建的平均分数
df['PE'] = df[['PE1', 'PE2', 'PE3']].mean(axis=1)
df['EE'] = df[['EE1', 'EE2', 'EE3', 'EE4']].mean(axis=1)
df['SI'] = df[['SI1', 'SI2', 'SI3']].mean(axis=1)
df['FC'] = df[['FC1', 'FC2', 'FC3', 'FC4']].mean(axis=1)
df['HM'] = df[['HM1', 'HM2', 'HM3']].mean(axis=1)
df['PV'] = df[['PV1', 'PV2', 'PV3']].mean(axis=1)
df['HT'] = df[['HT1', 'HT2', 'HT3']].mean(axis=1)
df['BI'] = df[['BI1', 'BI2', 'BI3']].mean(axis=1)

# 创建交互项
df['age_PE'] = df[age_column_name] * df['PE']
df['age_EE'] = df[age_column_name] * df['EE']
df['age_SI'] = df[age_column_name] * df['SI']
df['age_FC'] = df[age_column_name] * df['FC']
df['age_HM'] = df[age_column_name] * df['HM']
df['age_PV'] = df[age_column_name] * df['PV']
df['age_HT'] = df[age_column_name] * df['HT']

df['gender_PE'] = df['gender'] * df['PE']
df['gender_EE'] = df['gender'] * df['EE']
df['gender_SI'] = df['gender'] * df['SI']
df['gender_FC'] = df['gender'] * df['FC']
df['gender_HM'] = df['gender'] * df['HM']
df['gender_PV'] = df['gender'] * df['PV']
df['gender_HT'] = df['gender'] * df['HT']

# 标准化数据
scaler = StandardScaler()
scaled_df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# SEM 模型定义，删除 age 和 gender 对 BI 的调节效应
model = """
BI ~ PE + EE + SI + FC + HM + PV + HT + age + gender + age_PE + age_EE + age_SI + age_FC + age_HM + age_PV + age_HT + gender_PE + gender_EE + gender_SI + gender_FC + gender_HM + gender_PV + gender_HT
PE ~~ age + gender
EE ~~ age + gender
SI ~~ age + gender
FC ~~ age + gender
HM ~~ age + gender
PV ~~ age + gender
HT ~~ age + gender

"""

# 模型拟合
mod = semopy.Model(model)
res = mod.fit(scaled_df)

# 路径分析结果
params_df = mod.inspect()

# 将 z 值（t-value）改为 t 值，并格式化为小数点后两位
params_df['t-value'] = params_df['z-value'].map(lambda x: f"{x:.2f}")

# 删除原来的 z-value 列
params_df.drop(columns=['z-value'], inplace=True)

# 调整 p 值小数点显示格式
params_df['p-value'] = params_df['p-value'].map(lambda x: f"{x:.5f}")

print(params_df)