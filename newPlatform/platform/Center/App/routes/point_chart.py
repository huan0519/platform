from flask import Blueprint, jsonify, request
import pandas as pd
import os

point_chart = Blueprint('point_chart', __name__)

@point_chart.after_request
def add_header(response):
    response.cache_control.no_store = True  # 禁止缓存
    return response
@point_chart.route('/point_chart', methods=['POST'])
def point__chart():
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
                df = pd.read_excel(file_path, dtype=str)
            elif file.filename.endswith('.csv'):
                df = pd.read_csv(file_path, dtype=str)
            elif file.filename.endswith('.txt'):
                df = pd.read_csv(file_path, delimiter='\t', dtype=str)  # 假设是制表符分隔的文件

            # 读取完毕后删除临时文件
            os.remove(file_path)

            # 检查文件是否有至少两列（X 和 Y）
            if df.shape[1] < 2:
                return jsonify({'error': 'The file must contain at least two columns for X and Y data'}), 400

            # 提取 X 和 Y 数据
            data = df.iloc[:, :2].values.tolist()
            # 获取表头（列名）
            headers = df.columns.tolist()
            # 转换为 JSON 格式
            return jsonify({"data": data,"header":headers}), 200

        except Exception as e:
            print(f"Error occurred: {str(e)}")
            print(df.head())
            return jsonify({"error": str(e)}), 500
