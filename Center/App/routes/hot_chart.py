from flask import Blueprint, jsonify, request
import pandas as pd
import os
from scipy.stats import spearmanr, pearsonr

hot_chart = Blueprint('hot_chart', __name__)

@hot_chart.after_request
def add_header(response):
    response.cache_control.no_store = True  # 禁止缓存
    return response
@hot_chart.route('/hot_chart', methods=['POST'])
def hot__chart():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file:
        # 将文件保存到临时路径
        current_dir = os.getcwd()
        file_path = os.path.join(current_dir, 'App', 'uploads', file.filename)
        file.save(file_path)

        try:
            # 读取文件并强制将所有列的数据类型设置为字符串，避免数据类型问题
            if file.filename.endswith('.xlsx') or file.filename.endswith('.xls'):
                df = pd.read_excel(file_path)
            elif file.filename.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file.filename.endswith('.txt'):
                df = pd.read_csv(file_path, delimiter='\t')  # 假设是制表符分隔的文件

            # 读取完毕后删除临时文件
            os.remove(file_path)

            # 计算相关性矩阵
            spearman_corr = df.iloc[:, 1:].corr(method='spearman')  # Spearman 相关系数
            pearson_corr = df.iloc[:, 1:].corr(method='pearson')  # Pearson 相关系数

            # 将相关矩阵转换为字典格式，同时保留样本顺序
            spearman_dict = spearman_corr.to_dict(orient='index')
            pearson_dict = pearson_corr.to_dict(orient='index')

            # 将字典扁平化为键值对
            spearman_flat = {}
            pearson_flat = {}
            for row, cols in spearman_dict.items():
                for col, value in cols.items():
                    spearman_flat[f"{row}-{col}"] = value
            for row, cols in pearson_dict.items():
                for col, value in cols.items():
                    pearson_flat[f"{row}-{col}"] = value

            # 返回数据，附带样本顺序信息
            return jsonify({
                "spearman_matrix": spearman_flat,
                "pearson_matrix": pearson_flat
            })

        except Exception as e:
            return jsonify({'error': str(e)}), 500
