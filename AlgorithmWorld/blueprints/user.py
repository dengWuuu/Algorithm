from flask import Blueprint, request
from AlgorithmWorld.utils.jwtUtils import login_required

user_bp = Blueprint('user', __name__)


@user_bp.route('/login', methods=['POST'])
def login():
    data = request.form
    return {"code": 200, "data": data}


@user_bp.route('/register', methods=['POST'])
def register():
    data = request.form
    return {"code": 200, "data": data}


@user_bp.route('/add', methods=['POST'])
@login_required
def addUser():
    return None
