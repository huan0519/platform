# 路由文件
import uuid

from flask import Blueprint, request, send_file, jsonify
import os

from App.services.data_processing import *

dataProcess = Blueprint('dataProcess', __name__)

@dataProcess.route('/normalizeData', methods=['POST'])
def normalize_data_route():
    if 'file' not in request.files:
        return jsonify({"error": "没有上传文件"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "未选择文件"}), 400

     # 验证文件类型
    allowed_extensions = {'csv', 'xlsx'}
    if not file.filename.lower().endswith(tuple(allowed_extensions)):
        return jsonify({"error": "不允许的文件类型"}), 400

    # 保存上传的文件
    current_dir = os.getcwd()
    input_path = os.path.join(current_dir, 'App', 'uploads', file.filename)
    file.save(input_path)

    # 使用UUID生成随机输出文件名
    random_output_file_name = f"standardized_{uuid.uuid4()}.xlsx"
    # 定义输出文件路径
    output_path = os.path.join(current_dir, 'App', 'outputs', random_output_file_name)

    # 处理数据
    try:
        standardize_data(input_path, output_path)
    except Exception as e:
        return jsonify({"error": f"数据处理失败: {str(e)}"}), 500

    # 返回处理后的文件
    return send_file(output_path, as_attachment=True)



@dataProcess.route('/alignmentData', methods=['POST'])
def alignment_data_route():
    if 'file' not in request.files:
        return jsonify({"error": "没有上传文件"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "未选择文件"}), 400

     # 验证文件类型
    allowed_extensions = {'csv', 'xlsx'}
    if not file.filename.lower().endswith(tuple(allowed_extensions)):
        return jsonify({"error": "不允许的文件类型"}), 400

    # 保存上传的文件
    current_dir = os.getcwd()
    input_path = os.path.join(current_dir, 'App', 'uploads', file.filename)
    file.save(input_path)

    # 使用UUID生成随机输出文件名
    random_output_file_name = f"aligned_{uuid.uuid4()}.xlsx"
    # 定义输出文件路径
    output_path = os.path.join(current_dir, 'App', 'outputs', random_output_file_name)

    # 处理数据
    try:
        alignment_data(input_path, output_path)
    except Exception as e:
        return jsonify({"error": f"数据处理失败: {str(e)}"}), 500

    # 返回处理后的文件
    return send_file(output_path, as_attachment=True)

@dataProcess.route('/fillmissData', methods=['POST'])
def fillmiss_data_route():
    if 'file' not in request.files:
        return jsonify({"error": "没有上传文件"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "未选择文件"}), 400

     # 验证文件类型
    allowed_extensions = {'csv', 'xlsx'}
    if not file.filename.lower().endswith(tuple(allowed_extensions)):
        return jsonify({"error": "不允许的文件类型"}), 400

    # 保存上传的文件
    current_dir = os.getcwd()
    input_path = os.path.join(current_dir, 'App', 'uploads', file.filename)
    file.save(input_path)

    # 使用UUID生成随机输出文件名
    random_output_file_name = f"filled_{uuid.uuid4()}.xlsx"
    # 定义输出文件路径
    output_path = os.path.join(current_dir, 'App', 'outputs', random_output_file_name)

    # 处理数据
    try:
        fill_missing(input_path, output_path)
    except Exception as e:
        return jsonify({"error": f"数据处理失败: {str(e)}"}), 500

    # 返回处理后的文件
    return send_file(output_path, as_attachment=True)
