import logging
from sparkai.core.messages import ChatMessage

from Center.App.services.parseResponse import parse_response
from Center.App.services.spark_service import get_spark_instance
from Center.App.services.template import generate_template

spark = get_spark_instance()

def analyze_data(data, chart_type, x_axis, y_axis):
    try:
        prompt = generate_template(data, chart_type, x_axis, y_axis)
        logging.debug(f"生成的 Prompt 内容：{prompt}")

        # 创建 ChatMessage 对象
        messages = [ChatMessage(role="user", content=prompt)]

        # 使用 ChatSparkLLM 生成回应
        response = spark.generate([messages])  # 传入消息列表，确保是一个列表格式

        # 打印 response 和 generations 的内容来调试
        logging.info(f"模型返回的响应： {response}")
        logging.info(f"Generations: {response.generations}")  # 打印 generations 的内容

        if isinstance(response.generations, list) and len(response.generations) > 0:
            for generation_list in response.generations:  # response.generations 是一个嵌套的列表
                if isinstance(generation_list, list) and len(generation_list) > 0:
                    generation = generation_list[0]
                    if hasattr(generation, 'text'):
                        logging.info(f"生成的文本: {generation.text}")
                    else:
                        logging.error("Error: 'text' field is missing in the generation object")
                else:
                    logging.error("Error: 'generation_list' is empty or not a list")
        else:
            logging.error("Error: 'generations' field missing or empty in response")

        # 提取生成的图表配置和分析结论
        chart_config, analysis_conclusion = parse_response(response.generations[0][0].text)

        return {
            "chartConfig": chart_config,
            "analysisConclusion": analysis_conclusion,
        }

    except Exception as e:
        logging.error(f"数据分析错误: {str(e)}")
        return {"error": f"数据分析失败: {str(e)}"}