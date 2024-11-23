import numpy as np
import pandas as pd
from sklearn.preprocessing import scale


def perform_pca(df, variance_threshold=0.8):
    """
    对输入的DataFrame执行PCA分析，返回主成分结果和解释方差信息。

    参数:
    df (DataFrame): 输入数据框，包含数值型数据。
    variance_threshold (float): 选择主成分时的累积方差阈值，默认值为0.8。

    返回:
    dict: 包含主成分数量、解释方差比例、转换后的数据的字典。
    """
    # 数据标准化
    data_scaled = scale(df)

    # 计算协方差矩阵
    covX = np.around(np.corrcoef(data_scaled.T), decimals=3)

    # 计算特征值和特征向量
    featValue, featVec = np.linalg.eig(covX.T)

    # 对特征值排序
    featValue_sorted = sorted(featValue, reverse=True)

    # 计算解释方差比例和累积解释方差
    explained_variance_ratio = featValue_sorted / np.sum(featValue_sorted)
    cumulative_variance = np.cumsum(explained_variance_ratio)

    # 选择满足累积方差阈值的主成分
    selected_components_indices = [i for i in range(len(cumulative_variance)) if
                                   cumulative_variance[i] < variance_threshold]

    # 构建选择的特征向量矩阵
    selectVec = np.matrix(featVec.T[selected_components_indices]).T
    selectVec = selectVec * (-1)

    # 转换数据到新的子空间
    transformed_data = np.dot(data_scaled, selectVec)

    # 返回结果
    return {
        "selected_components": len(selected_components_indices),
        "explained_variance_ratio": explained_variance_ratio.tolist(),
        "cumulative_variance": cumulative_variance.tolist(),
        "transformed_data": transformed_data.tolist()
    }
