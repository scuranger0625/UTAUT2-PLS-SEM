PE1 = [5, 3, 4, 2, 1, 2, 4, 4, 3, 5, 4, 4, 4, 5, 4, 4, 4, 3, 4, 4, 4, 4, 3, 5, 5, 4, 4, 4, 3, 4, 3, 5, 3, 4, 4, 4, 4, 3, 4, 5, 4, 5, 5, 3, 2, 4, 4, 4, 5, 5, 3]
PE2 = [4, 3, 3, 3, 1, 2, 5, 3, 3, 5, 4, 3, 4, 5, 3, 4, 4, 4, 4, 4, 5, 3, 3, 5, 5, 4, 3, 5, 4, 5, 2, 5, 4, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 3, 2, 4, 4, 5, 5, 5, 2]
PE3 = [5, 3, 4, 3, 1, 2, 4, 5, 3, 5, 4, 3, 5, 5, 4, 4, 4, 4, 3, 4, 4, 4, 3, 5, 4, 4, 3, 4, 4, 4, 2, 5, 4, 3, 3, 4, 4, 3, 3, 4, 4, 5, 5, 3, 4, 4, 2, 4, 5, 5, 3]

import numpy as np

# 定义计算因素负荷量、Cronbach's α、CR和AVE的函数
def calculate_loadings_alpha_cr_ave(scores):
    scores = np.array(scores)  # 转换成NumPy数组
    loadings = np.mean(scores, axis=1)  # 计算因素负荷量
    alpha = cronbach_alpha(scores)  # 计算Cronbach's α
    cr, ave = calculate_cr_ave(scores)  # 计算CR和AVE
    return loadings, alpha, cr, ave

# 定义Cronbach's α函数
def cronbach_alpha(items_scores):
    items_scores = np.array(items_scores)
    item_variances = items_scores.var(axis=1, ddof=1)
    total_variance = items_scores.sum(axis=0).var(ddof=1)
    n_items = items_scores.shape[0]
    return (n_items / (n_items - 1)) * (1 - (item_variances.sum() / total_variance))

# 定义CR和AVE函数
def calculate_cr_ave(items_scores):
    items_scores = np.array(items_scores)
    loadings = np.mean(items_scores, axis=1)
    squared_loadings = loadings ** 2
    cr = np.sum(squared_loadings) / (np.sum(squared_loadings) + np.sum(items_scores.var(axis=1, ddof=1)))
    ave = np.mean(squared_loadings)
    return cr, ave

# 将各个变量的观察值放入列表
PE1 = [5, 3, 4, 2, 1, 2, 4, 4, 3, 5, 4, 4, 4, 5, 4, 4, 4, 3, 4, 4, 4, 4, 3, 5, 5, 4, 4, 4, 3, 4, 3, 5, 3, 4, 4, 4, 4, 3, 4, 5, 4, 5, 5, 3, 2, 4, 4, 4, 5, 5, 3]
PE2 = [4, 3, 3, 3, 1, 2, 5, 3, 3, 5, 4, 3, 4, 5, 3, 4, 4, 4, 4, 4, 5, 3, 3, 5, 5, 4, 3, 5, 4, 5, 2, 5, 4, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 3, 2, 4, 4, 5, 5, 5, 2]
PE3 = [5, 3, 4, 3, 1, 2, 4, 5, 3, 5, 4, 3, 5, 5, 4, 4, 4, 4, 3, 4, 4, 4, 3, 5, 4, 4, 3, 4, 4, 4, 2, 5, 4, 3, 3, 4, 4, 3, 3, 4, 4, 5, 5, 3, 4, 4, 2, 4, 5, 5, 3]

# 放入二维数组中
PE_scores = np.array([PE1, PE2, PE3])

# 计算并输出因素负荷量、Cronbach's α、CR和AVE
loadings, alpha, cr, ave = calculate_loadings_alpha_cr_ave(PE_scores)
print(f"Loadings: {loadings}")
print(f"Cronbach's α: {alpha:.4f}")
print(f"CR: {cr:.4f}")
print(f"AVE: {ave:.4f}")


