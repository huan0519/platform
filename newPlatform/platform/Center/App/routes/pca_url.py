from flask import Blueprint, request, jsonify
import os
import pandas as pd
from App.services.PCA import perform_pca
import redis

PCA = Blueprint('PCA', __name__)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

@PCA.route('/pca', methods=['POST'])
def pre_pca():
    # 检查是否传递了强制更新缓存的参数
    force_update = request.args.get('force_update', '0') == '1'

    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

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
            df = pd.read_excel(input_path, header=None, engine='openpyxl')  # 不设定header，避免自动识别表头
            df = df.iloc[1:, 1:]  # 从第二行（索引1）第三列（索引2）开始读取数据
        except Exception as e:
            return jsonify({"error": f"Error reading Excel file: {str(e)}"}), 500

        # 如果需要强制更新缓存
        if force_update:
            try:
                # 删除Redis缓存
                redis_client.delete('pca_result')  # 删除之前存储的PCA结果
            except Exception as e:
                return jsonify({"error": f"Error deleting cache from Redis: {str(e)}"}), 500

        # 删除临时文件
        os.remove(input_path)
        # 执行 PCA 分析
        pca_result = perform_pca(df)  # 假设返回的是一个字典

        # 提取降维数据
        transformed_data = pca_result['rows']  # 取降维后的数据
        total = len(transformed_data)

        # 分页逻辑
        start = (page - 1) * per_page
        end = start + per_page
        paginated_rows = transformed_data[start:end]  # 提取分页数据

        # 构造返回结果
        response = {
            'columns': pca_result['columns'],  # 列名
            'rows': paginated_rows,            # 分页后的数据
            'total': total,                    # 总数据量
            'features': pca_result.get('features', []),                                  # 原始特征名
            'loadings_matrix': pca_result.get('loadings_matrix', [])                     # 载荷矩阵
        }

        return jsonify(response)
