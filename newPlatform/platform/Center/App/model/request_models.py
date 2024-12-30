from pydantic import BaseModel
from typing import List

class AnalyzeRequest(BaseModel):
    data: List[dict]
    chartType: str
    xAxis: str
    yAxis: str

    class Config:
        extra = "forbid"  # 禁止额外字段
