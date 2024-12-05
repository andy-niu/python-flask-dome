# 构建Python flask项目镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 复制项目文件到工作目录
COPY . /app

# 安装依赖
RUN pip install -r requirements.txt

# 暴露端口
EXPOSE 5000

# 启动Flask应用
CMD ["python", "./flaskr/app.py"]