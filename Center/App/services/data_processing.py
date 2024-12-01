import os

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# 预处理函数：提取样品名称并清理非数值数据
def preprocess_data(file_path):
    return data_numeric_renamed, sample_names


# 1. 清洗数据
def load_and_clean_data(data):
    data.dropna(thresh=len(data.columns) * 0.5, axis=0, inplace=True)
    data.dropna(thresh=len(data) * 0.5, axis=1, inplace=True)
    return data


# 2. 筛选有效的质量数和强度列
def get_valid_columns(data):
    return mass_columns[:num_samples], intensity_columns[:num_samples]


# 3. 统计并筛选高频质量数
def get_target_masses(data, mass_columns, frequency_threshold=0.3):
    return sorted(frequent_masses)


# 4. 对齐质量数并填充强度
def align_masses(data, mass_columns, intensity_columns, target_masses):
    return aligned_data


# 5. 填充缺失值
def fill_missing_values(aligned_data):
    aligned_data = aligned_data.interpolate(method='linear', axis=0)
    aligned_data.fillna(method='ffill', axis=0, inplace=True)
    aligned_data.fillna(method='bfill', axis=0, inplace=True)
    return aligned_data


# 6. 标准化数据
def Zscore(aligned_data):
    for col in aligned_data.columns[1:]:
        aligned_data[col] = (aligned_data[col] - aligned_data[col].mean()) / aligned_data[col].std()
    return aligned_data


# 数据对齐：处理数据并添加样品名称
def process_data(file_path, output_path, standardize=False):
        print(f"数据处理过程中发生错误: {e}")


# 归一化
def standardize_data(file_path, output_path):
    process_data(file_path, output_path, standardize=True)


# 数据对齐
def alignment_data(file_path, output_path):
    process_data(file_path, output_path, standardize=False)

# 缺失值填充
def fill_missing(file_path, output_path):
    # 读取数据文件
    df_original = pd.read_excel(file_path, header=None)

    # 分离前7行元数据（包括列名在内的所有元数据）
    metadata = df_original.iloc[:7, :]
    # 获取列名（第8行作为列名）
    columns = df_original.iloc[7, :].values

    # 提取有效数据部分（从第9行开始的数据），并设置列名
    df_valid = pd.read_excel(file_path, skiprows=8, header=None, names=columns)

    metadata.columns = df_valid.columns

    # 缺失值填充
    for i in range(len(df_valid.columns) // 2):
        mass_col = f'Mass{"" if i == 0 else "." + str(i)}'
        intensity_col = f'Intensity{"" if i == 0 else "." + str(i)}'

        # 检查列是否存在
        if mass_col in df_valid.columns and intensity_col in df_valid.columns:
            # 仅在mass和intensity各自列上进行插值和填充
            df_valid[mass_col] = df_valid[mass_col].interpolate(method='linear')
            df_valid[mass_col].fillna(method='ffill', inplace=True)
            df_valid[mass_col].fillna(method='bfill', inplace=True)

            df_valid[intensity_col] = df_valid[intensity_col].interpolate(method='linear')
            df_valid[intensity_col].fillna(method='ffill', inplace=True)
            df_valid[intensity_col].fillna(method='bfill', inplace=True)

    # 将元数据和处理后的有效数据合并
    df_final = pd.concat([metadata, df_valid], ignore_index=True)

    # 保存清洗和填充后的完整数据
    df_final.to_excel(output_path, index=False, header=False)
    print(f"清洗并填充后的数据已保存至 {output_path}")