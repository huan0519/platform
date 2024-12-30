from flask import Blueprint, jsonify, request
import pandas as pd
import os

line_bar = Blueprint('line_bar', __name__)

@line_bar.after_request
def add_header(response):
    response.cache_control.no_store = True  # 禁止缓存
    return response
@line_bar.route('/line_bar', methods=['POST'])
def Line_bar():
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
            # 确保所有列都被转换为字符串
            df = df.applymap(str)  # 将 `DataFrame` 中的所有值都转换为字符串

            # 替换所有 'None' 或 'NaN' 值为字符串 'null'
            df = df.replace(['None', 'NaN', 'nan'], 'null')

            # 获取列名并构建数据对象
            column_names = df.columns.tolist()  # 获取所有列名
            date_column = column_names[0]  # 假设第一列是日期列

            # 格式化日期列，只保留 YYYY-MM-DD
            df[date_column] = pd.to_datetime(df[date_column]).dt.strftime('%Y-%m-%d')
            # 获取除了第一列外的所有列名
            data_columns = column_names[1:]  # 从第二列开始的列名列表

            # 构建数据对象
            data = {
                'date': df[date_column].tolist(),  # 日期列
                'data_columns': data_columns,  # 数据列名
                'data': {col: df[col].tolist() for col in data_columns}  # 各列数据
            }

            return jsonify(data)

        except Exception as e:
            print(f"Error occurred: {str(e)}")
            print(df.head())
            return jsonify({"error": str(e)}), 500
