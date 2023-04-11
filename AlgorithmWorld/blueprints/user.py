from flask import Blueprint, request

from AlgorithmWorld.dao import userDao
from AlgorithmWorld.extensions import db
from AlgorithmWorld.model.model import User
from AlgorithmWorld.utils.jwtUtils import create_token
from AlgorithmWorld.utils.md5 import password_md5

user_bp = Blueprint('user', __name__)


@user_bp.route('/login', methods=['POST'])
def login():
    data = request.form
    username = data.get("username")
    password = data.get("password")
    password = password_md5(password)
    # 首先判断是否有此用户
    user = db.session.query(User).filter(User.username == username).first()

    if user is None:
        return {"code": 200, "message": "该用户不存在"}

    # judge password
    if password != user.password:
        return {"code": 200, "message": "密码错误"}

    # success
    token = create_token(user.userId, user.isRoot)
    return {"code": 200, "data": {"token": token}}


@user_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    # build user
    user = User()
    user.username = data['username']
    # 判断是否有重复用户名
    result = db.session.query(User).filter(User.username == user.username).first()
    if result is not None:
        return {"code": 200, "message": "用户名已存在"}
    # 密码加密
    password = data['password']
    password = password_md5(password)
    user.password = password

    # 数据库操作
    db.session.add(user)
    db.session.commit()
    return {"code": 200, "data": user.username}


@user_bp.route('/add', methods=['POST'])
# @login_required
# @root_required
def addUser():
    # 权限验证
    data = request.json
    user = packUser(data)
    user.password = password_md5(user.password)

    # 判断是否有重复用户名
    result = db.session.query(User).filter(User.username == user.username).first()
    if result is not None:
        return {"code": 200, "message": "用户名已存在"}

    db.session.add(user)
    db.session.commit()

    del data['password']
    return {"code": 200, "data": data}


@user_bp.route('/delete', methods=['POST'])
# @login_required
# @root_required
def deleteUser():
    # 权限验证
    data = request.json
    user = packUser(data)

    # 判断是否存在此用户
    result = db.session.query(User).filter(User.userId == user.userId).first()
    if result is None:
        return {"code": 200, "message": "不存在此用户"}

    # 存在则删除用户
    success = userDao.delete1User(user)
    if not success:
        return {"code": 200, "message": "删除用户失败"}
    return {"code": 200, "message": "删除用户成功"}

@user_bp.route('/update', methods=['POST'])
# @login_required
# @root_required
def updateUser():
    return None

@user_bp.route('/', methods=['GET'])
# @login_required
def getUser():
    userId = request.values.get("userId")
    # 判断是否存在此用户
    result:User = db.session.query(User).filter(User.userId == userId).first()
    if result is None:
        return {"code": 200, "message": "不存在此用户"}

    return {"code": 200, "data": result.as_dict()}

def packUser(data):
    user = User()
    user.username = data['username']
    user.isRoot = data['isRoot']
    user.password = data['password']
    return user
