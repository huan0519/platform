import pandas as pd
from Center.App.services.recommend_parameters import recommend_chart_parameters


# 文件上传处理函数
def parse_uploaded_file(file):
    try:
        filename = file.filename
        if filename.endswith(".csv"):
            data = pd.read_csv(file)
        elif filename.endswith(".xls") or filename.endswith(".xlsx"):
            data = pd.read_excel(file)
        else:
            raise ValueError("仅支持 CSV 或 Excel 文件格式")

        if data.empty:
            raise ValueError("文件内容为空")

        columns = data.columns.tolist()
        recommendations = recommend_chart_parameters(data)

        return data, columns, recommendations
    except Exception as e:
        raise ValueError(f"文件解析失败: {str(e)}")