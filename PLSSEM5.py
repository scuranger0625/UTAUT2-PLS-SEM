import pandas as pd
import semopy
from sklearn.preprocessing import StandardScaler

# 讀取 Excel 文件，確保正確設置列名
file_path = r"C:\Users\Leon\Desktop\SunoAI之消費者族群研究 (回覆) (2).xlsx"
df = pd.read_excel(file_path)

# 將 gender 轉換為虛擬變量
df['gender'] = pd.get_dummies(df['gender'])['male']

# 使用已經編碼好的年齡列
# 假設年齡列已經被編碼為1-5的分類變量，名稱為 'age'
# 如果有其他的列名，請根據實際情況修改
age_column_name = 'age'

# 計算各構建的平均分數
df['PE'] = df[['PE1', 'PE2', 'PE3']].mean(axis=1)
df['EE'] = df[['EE1', 'EE2', 'EE3', 'EE4']].mean(axis=1)
df['SI'] = df[['SI1', 'SI2', 'SI3']].mean(axis=1)
df['FC'] = df[['FC1', 'FC2', 'FC3', 'FC4']].mean(axis=1)
df['HM'] = df[['HM1', 'HM2', 'HM3']].mean(axis=1)
df['PV'] = df[['PV1', 'PV2', 'PV3']].mean(axis=1)
df['HT'] = df[['HT1', 'HT2', 'HT3']].mean(axis=1)
df['BI'] = df[['BI1', 'BI2', 'BI3']].mean(axis=1)

# 創建交互項
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

# 標準化數據
scaler = StandardScaler()
scaled_df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# SEM 模型定義，刪除 age 和 gender 對 BI 的調節效應
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

# 模型擬合
mod = semopy.Model(model)
res = mod.fit(scaled_df)

# 路徑分析結果
params_df = mod.inspect()

# 將 z 值（t-value）改為 t 值，並格式化為小數點後兩位
params_df['t-value'] = params_df['z-value'].map(lambda x: f"{x:.2f}")

# 刪除原來的 z-value 列
params_df.drop(columns=['z-value'], inplace=True)

# 調整 p 值小數點顯示格式
params_df['p-value'] = params_df['p-value'].map(lambda x: f"{x:.5f}")

print(params_df)
