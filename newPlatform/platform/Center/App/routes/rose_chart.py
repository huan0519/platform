from flask import Blueprint, jsonify, request
import pandas as pd
import os

rose_chart = Blueprint('rose_chart', __name__)

@rose_chart.after_request
def add_header(response):
    response.cache_control.no_store = True  # 禁止缓存
    return response
@rose_chart.route('/rose_chart', methods=['POST'])
def rose__chart():
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
            # 确保至少有两列数据
            if df.shape[1] < 2:
                return jsonify({'error': 'The file must have at least two columns'}), 400

            # 自动选择前两列作为 'value' 和 'name'
            first_column = df.columns[0]  # 假设第一列为 name
            second_column = df.columns[1]  # 假设第二列为 value

            # 重命名列以匹配目标格式
            df = df.rename(columns={first_column: 'name', second_column: 'value'})

            # 转换为所需格式，并按 value 列排序（从大到小）
            sorted_data = df[['name', 'value']].sort_values(by='value', ascending=False)

            # 转换为 JSON 格式
            data = sorted_data.to_dict(orient='records')

            return jsonify(data), 200

        except Exception as e:
            print(f"Error occurred: {str(e)}")
            print(df.head())
            return jsonify({"error": str(e)}), 500
