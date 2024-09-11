import json
from logging_config import logger

def check(username, password):
    code = 0
    leftdays = 0
    with open('user_info.json', 'r', encoding='utf-8') as f:
        user_info = json.load(f)['users']
    logger.info(user_info)
    usernames = [x['username'] for x in user_info]
    if username in usernames:
        if password == [x['password'] for x in user_info if x["username"] == username][0]:
            if [x['leftdays'] for x in user_info if x["username"] == username][0] >0:
                msg = '登录验证成功!'
                leftdays = [x['leftdays'] for x in user_info if x["username"] == username][0]
                code = 1
            else:
                msg = '软件已过期!'
        else:
            msg = '密码错误！'
    else:
        msg = '用户名不存在！'
    return code, msg, leftdays
