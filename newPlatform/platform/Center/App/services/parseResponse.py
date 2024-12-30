# 解析响应中的图表配置和分析结论
import json
import logging


def parse_response(response_text):
    try:
        # 移除 Markdown 的代码块符号 ```json 和 ```
        if response_text.startswith("```json"):
            response_text = response_text[7:]  # 移除开头的 ```json
        if response_text.endswith("```"):
            response_text = response_text[:-3]  # 移除结尾的 ```

        # 尝试解析为 JSON
        parsed_response = json.loads(response_text)
        logging.info(f"成功解析响应 JSON：{parsed_response}")

        # 获取图表配置和分析结论
        chart_config = parsed_response.get("chartConfig", {})
        analysis_conclusion = parsed_response.get("analysisConclusion", "未生成分析结论")

        return chart_config, analysis_conclusion

    except json.JSONDecodeError as e:
        logging.error(f"解析响应失败，JSON 格式错误: {str(e)}")
        raise ValueError("返回结果不是有效的 JSON 格式")
    except Exception as e:
        logging.error(f"解析响应失败: {str(e)}")
        raise ValueError("解析响应失败")