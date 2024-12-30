from flask import Blueprint, jsonify, request
import pandas as pd
import os

Large_Area_Chart = Blueprint('Large_Area_Chart', __name__)

@Large_Area_Chart.after_request
def add_header(response):
    response.cache_control.no_store = True  # 禁止缓存
    return response
@Large_Area_Chart.route('/Large_Area_Chart', methods=['POST'])
def Large_Chart():
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
            data_column = column_names[1]  # 假设第二列是数据列，或者可以选择任意其他列

            data = {
                'data_title': data_column,
                'date': df[date_column].astype(str).tolist(),  # 将日期列转为字符串
                'data': df[data_column].tolist()  # 数据列
            }

            return jsonify(data)

        except Exception as e:
            print(f"Error occurred: {str(e)}")
            print(df.head())
            return jsonify({"error": str(e)}), 500
