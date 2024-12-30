from flask import Blueprint, send_file, request
import os
import pandas as pd

download = Blueprint('download', __name__)


# 文件下载接口
@download.route('/download', methods=['GET'])
def download_file():
    # 获取请求参数中的文件名
    filename = request.args.get('filename')

    if filename:
        # 获取当前工作目录并组合成文件路径
        current_dir = os.getcwd()
        file_path = os.path.join(current_dir, 'App', 'download_file', filename)

        # 打印文件路径，方便调试
        print(file_path)

        # 判断文件是否存在
        if os.path.exists(file_path):
            # 返回文件，并指定下载时的文件名和 MIME 类型
            return send_file(
                file_path,
                as_attachment=True,
                download_name=filename,  # 设置下载文件名
                mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'  # Excel文件的MIME类型
            )
        else:
            return "File not found", 404
    else:
        return "Filename is required", 400
