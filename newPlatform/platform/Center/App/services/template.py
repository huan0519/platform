from jinja2 import Template

# 生成图表和分析结论的模板
def generate_template(data, chart_type, x_axis, y_axis):
    """
    生成 Prompt 模板，确保输出格式符合 API 要求。
    """
    prompt_template = """
    你是一个专业的数据分析师和前端开发专家。用户会提供原始数据和需求，你需要：
    1. 根据需求生成一个符合 ECharts 标准的图表配置（JSON 格式），前端可以直接渲染。
    2. 根据数据给出简洁的“数据分析结论”，总结关键趋势、特点或异常。

    以下是用户的需求：
    - 图表类型：{{ chart_type }}
    - 横坐标字段：{{ x_axis }}
    - 纵坐标字段：{{ y_axis }}
    - 数据内容（已格式化为 JSON）：{{ data | tojson }}

    输出内容格式如下：
    ```json
    {
        "chartConfig": {
            // 这里是 ECharts 图表配置
        },
        "analysisConclusion": "这里是数据分析的文字结论"
    }
    ```

    请严格按照上述格式生成内容，确保 JSON 部分可以被解析和渲染。
    """
    template = Template(prompt_template)
    return template.render(
        chart_type=chart_type,
        x_axis=x_axis,
        y_axis=y_axis,
        data=data,
    ).strip()