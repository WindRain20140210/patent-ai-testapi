from flask import Flask
from api_v1 import api_v1
from api_v2 import api_v2

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(api_v1)
app.register_blueprint(api_v2)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)