# 控制层
from flask import jsonify
from flask_restful import Resource, marshal_with, fields, reqparse


import pandas as pd
import numpy as np


# 1. 加载和清洗数据
def load_and_clean_data(file_path):
    data = pd.read_excel(file_path, engine='openpyxl')
    # 删除缺失值超过50%的行和列
    data.dropna(thresh=len(data.columns) * 0.5, axis=0, inplace=True)
    data.dropna(thresh=len(data) * 0.5, axis=1, inplace=True)
    return data


# 2. 筛选有效的质量数和强度列
def get_valid_columns(data):
    mass_columns = [col for col in data.columns if 'Mass' in col and not data[col].isnull().all()]
    intensity_columns = [col for col in data.columns if 'Intensity' in col and not data[col].isnull().all()]
    num_samples = min(len(mass_columns), len(intensity_columns))
    return mass_columns[:num_samples], intensity_columns[:num_samples]


# 3. 统计并筛选高频质量数
def get_target_masses(data, mass_columns, frequency_threshold=0.3):
    all_masses = pd.Series(dtype='float')
    for col in mass_columns:
        all_masses = all_masses.append(data[col].dropna())
    mass_counts = all_masses.value_counts()
    threshold_count = len(mass_columns) * frequency_threshold
    frequent_masses = mass_counts[mass_counts >= threshold_count].index
    return sorted(frequent_masses)


# 4. 对齐质量数并填充强度
def align_masses(data, mass_columns, intensity_columns, target_masses):
    aligned_data = pd.DataFrame({'Aligned_Mass': target_masses})
    sample_id = 1
    for i in range(len(mass_columns)):
        col = mass_columns[i]
        intensity_col = intensity_columns[i]

        # 确保当前列包含数据
        if data[col].isnull().all() or data[intensity_col].isnull().all():
            continue

        aligned_intensity = []
        has_data = False  # 标记当前列是否有匹配的有效数据
        for target_mass in target_masses:
            # 精确匹配目标质量数
            match = data.loc[data[col] == target_mass, intensity_col]
            if not match.empty:
                aligned_intensity.append(match.iloc[0])  # 使用找到的第一个匹配值
                has_data = True
            else:
                aligned_intensity.append(np.nan)

        # 仅当存在有效数据时，才添加该列
        if has_data:
            aligned_data[f'Sample_{sample_id}_Intensity'] = aligned_intensity
            sample_id += 1
    return aligned_data


# 5. 线性插值并填充缺失值
def fill_missing_values(aligned_data):
    aligned_data = aligned_data.interpolate(method='linear', axis=0)
    aligned_data.fillna(method='ffill', axis=0, inplace=True)
    aligned_data.fillna(method='bfill', axis=0, inplace=True)
    return aligned_data


# 6. Z-score标准化处理
def standardize_data(aligned_data):
    for col in aligned_data.columns[1:]:
        aligned_data[col] = (aligned_data[col] - aligned_data[col].mean()) / aligned_data[col].std()
    return aligned_data


# 7. 主函数，执行所有步骤

def process_data(file_path, output_path):
    data = load_and_clean_data(file_path)
    mass_columns, intensity_columns = get_valid_columns(data)
    target_masses = get_target_masses(data, mass_columns)
    aligned_data = align_masses(data, mass_columns, intensity_columns, target_masses)
    aligned_data = fill_missing_values(aligned_data)
    aligned_data = standardize_data(aligned_data)
    aligned_data.to_excel(output_path, index=False)
    print(f"数据处理完成，结果已保存为 '{output_path}'")


