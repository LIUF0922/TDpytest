import flask, json
from comms.database_utils import DBUtils

app = flask.Flask(__name__)


# 注册
@app.route('/register', methods=['post', 'get'])
def register():
    """
    :param username: not null
    :param passwd: not null
    :param re_passwd: not null
    :param sex:
    :param phone:
    :param email:
    :param remail:
    """
    data = flask.request.values
    username = data.get('username')
    passwd = data.get('passwd')
    re_passwd = data.get('re_passwd')
    re_sex = data.get('sex')
    re_phone = data.get('phone')
    re_email = data.get('email')
    re_remark = data.get('remark')
    # print('传入username的值：', username, '传入passwd的值：', passwd, '传入re_passwd的值：', re_passwd)
    if len(username) == 0:
        return json.dumps({"code": 1001, "msg": "用户名不能为空"}, ensure_ascii=False)
    elif len(passwd) == 0:
        return json.dumps({'code': 1002, "msg": "密码不能为空"}, ensure_ascii=False)
    elif len(re_passwd) == 0:
        return json.dumps({"code": 1003, "msg": "确认密码不能为空"}, ensure_ascii=False)
    elif not (6 <= len(username) <= 18 and 6 <= len(passwd) <= 18):
        return json.dumps({"code": 1004, "msg": "用户名和密码必须在6-18位之间"}, ensure_ascii=False)
    elif passwd != re_passwd:
        return json.dumps({"code": 1005, "msg": "确认密码必须和密码一致"}, ensure_ascii=False)
    db = DBUtils()
    count = db.find_count("select * from my_user where username=%s", (username,))
    print(count)
    if count != 0:
        db.close()
        return json.dumps({'code': 1006, 'msg': '用户名已存在'}, ensure_ascii=False)
    else:
        count = db.cud('insert into my_user(username,password,sex,phone,email,remark) values(%s,%s,%s,%s,%s,%s)',
                       (username, passwd, re_sex, re_phone, re_email, re_remark))
        db.close()
        if count == 1:
            return json.dumps({'code': 1000, 'msg': '注册成功'}, ensure_ascii=False)
        else:
            return json.dumps({'code': 9999, 'msg': '插入数据失败'}, ensure_ascii=False)


# 登录
@app.route('/user_login', methods=['post', 'get'])
def login():
    """
    :param username: not null
    :param passwd: not null
    """
    data = flask.request.values
    username = data.get('username')
    passwd = data.get('passwd')
    print('用户传入的username的值为：', username, '  转入passwd的值为：', passwd)
    if len(username) == 0:
        return json.dumps({"code": 1001, "msg": "用户名不能为空"}, ensure_ascii=False)
    elif len(passwd) == 0:
        return json.dumps({'code': 1002, "msg": "密码不能为空"}, ensure_ascii=False)
    else:
        db = DBUtils()
        count = db.find_count("select * from my_user where username=%s and password = %s", (username, passwd))
        db.close()
        if count == 0:
            return json.dumps({"code": 1003, "msg": "用户名或者密码错误"}, ensure_ascii=False)
        elif count > 0:
            return json.dumps({'code': 1000, 'msg': '登录成功'}, ensure_ascii=False)


app.run(debug=True)

if __name__ == '__main__':
    app.run()
