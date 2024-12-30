# 自动推荐图表参数
import pandas as pd


def recommend_chart_parameters(data: pd.DataFrame):
    try:
        if data.empty:
            return {"error": "数据为空，无法生成推荐参数"}

        columns = data.columns.tolist()
        numeric_columns = data.select_dtypes(include=["number"]).columns.tolist()

        if len(columns) == 1:
            # 如果只有一列，推荐饼图或雷达图
            return {
                "chartType": "饼图",
                "xAxis": columns[0],
                "yAxis": None,
                "message": "只有一列数据，推荐使用饼图展示分类占比"
            }

        if len(numeric_columns) >= 2:
            # 如果有两列数值数据，推荐散点图
            return {
                "chartType": "散点图",
                "xAxis": numeric_columns[0],
                "yAxis": numeric_columns[1],
                "message": "两列数值数据，推荐散点图展示变量关系"
            }

        if len(columns) >= 3:
            # 多列数据时，推荐雷达图或堆叠柱状图
            return {
                "chartType": "雷达图",
                "xAxis": None,
                "yAxis": None,
                "message": "多维数据，推荐使用雷达图展示多维对比"
            }

        # 默认推荐柱状图
        return {
            "chartType": "柱状图",
            "xAxis": columns[0],
            "yAxis": numeric_columns[0] if numeric_columns else None,
            "message": "默认推荐柱状图，适合分类与数值数据"
        }
    except Exception as e:
        return {"error": f"推荐参数生成失败: {str(e)}"}