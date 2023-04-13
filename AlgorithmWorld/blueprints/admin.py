import json

from flask import Blueprint

from AlgorithmWorld.extensions import db
from AlgorithmWorld.model.model import User
from AlgorithmWorld.utils.jwtUtils import root_required

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/getAllUsers', methods=['GET'])
@root_required
def getAllUser():
    users = db.session.query(User).all()

    userList = []
    for user in users:
        userList.append(user.as_dict())
    return {"code": 200, "data": userList}
