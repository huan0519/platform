import os
import logging
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 配置日志
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


# 环境变量配置
SPARKAI_URL = os.getenv('SPARKAI_URL', 'wss://spark-api.xf-yun.com/v4.0/chat')
SPARKAI_APP_ID = os.getenv('SPARKAI_APP_ID', '437e4882')
SPARKAI_API_SECRET = os.getenv('SPARKAI_API_SECRET', 'ZjczZTExZGMyZjAxOWRjNTQzMzA4YmRk')
SPARKAI_API_KEY = os.getenv('SPARKAI_API_KEY', '42bac03771f90f1324e54af8619ad0ca')
SPARKAI_DOMAIN = os.getenv('SPARKAI_DOMAIN', '4.0Ultra')
api_key = "nwRVSAullmCbgRJAncNO:JiKRxsIxntNLAkFhBxUG"