# 构建Python flask项目镜像
FROM python:3.9

# set the maintainer label
ARG TAG
RUN echo "Building image with tag: $TAG"

# 设置工作目录
WORKDIR /app

# 复制项目文件到工作目录
COPY . /app

# 安装依赖
RUN pip install -r requirements.txt

# 设置环境变量
ENV FLASK_APP=src/program.py
ENV FLASK_ENV=production

# 暴露端口
EXPOSE 5000

# 启动 Flask 应用
CMD ["flask", "run", "--host=0.0.0.0"]