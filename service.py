import flask
from flask import request
from My_Utils_Server import check_login
import yaml
import time
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
app = flask.Flask(__name__)


@app.route("/login", methods=['GET', 'POST'])
def index():
    logging.info(f'请求地址:{request.url},客户端IP:{request.remote_addr}')
    data = request.get_json()
    code, msg, leftdays = check_login.check(data['username'],data['password'])
    return {"success":code, "message":msg, "leftdays": leftdays}


if __name__ == '__main__':
    app.run('0.0.0.0', 8989)
