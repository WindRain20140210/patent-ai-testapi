# 使用官方的 Python 镜像作为基础镜像
FROM python:3.9-slim
# 设置工作目录
WORKDIR /app
# 将当前目录的内容复制到工作目录
COPY . .
# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt
# 设置环境变量，以便 Flask 在容器中运行
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
# 启动 Flask 应用
CMD ["flask", "run"]
# 暴露端口
EXPOSE 5000
