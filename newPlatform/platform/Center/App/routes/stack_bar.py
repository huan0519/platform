from flask import Blueprint, jsonify, request
import pandas as pd
import os

stack_bar = Blueprint('stack_bar', __name__)

@stack_bar.after_request
def add_header(response):
    response.cache_control.no_store = True  # 禁止缓存
    return response
@stack_bar.route('/stack_bar', methods=['POST'])
def stack__chart():
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

            # 假设第一列为 xAxisData，第二列及之后为 seriesData
            if len(df.columns) < 2:
                return jsonify({'error': 'Invalid file format. The file must have at least two columns.'}), 400

            x_axis_data = df.iloc[:, 0].tolist()  # 第一列的数据，去除表头
            series_data = {col: df.iloc[0:, idx].tolist() for idx, col in enumerate(df.columns[1:],start=1)}

            response = {
                "seriesData": series_data,
                "xAxisData": x_axis_data
            }
            return jsonify(response)

        except Exception as e:
            return jsonify({'error': str(e)}), 500
