from flask import Blueprint, request, send_file, jsonify
import os

from flask_cors import CORS

from App.services.PCA import *

PCA = Blueprint('PCA', __name__)
CORS(PCA, resources={r"/*": {"origins": "*"}})
@PCA.route('/pca', methods=['POST'])
def pre_pca():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # 验证文件类型
    allowed_extensions = {'csv', 'xlsx'}
    if not file.filename.lower().endswith(tuple(allowed_extensions)):
        return jsonify({"error": "不允许的文件类型"}), 400


    if file:
        # 保存上传的文件
        current_dir = os.getcwd()
        input_path = os.path.join(current_dir, 'App', 'uploads', file.filename)
        file.save(input_path)

        # 读取Excel文件
        try:
            # 从文件读取数据，跳过前两行和前两列
            df = pd.read_excel(input_path, header=None,engine='openpyxl')  # 不设定header，避免自动识别表头
            df = df.iloc[1:, 2:]  # 从第二行（索引1）第三列（索引2）开始读取数据
        except Exception as e:
            return jsonify({"error": f"Error reading Excel file: {str(e)}"}), 500

        # 调用PCA函数
        try:
            pca_result = perform_pca(df)
            return jsonify(pca_result)

        except Exception as e:
            return jsonify({"error": f"Error during PCA analysis: {str(e)}"}), 500

