import datetime
import functools

import jwt
from flask import g, request, Flask, current_app
from jwt import exceptions

# 构造header
headers = {
    'typ': 'jwt',
    'alg': 'HS256'
}

# 密钥
SALT = 'iv%i6xo7l8_t9bf_u!8#g#m*)*+ej@bek6)(@u3kh*42+unit='


def create_token(userId, isRoot):
    # 构造payload
    payload = {
        'userId': userId,
        'isRoot': isRoot,  # 自定义用户ID
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)  # 超时时间
    }
    result = jwt.encode(payload=payload, key=SALT, algorithm="HS256", headers=headers).decode('utf-8')
    return result


def verify_jwt(token, secret=None):
    """
    检验jwt
    :param token: jwt
    :param secret: 密钥
    :return: dict: payload
    """
    if not secret:
        secret = current_app.config['JWT_SECRET']

    try:
        payload = jwt.decode(token, secret, algorithms=['HS256'])
        return payload
    except exceptions.ExpiredSignatureError:  # 'token已失效'
        return -1
    except jwt.DecodeError:  # 'token认证失败'
        return -2
    except jwt.InvalidTokenError:  # '非法的token'
        return -3


def login_required(f):
    """让装饰器装饰的函数属性不会变 -- name属性"""
    '第1种方法,使用functools模块的wraps装饰内部函数'

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        try:
            if g.userId == -1:
                return {'code': 4001, 'message': 'token已失效'}, 401
            elif g.userId == -2:
                return {'code': 4001, 'message': 'token认证失败'}, 401
            elif g.userId == -3:
                return {'code': 4001, 'message': '非法的token'}, 401
            else:
                return f(*args, **kwargs)
        except BaseException as e:
            return {'code': 4001, 'message': '请先登录认证.'}, 401

    return wrapper


@app.before_request
def jwt_authentication():
    """
    1.获取请求头Authorization中的token
    2.判断是否以 Bearer开头
    3.使用jwt模块进行校验
    4.判断校验结果,成功就提取token中的载荷信息,赋值给g对象保存
    """
    auth = request.headers.get('Authorization')
    if auth and auth.startswith('Bearer '):
        "提取token 0-6 被Bearer和空格占用 取下标7以后的所有字符"
        token = auth[7:]
        "校验token"
        g.userId = None
        try:
            "判断token的校验结果"
            payload = jwt.decode(token, SALT, algorithms=['HS256'])
            "获取载荷中的信息赋值给g对象"
            g.userId = payload.get('userId')
        except exceptions.ExpiredSignatureError:  # 'token已失效'
            g.userId = -1
        except jwt.DecodeError:  # 'token认证失败'
            g.userId = -2
        except jwt.InvalidTokenError:  # '非法的token'
            g.userId = -3
# 测试接口
@app.route('/api/test', methods=['GET', 'POST'])
@login_required
def submit_test_info_():
    userId = g.userId
    return userId



