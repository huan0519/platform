import json
import numpy as np
import pandas as pd
from sklearn.preprocessing import scale
import redis

# 连接到Redis数据库
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=False)

def perform_pca(df, variance_threshold=0.8, cache_expire=3600):
    """
    对输入的DataFrame执行PCA分析，返回降维结果、载荷矩阵和解释方差信息，并将结果缓存到Redis。

    参数:
    df (DataFrame): 输入数据框，包含数值型数据。
    variance_threshold (float): 累积方差阈值，决定选取的主成分数，默认0.8。
    cache_expire (int): Redis缓存过期时间，单位秒，默认1小时。

    返回:
    dict: 包含降维结果、载荷矩阵和解释方差信息的字典。
    """
    # 缓存键
    cache_key = 'pca_result'
    cached_result = redis_client.get(cache_key)

    if cached_result:
        # 如果缓存存在，直接返回
        return json.loads(cached_result)

    # 数据标准化
    data_scaled = scale(df)

    # 计算协方差矩阵
    covX = np.corrcoef(data_scaled.T)

    # 计算特征值和特征向量
    featValue, featVec = np.linalg.eig(covX)

    # 排序特征值和特征向量
    featValue_sorted_indices = np.argsort(featValue)[::-1]
    featValue_sorted = featValue[featValue_sorted_indices]
    featVec_sorted = featVec[:, featValue_sorted_indices]

    # 计算解释方差比例和累积解释方差
    explained_variance_ratio = featValue_sorted / np.sum(featValue_sorted)
    cumulative_variance = np.cumsum(explained_variance_ratio)

    # 选择满足累积方差阈值的主成分
    n_components = np.argmax(cumulative_variance >= variance_threshold) + 1
    selected_featVec = featVec_sorted[:, :n_components]

    # 计算主成分载荷矩阵（权重矩阵）
    loadings_matrix = selected_featVec.T

    # 转换数据到新的子空间
    transformed_data = np.dot(data_scaled, selected_featVec)

    # 创建降维结果 DataFrame
    pca_df = pd.DataFrame(
        transformed_data,
        columns=[f"PC{i + 1}" for i in range(n_components)]
    )
    pca_df.insert(0, 'id', range(1, len(pca_df) + 1))

    # 检查是否需要替换默认列名
    if all(isinstance(col, (int, float)) for col in df.columns):
        # 如果列名全为数字，替换为 feature1, feature2, ...
        df.columns = [f"feature{i + 1}" for i in range(df.shape[1])]

    # 缓存的结果结构
    pca_result = {
        "columns": pca_df.columns.tolist(),
        "rows": pca_df.astype({"id": int}).values.tolist(),
        "explained_variance_ratio": explained_variance_ratio.tolist(),
        "cumulative_variance": cumulative_variance.tolist(),
        "loadings_matrix": loadings_matrix.tolist(),
        "features": df.columns.tolist()
    }

    # 缓存结果到 Redis
    redis_client.setex(cache_key, cache_expire, json.dumps(pca_result))

    return pca_result
