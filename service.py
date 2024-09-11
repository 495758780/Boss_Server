import flask
from flask import request
from My_Utils_Server import check_login, my_ocr
import json
import logging
import yaml
from logging_config import logger
from PIL import Image
import numpy as np
from cnocr import CnOcr
import time
from io import BytesIO

app = flask.Flask(__name__)
ocr = CnOcr()
@app.route("/login",methods=['GET', 'POST'])
def index():
    data = request.get_json()
    code, msg, leftdays = check_login.check(data['username'],data['password'])
    logger.info(f'{code},{msg}')
    return {"success":code, "message":msg, "leftdays": leftdays}

@app.route("/ocr", methods=['POST'])
def img_to_str():
    t1 = time.time()
    file = request.files['file']
    img = Image.open(BytesIO(file.read()))
    if img.mode != 'RGB':
        img = img.convert('RGB')
    ocr_result = ocr.ocr(img)
    print(ocr_result)
    print(f'请求总时间：{time.time() - t1}')
    return {"ok": 1}


if __name__ == '__main__':
    app.run('127.0.0.1', 8090)