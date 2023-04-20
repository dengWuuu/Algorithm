from flask import Blueprint, request

from AlgorithmWorld.utils.jwtUtils import login_required, root_required
from AlgorithmWorld.utils.upload import upload_img, upload_zips
from AlgorithmWorld.config.config import DevelopmentConfig

file_bp = Blueprint('file', __name__)


@file_bp.route('/uploadImg', methods=['POST'])
@login_required
def uploadImg():
    file_path = upload_img(base_path=DevelopmentConfig.UPLOAD_IMG_FOLDER)
    if file_path is None:
        return {"code": 200, "message": "上传失败"}

    return {"code": 200, "message": "上传成功", "file_path": file_path}


@file_bp.route('/uploadToolZip', methods=['POST'])
@login_required
@root_required
def uploadToolZip():
    file_path = upload_zips(base_path=DevelopmentConfig.UPLOAD_FOLDER)
    if file_path is None:
        return {"code": 200, "message": "上传失败"}

    return {"code": 200, "message": "上传成功", "file_path": file_path}
