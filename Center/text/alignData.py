import json
import os

import requests


# response = requests.get('http://127.0.0.1:5000/process')
# print(response.test)

# 定义要上传的文件路径
# 定义各个部分的路径
base_dir = '../App'
sub_dir = 'uploads'
file_name = 'lowerData.xlsx'

# 使用 os.path.join 构建完整路径
file_path = os.path.join(base_dir, sub_dir, file_name)
# 定义Flask服务的URL
url = 'http://127.0.0.1:5000//alignmentData'


# 检查文件是否存在
if os.path.exists(file_path):
    print(f"文件 {file_path} 存在")
else:
    print(f"文件 {file_path} 不存在")

try:
    with open(file_path, 'rb') as file:
        print(f"成功打开文件 {file_path}")
        files = {'file': file}
        response = requests.post(url, files=files)
        print("响应状态码:", response.status_code)
        # 检查请求是否成功
        if response.status_code == 200:
            print("文件处理成功，已保存为:", response.text)
        else:
            # 请求失败时，打印出响应内容而不是尝试解析JSON
            print("请求失败:", response.status_code)
            print("响应内容:", response.text)
except IOError as e:
    print(f"无法打开文件 {file_path}: {e}")

