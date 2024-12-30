from flask import Flask
from Center.App.routes.urls import dataProcess
from Center.App.routes.pca_url import PCA
from Center.App.routes.predict_url import predict
from Center.App.routes.getdata_json import data_json
from Center.App.routes.lineChart import lineChart
from Center.App.routes._3DChart import _3DChart
from Center.App.routes.Large_Area_Chart import Large_Area_Chart
from Center.App.routes.line_bar import line_bar
from Center.App.routes.download_file import download
from Center.App.routes.boxplot import boxplot
from Center.App.routes.rose_chart import rose_chart
from Center.App.routes.hot_chart import hot_chart
from Center.App.routes.stack_bar import stack_bar
from Center.App.routes.point_chart import point_chart
from Center.App.routes.analyze import analyze_bp
from Center.App.routes.chat_bp import chat_bp
from flask_cors import CORS  # 导入 CORS 模块
def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(dataProcess)
    app.register_blueprint(PCA)
    app.register_blueprint(predict)
    app.register_blueprint(data_json)
    app.register_blueprint(lineChart)
    app.register_blueprint(_3DChart)
    app.register_blueprint(Large_Area_Chart)
    app.register_blueprint(line_bar)
    app.register_blueprint(download)
    app.register_blueprint(boxplot)
    app.register_blueprint(rose_chart)
    app.register_blueprint(hot_chart)
    app.register_blueprint(stack_bar)
    app.register_blueprint(point_chart)
    app.register_blueprint(analyze_bp)
    app.register_blueprint(chat_bp)
    # 配置数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/platform'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app
