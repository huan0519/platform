from sparkai.llm.llm import ChatSparkLLM

from Center.App.config.settings import SPARKAI_URL, SPARKAI_APP_ID, SPARKAI_API_KEY, SPARKAI_API_SECRET, SPARKAI_DOMAIN

# 初始化星火大模型
spark = ChatSparkLLM(
    spark_api_url=SPARKAI_URL,
    spark_app_id=SPARKAI_APP_ID,
    spark_api_key=SPARKAI_API_KEY,
    spark_api_secret=SPARKAI_API_SECRET,
    spark_llm_domain=SPARKAI_DOMAIN,
    streaming=False,
)

# 提供一个获取 Spark 实例的方法（可选）
def get_spark_instance():
    return spark