from flask import Blueprint, request, send_file, jsonify
import os

from flask_cors import CORS

from App.services.predict import *

predict = Blueprint('predict', __name__)
CORS(predict, resources={r"/*": {"origins": "*"}})
@predict.route('/predict', methods=['POST'])
def disease_predict():
    # 检查是否有文件上传
    if 'file1' not in request.files or 'file2' not in request.files:
        return jsonify({"error": "缺少文件"}), 400

    file1 = request.files['file1']
    file2 = request.files['file2']

    # 确保文件名不为空
    if file1.filename == '' or file2.filename == '':
        return jsonify({"error": "文件名为空"}), 400

    # 验证文件类型
    allowed_extensions = {'csv', 'xlsx'}
    if not file1.filename.lower().endswith(tuple(allowed_extensions)):
        return jsonify({"error": "不允许的文件类型"}), 400
    if not file2.filename.lower().endswith(tuple(allowed_extensions)):
         return jsonify({"error": "不允许的文件类型"}), 400

    # 保存文件到临时路径
    temp_dir = os.path.join(os.getcwd(), 'uploads')
    os.makedirs(temp_dir, exist_ok=True)
    file1_path = os.path.join(temp_dir, file1.filename)
    file2_path = os.path.join(temp_dir, file2.filename)
    file1.save(file1_path)
    file2.save(file2_path)

    try:
        # 执行PCA降维并训练模型
        accuracy, predictions, cm, class_labels, classification_report, roc_auc, feature_importance = perform_pca_and_train_models(
            file1_path, file2_path)

        # 删除临时文件
        os.remove(file1_path)
        os.remove(file2_path)

        # 将所有信息打包成字典返回
        return jsonify({
            "accuracy": accuracy,
            "predictions": predictions,
            "confusion_matrix": cm,
            "class_labels":  class_labels,
            "classification_report": classification_report,
            "roc_auc": roc_auc,
            "feature_importance": feature_importance
        })

    except Exception as e:
        return jsonify({"error": f"处理过程中出错: {str(e)}"}), 500