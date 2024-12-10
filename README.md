### Flaskr
```
# 创建虚拟环境
$ python3 -m venv .venv
$ . .venv/bin/activate

# windows cmd 激活虚拟环境
$ py -3 -m venv .venv
$ .venv\Scripts\activate


# 安装依赖
$ pip install -r requirements.txt
$ pip install -e .

# 运行
$ flask --app src init-db
$ flask --app src run --debug
```

### 数据库迁移
```
$ flask --app src db init
$ flask --app src db migrate
$ flask --app src db upgrade
```

### Deploy Server
```
$ docker-compose up --build -d

```

### Dome
- http://117.72.68.141:5000/

### Repository
- http://ddns.mzmalls.com:2052/andy/python-flask

## Reference
- https://flask.palletsprojects.com/zh-cn/stable/
- https://flask-sqlalchemy.palletsprojects.com/en/stable/quickstart/
- https://flask-migrate.readthedocs.io/en/latest/index.html
- https://bootstrap-flask.readthedocs.io/en/stable/