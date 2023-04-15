import json

from flask import Blueprint

from AlgorithmWorld.extensions import db
from AlgorithmWorld.model.model import User
from AlgorithmWorld.utils.jwtUtils import root_required, login_required
from flask import Blueprint, request

from AlgorithmWorld.dao import userDao
from AlgorithmWorld.extensions import db
from AlgorithmWorld.model.model import User
from AlgorithmWorld.utils.jwtUtils import create_token, login_required, root_required, get_jwt_payload
from AlgorithmWorld.utils.md5 import password_md5
from AlgorithmWorld.utils.pack import packUser

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/getAllUsers', methods=['GET'])
@root_required
def getAllUser():
    users = db.session.query(User).all()

    userList = []
    for user in users:
        userList.append(user.as_dict())
    return {"code": 200, "data": userList}


@admin_bp.route('/add', methods=['POST'])
@login_required
@root_required
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
