from flask import Flask
from App.routes.urls import dataProcess
from App.routes.pca_url import PCA
from App.routes.predict_url import predict
from App.routes.getdata_json import data_json
from App.routes.lineChart import lineChart
from App.routes._3DChart import _3DChart
from App.routes.Large_Area_Chart import Large_Area_Chart
from App.routes.line_bar import line_bar
from App.routes.download_file import download
from App.routes.boxplot import boxplot
from App.routes.rose_chart import rose_chart
from App.routes.hot_chart import hot_chart
from App.routes.stack_bar import stack_bar
from App.routes.point_chart import point_chart
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
    # 配置数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/platform'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app
