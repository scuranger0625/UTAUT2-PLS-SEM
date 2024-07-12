import numpy as np

# 相關係數矩陣，這裡是您提供的數據
correlation_matrix = np.array([
    [1.000, 0.916, 0.910],
    [0.916, 1.000, 0.895],
    [0.910, 0.895, 1.000]
])

# 計算相關係數矩陣的平均值
mean_corr = np.mean(correlation_matrix[np.triu_indices(correlation_matrix.shape[0], k=1)])

# 變數數量
num_vars = correlation_matrix.shape[0]

# 計算構念信度（CR）
CR = (num_vars * mean_corr) / (mean_corr + (num_vars - 1))

print(f"構念信度（CR）為: {CR:.4f}")



