import json

from flask import Blueprint, jsonify, request
import pandas as pd
import os

data_json = Blueprint('data_json', __name__)

@data_json.after_request
def add_header(response):
    response.cache_control.no_store = True  # 禁止缓存
    return response
@data_json.route('/get_data', methods=['POST'])
def get_data():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

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

            # 分页逻辑
            total = len(df)
            start = (page - 1) * per_page
            end = start + per_page
            paginated_df = df.iloc[start:end]

            # 返回结果
            return jsonify({
                'columns': list(df.columns),
                'rows': paginated_df.values.tolist(),
                'total': total,
            })

        except Exception as e:
            print(f"Error occurred: {str(e)}")
            print(df.head())
            return jsonify({"error": str(e)}), 500
