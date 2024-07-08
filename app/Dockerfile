# 使用官方 Python 基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件到工作目录
COPY . .

# 安装项目依赖
RUN pip install Flask

# 暴露端口，如果你的 Flask 应用程序监听的是不同的端口，确保在这里设置正确的端口号
EXPOSE 5000

# 定义环境变量
ENV FLASK_APP=app.py

# 指定启动命令
CMD ["python", "app.py "]