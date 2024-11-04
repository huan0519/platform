import pandas as pd
import numpy as np


# 预处理函数：提取样品名称并清理非数值数据
def preprocess_data(file_path):
    # 读取原始数据
    data = pd.read_excel(file_path)

    # Step 1: 提取样品名称（第二行）
    sample_names = data.iloc[0].dropna().reset_index(drop=True)

    # Step 2: 移除非数值信息行并保留有效数据
    data_numeric = data.drop(index=[0, 1])  # 移除第一行和第二行
    data_numeric = data_numeric.applymap(lambda x: pd.to_numeric(x, errors='coerce')).dropna(how='all')
    data_numeric = data_numeric.dropna(axis=1, how='all')  # 删除完全为空的列

    # Step 3: 筛选和重命名'质量数'和'强度'列
    mass_columns = [col for col in data_numeric.columns if "Mass" in col or "SPECTRUM" in col]
    intensity_columns = [col for col in data_numeric.columns if "Unnamed" in col]

    mass_columns_renamed = {col: f"Mass_{i + 1}" for i, col in enumerate(mass_columns)}
    intensity_columns_renamed = {col: f"Intensity_{i + 1}" for i, col in enumerate(intensity_columns)}
    data_numeric_renamed = data_numeric.rename(columns={**mass_columns_renamed, **intensity_columns_renamed})

    return data_numeric_renamed, sample_names


# 1. 清洗数据
def load_and_clean_data(data):
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
        has_data = False
        for target_mass in target_masses:
            match = data.loc[data[col] == target_mass, intensity_col]
            if not match.empty:
                aligned_intensity.append(match.iloc[0])
                has_data = True
            else:
                aligned_intensity.append(np.nan)

        if has_data:
            aligned_data[f'Sample_{sample_id}_Intensity'] = aligned_intensity
            sample_id += 1
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
def standardize_data(file_path, output_path):
    # Step 1: 预处理数据
    data, sample_names = preprocess_data(file_path)

    # Step 2: 清洗数据
    data = load_and_clean_data(data)

    # Step 3: 筛选有效列并获取目标质量数
    mass_columns, intensity_columns = get_valid_columns(data)
    target_masses = get_target_masses(data, mass_columns)

    # Step 4: 对齐质量数并填充强度
    aligned_data = align_masses(data, mass_columns, intensity_columns, target_masses)

    # Step 5: 填充缺失值并标准化
    aligned_data = fill_missing_values(aligned_data)
    standardized_data = Zscore(aligned_data)

    # Step 6: 添加样品名称
    standardized_data.columns = ['Aligned_Mass'] + [f"Sample_{i}_Intensity ({sample_names[i - 1]})" for i in
                                                    range(1, len(standardized_data.columns))]

    # 保存结果
    standardized_data.to_excel(output_path, index=False)
    print(f"数据处理完成，结果已保存为 '{output_path}'")


