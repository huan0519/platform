import numpy as np
from flask import Blueprint, jsonify, request
import pandas as pd
import os

boxplot = Blueprint('boxplot', __name__)

@boxplot.after_request
def add_header(response):
    response.cache_control.no_store = True  # 禁止缓存
    return response


def calculate_boxplot_data(data):
    print(data)
    result = []
    for arr in data:
        arr = sorted(arr)  # 确保数据有序
        n = len(arr)
        if n == 0:  # 跳过空数组
            result.append([])
            continue

        # Helper function for calculating quartiles
        def calc_position_value(position):
            if position.is_integer():
                return arr[int(position) - 1]  # 索引从1开始，减去1
            else:
                lower_idx = int(np.floor(position)) - 1
                upper_idx = int(np.ceil(position)) - 1
                fraction = position - np.floor(position)
                return arr[lower_idx] + (arr[upper_idx] - arr[lower_idx]) * fraction

        # Min and Max
        min_val = arr[0]
        max_val = arr[-1]

        # Q1, Median (Q2), Q3
        q1 = calc_position_value((n + 1) / 4)
        q2 = calc_position_value((n + 1) / 2)
        q3 = calc_position_value(3 * (n + 1) / 4)

        # Append results
        result.append([min_val, q1, q2, q3, max_val])
    return result
@boxplot.route('/boxplot', methods=['POST'])
def boxplot_chart():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file:
        # 将文件保存到临时路径
        current_dir = os.getcwd()
        file_path = os.path.join(current_dir, 'App', 'uploads', file.filename)
        file.save(file_path)

        try:
            # 根据文件后缀读取数据
            if file.filename.endswith('.xlsx') or file.filename.endswith('.xls'):
                df = pd.read_excel(file_path)
            elif file.filename.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file.filename.endswith('.txt'):
                df = pd.read_csv(file_path, delimiter='\t')  # 假设是制表符分隔的文件

            # 尝试将每一列转换为数值类型，非数值数据会变成 NaN
            df = df.apply(pd.to_numeric, errors='coerce')

            # 删除全是 NaN 的列
            df = df.dropna(axis=1, how='all')

            # 将数据框转为列表并计算箱线图数据
            boxplot_data = calculate_boxplot_data(df.values.T.tolist())  # 转置后逐列计算

            # 删除临时文件
            os.remove(file_path)

            return jsonify({
                "columns": df.columns.tolist(),  # 列名
                "boxplot_data": boxplot_data  # 箱线图数据
            })

        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return jsonify({"error": str(e)}), 500