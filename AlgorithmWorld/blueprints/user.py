from flask import Blueprint, request
from sqlalchemy import and_

from AlgorithmWorld.extensions import db
from AlgorithmWorld.model.model import User
from AlgorithmWorld.utils.jwtUtils import login_required, create_token
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
    # 密码加密
    password = data['password']
    password = password_md5(password)
    user.password = password

    # 数据库操作
    db.session.add(user)
    db.session.commit()
    return {"code": 200, "data": user.username}


@user_bp.route('/add', methods=['POST'])
@login_required
def addUser():
    return None
