import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale, LabelEncoder
import tensorflow as tf
import xgboost as xgb


def perform_pca_and_train_models(file1, file2):
    # 读取训练数据和目标列
    df = pd.read_excel(file1, engine='openpyxl')
    X_train = df.iloc[:, 2:-1]  # 特征数据
    y_train = df['target']  # 目标列

    # 读取需要预测的数据
    df_predict = pd.read_excel(file2, engine='openpyxl')
    X_predict = df_predict.iloc[:, 1:]  # 预测数据

    # PCA降维
    data_scaled = scale(X_train)  # 对训练数据进行标准化
    covX = np.around(np.corrcoef(data_scaled.T), decimals=3)
    featValue, featVec = np.linalg.eig(covX.T)
    featValue = sorted(featValue, reverse=True)
    gx = featValue / np.sum(featValue)
    lg = np.cumsum(gx)
    k = [i for i in range(len(lg)) if lg[i] < 0.8]
    selectVec = np.matrix(featVec.T[k]).T
    finalData = np.dot(data_scaled, selectVec)

    # 目标变量处理（LabelEncoder）
    label_encoder = LabelEncoder()
    label_encoder.fit(y_train)
    y_train = label_encoder.transform(y_train)

    # 准备训练数据
    X = np.asarray(finalData)
    X_train, X_test, y_train, y_test = train_test_split(X, y_train, test_size=0.2, random_state=42)

    # 基础模型训练
    base_model1 = RandomForestClassifier(n_estimators=50, random_state=42)
    # base_model2 = GradientBoostingClassifier(n_estimators=50, random_state=42)
    base_model2 = xgb.XGBClassifier(n_estimators=50, random_state=42)

    base_model1.fit(X_train, y_train)
    base_model2.fit(X_train, y_train)

    # 模型预测
    pred_model1 = base_model1.predict(X_test)
    pred_model2 = base_model2.predict(X_test)

    # 构建元模型
    stacked_features = np.column_stack((pred_model1, pred_model2))
    meta_model = LogisticRegression(multi_class='ovr', solver='lbfgs', max_iter=1000)
    meta_model.fit(stacked_features, y_test)

    # 使用元模型进行预测
    stacked_predictions = meta_model.predict(stacked_features)
    # 获取每个类别的预测概率值（用于计算 ROC AUC）
    stacked_probabilities = meta_model.predict_proba(stacked_features)
    # 准确率
    accuracy = accuracy_score(y_test, stacked_predictions)
    print(accuracy)

    # 预测需要的数据
    data_scaled_predict = scale(X_predict)
    finalData_predict = np.dot(data_scaled_predict, selectVec)
    X_predict = tf.convert_to_tensor(finalData_predict, dtype=tf.float32)
    pred_model1_predict = base_model1.predict(X_predict)
    pred_model2_predict = base_model2.predict(X_predict)
    blend_features_predict = np.column_stack((pred_model1_predict, pred_model2_predict))
    blended_predictions_predict = meta_model.predict(blend_features_predict)

    # 将预测结果转换为汉字标签
    predicted_labels = label_encoder.inverse_transform(blended_predictions_predict)
    print(predicted_labels)

    # 混淆矩阵
    cm = confusion_matrix(y_test, stacked_predictions)
    cm_df = pd.DataFrame(cm, index=label_encoder.classes_, columns=label_encoder.classes_)
    print(cm_df)
    # 获取分类报告的数值
    classification_report_dict = classification_report(y_test, stacked_predictions, target_names=label_encoder.classes_, output_dict=True, zero_division=0)

    # 转换分类报告为数组格式
    classification_report_array = []
    for label, metrics in classification_report_dict.items():
        if label not in ['accuracy', 'macro avg', 'weighted avg']:  # 去除不需要的行
            classification_report_array.append([
                label,
                metrics['precision'],
                metrics['recall'],
                metrics['f1-score'],
                metrics['support']
            ])

    print(classification_report_dict)
    # 使用 predict_proba 计算 ROC AUC
    roc_auc = roc_auc_score(y_test, stacked_probabilities, multi_class='ovr')

    # 特征重要性
    feature_importance = {
        "RandomForest": base_model1.feature_importances_.tolist(),
        "GradientBoosting": base_model2.feature_importances_.tolist()
    }

    # 返回所有结果
    return accuracy, predicted_labels.tolist(), cm.tolist(),label_encoder.classes_.tolist(), classification_report_array, roc_auc, feature_importance
