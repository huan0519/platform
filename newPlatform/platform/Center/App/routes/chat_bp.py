import logging

import markdown
import requests
from flask import Blueprint, request, jsonify

from Center.App.config.settings import api_key
from Center.App.services.error import error_response

chat_bp = Blueprint("chat_bp", __name__)

# 处理前端请求并代理到星火API
@chat_bp.route('/api/chat', methods=['POST'])
def chat():
    if request.is_json:
        try:
            req_data = request.get_json()  # 解析JSON
            logging.debug(f"收到的请求数据: {req_data}")  # 打印请求数据到日志
            user_message = req_data.get('messages')[0].get('content')

            if not user_message:
                return error_response("消息内容为空", 400)


            # 请求数据构建
            request_data = {
                'model': '4.0Ultra',
                'messages': [{'role': 'user', 'content': user_message}]
            }

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }

            # 向星火API发起请求
            response = requests.post(
                'https://spark-api-open.xf-yun.com/v1/chat/completions',
                json=request_data,
                headers=headers
            )
            # 检查返回的状态码是否为200
            if response.status_code == 200:
                try:
                    # 提取JSON响应数据
                    response_data = response.json()
                    chat_response = response_data.get('choices', [{}])[0].get('message', {}).get('content', '')
                    # 将 Markdown 转换为 HTML
                    ai_response = markdown.markdown(chat_response)

                    # 返回聊天内容给前端
                    return jsonify({'chatResponse': ai_response})

                except ValueError as e:
                    return jsonify({'error': 'Response is not in JSON format', 'details': str(e)}), 500
            else:
                # 处理失败情况
                return jsonify({'error': 'Request failed', 'status_code': response.status_code}), response.status_code


        except Exception as e:
            logging.error(f"聊天处理错误: {str(e)}")
            return error_response(f"聊天处理失败: {str(e)}")
        return error_response("请求格式错误，必须是JSON")
