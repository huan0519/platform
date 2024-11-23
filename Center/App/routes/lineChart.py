from flask import Blueprint, jsonify, request
import pandas as pd
import os

lineChart = Blueprint('lineChart', __name__)

@lineChart.after_request
def add_header(response):
    response.cache_control.no_store = True  # 禁止缓存
    return response
@lineChart.route('/lineChart', methods=['POST'])
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

            # # 转换为 JSON 格式（避免对数据进行任何排序或比较）
            # data = df.to_dict(orient='records')
            X = {df.columns[0]: df.iloc[:, 0].tolist()}
            data = {col: df[col].tolist() for col in df.columns[1:]}

            # 转换为 JSON 格式
            return jsonify({"X": X,"data": data}), 200

        except Exception as e:
            print(f"Error occurred: {str(e)}")
            print(df.head())
            return jsonify({"error": str(e)}), 500
