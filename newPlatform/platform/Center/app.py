from App import create_app


if __name__ == '__main__':
    app = create_app()
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 设置最大文件大小为 16MB

    app.run(host='0.0.0.0', port=8000, debug=True)