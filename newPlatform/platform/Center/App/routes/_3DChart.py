from flask import Blueprint, jsonify, request
import pandas as pd
import os

_3DChart = Blueprint('_3DChart', __name__)

@_3DChart.after_request
def add_header(response):
    response.cache_control.no_store = True  # 禁止缓存
    return response
@_3DChart.route('/3DChart', methods=['POST'])
def line_Chart():
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

            # 获取列名作为 days 和 hours
            days = df.iloc[:, 0].tolist()
            hours = df.columns[1:].tolist()

            # 转换数据为所需的格式
            data = []
            for i, day in enumerate(days):
                for j, hour in enumerate(hours):
                    value = df.iloc[i, j + 1]  # j+1 是因为第一列是 day
                    data.append([i, j, value])

            # 构建 JSON 响应
            response = {
                "days": days,
                "hours": hours,
                "data": data
            }

            return jsonify(response)

        except Exception as e:
            print(f"Error occurred: {str(e)}")
            print(df.head())
            return jsonify({"error": str(e)}), 500
