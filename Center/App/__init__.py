from flask import Flask
from App.routes.urls import dataProcess

def create_app():
    app = Flask(__name__)

    app.register_blueprint(dataProcess)
    # 配置数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/platform'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app
