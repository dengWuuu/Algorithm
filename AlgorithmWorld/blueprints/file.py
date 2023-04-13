from flask import Blueprint, request

from AlgorithmWorld.utils.jwtUtils import login_required
from AlgorithmWorld.utils.upload import upload_files
from AlgorithmWorld.config.config import DevelopmentConfig

file_bp = Blueprint('file', __name__)


@file_bp.route('/uploadImg', methods=['POST'])
@login_required
def uploadImg():
    file_path = upload_files(base_path=DevelopmentConfig.UPLOAD_FOLDER)
    if file_path is None:
        return {"code": 200, "message": "上传失败"}

    return {"code": 200, "message": "上传成功", "file_path": file_path}
