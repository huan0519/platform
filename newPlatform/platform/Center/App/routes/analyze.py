from flask import Blueprint, request, jsonify
import logging
from flask import Flask, request, jsonify, render_template_string
from pydantic import ValidationError

from Center.App.model.request_models import AnalyzeRequest
from Center.App.services.analyzeData import analyze_data
from Center.App.services.error import error_response
from Center.App.services.parse_file import parse_uploaded_file

analyze_bp = Blueprint("analyze_bp", __name__)

# 数据分析路由
@analyze_bp.route('/api/analyze', methods=['POST'])
def analyze():
    if "file" in request.files:
        file = request.files["file"]
        try:
            data, columns, recommendations = parse_uploaded_file(file)
            return jsonify({
                "columns": columns,
                "recommendations": recommendations,
                "data": data.to_dict(orient="records"),
                "message": "文件上传成功，已生成推荐参数",
            })
        except Exception as e:
            logging.error(f"文件解析失败: {str(e)}")
            return error_response(f"文件解析失败: {str(e)}", 400)

    if request.is_json:
        try:
            req_data = request.json
            validated_data = AnalyzeRequest(**req_data)
            result = analyze_data(
                validated_data.data,
                validated_data.chartType,
                validated_data.xAxis,
                validated_data.yAxis,
            )
            return jsonify(result)
        except ValidationError as e:
            logging.error(f"数据验证失败: {str(e)}")
            return error_response(f"请求数据验证失败: {str(e)}", 400)
        except Exception as e:
            logging.error(f"数据分析处理失败: {str(e)}")
            return error_response(f"数据分析处理失败: {str(e)}", 500)

    return error_response("请求格式错误，必须是 JSON 或包含文件", 400)
