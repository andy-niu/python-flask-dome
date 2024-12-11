# build stage
FROM python:3.10-alpine

# set working directory
WORKDIR /app

# copy project files to working directory
COPY . /app

# install dependencies
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple && rm -rf /root/.cache/pip

# set the maintainer label
ARG TAG
RUN echo "Building image with tag: $TAG"

# set environment variables
ENV FLASK_APP=src
ENV FLASK_ENV=production

# expose port
EXPOSE 5000

# run Flask application
CMD ["flask", "run", "--host=0.0.0.0"]