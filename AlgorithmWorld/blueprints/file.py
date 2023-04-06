import os

from flask import Blueprint, request

base_path = os.path.abspath(os.path.dirname(__name__))
base_path = base_path.replace('/blueprints', '/static')
file_bp = Blueprint('file', __name__)


@file_bp.route('/upload/', methods=['GET', 'POST'])
def upload():
    image = request.files['image']
    # file path
    path = base_path

    file_path = path + image.filename
    image.save(file_path)
    return {"code": 200, "message": "储存文件成功"}
