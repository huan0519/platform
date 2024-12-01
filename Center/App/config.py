from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy() # 数据库对象
migrate = Migrate() # 数据库迁移对象
api = Api()

REDIS_DB_URL = {
        'host': '127.0.0.1',
        'port': 6379,
        'password': '',
        'db': 0
    }

def init_exts(app):
    db.init_app(app)
    migrate.init_app(app,db)
    api.init_app(app)
