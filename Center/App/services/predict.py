from flask import Flask, request, jsonify
import os
import pandas as pd
import numpy as np
import tensorflow as tf
from keras.src.utils import to_categorical
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder  # 导入 LabelEncoder

# 创建 Flask 应用
app = Flask(__name__)

# 基础模型和元模型（假设你已经定义了模型，这里用占位符）
from keras import Sequential
from tensorflow.keras.layers import Dense

# PCA 和模型训练的核心过程封装在一个函数中
def perform_pca_and_train_models(file1, file2):
    # 1. 读取训练数据和目标列
    df = pd.read_excel(file1, engine='openpyxl')
    X_train = df.iloc[:, 2:-1]  # 特征数据
    y_train = df['target']  # 目标列
    print(X_train.head())

    # 2. 读取需要预测的数据
    df_predict = pd.read_excel(file2, engine='openpyxl')
    X_predict = df_predict.iloc[:, 1:]  # 预测数据
    print(X_predict.head())
    # 3. 执行PCA降维
    from sklearn.preprocessing import scale
    data_scaled = scale(X_train)  # 对训练数据进行标准化
    covX = np.around(np.corrcoef(data_scaled.T), decimals=3)
    featValue, featVec = np.linalg.eig(covX.T)
    featValue = sorted(featValue, reverse=True)
    gx = featValue / np.sum(featValue)
    lg = np.cumsum(gx)
    k = [i for i in range(len(lg)) if lg[i] < 0.8]
    selectVec = np.matrix(featVec.T[k]).T
    selectVec = selectVec * (-1)
    finalData = np.dot(data_scaled, selectVec)
    print(finalData)

    # 4. 处理目标变量：汉字标签转数值
    label_encoder = LabelEncoder()
    label_encoder.fit(y_train)

    # 转换为数值标签
    y_train = label_encoder.transform(y_train)
    print(y_train)

    # 5. 准备训练数据
    X = np.asarray(finalData)

    # 6. 划分数据集
    X_train, X_test, y_train, y_test = train_test_split(X, y_train, test_size=0.2, random_state=42)

    # 7. 训练基础模型
    # 创建基本模型
    base_model1 = RandomForestClassifier(n_estimators=50, random_state=42)
    base_model2 = GradientBoostingClassifier(n_estimators=50, random_state=42)

    # 拟合基本模型
    base_model1.fit(X_train, y_train)
    base_model2.fit(X_train, y_train)

    # 使用基本模型进行预测
    pred_model1 = base_model1.predict(X_test)
    pred_model2 = base_model2.predict(X_test)

    # 构建元特征
    stacked_features = np.column_stack((pred_model1, pred_model2))

    # 8. 使用元模型
    meta_model = LogisticRegression()
    meta_model.fit(stacked_features, y_test)

    # 9. 结合预测结果
    stacked_predictions = meta_model.predict(stacked_features)

    # 10. 计算准确率
    accuracy = accuracy_score(y_test, stacked_predictions)  # 不需要 np.argmax，因为 y_test 已经是整数标签
    print(accuracy)
    # 11. 对需要预测的数据进行预测
    data_scaled_predict = scale(X_predict)
    finalData_predict = np.dot(data_scaled_predict, selectVec)
    print(finalData_predict)
    X_predict = tf.convert_to_tensor(finalData_predict, dtype=tf.float32)
    print(X_predict)
    pred_model1_predict = base_model1.predict(X_predict)
    pred_model2_predict = base_model2.predict(X_predict)
    blend_features_predict = np.column_stack((pred_model1_predict, pred_model2_predict))
    blended_predictions_predict = meta_model.predict(blend_features_predict)
    print(blended_predictions_predict)
    # 12. 将预测结果转换为汉字标签
    # predicted_classes = np.argmax(blended_predictions_predict, axis=0)  # 获取预测的类别索引
    predicted_labels = label_encoder.inverse_transform(blended_predictions_predict)  # 转换为汉字标签

    # 返回预测结果和准确率
    return accuracy, predicted_labels.tolist()