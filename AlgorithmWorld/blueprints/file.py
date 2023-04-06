from flask import Blueprint
from AlgorithmWorld.utils.upload import upload_files
from AlgorithmWorld.config.config import DevelopmentConfig

file_bp = Blueprint('file', __name__)


@file_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    file_path = upload_files(base_path=DevelopmentConfig.UPLOAD_FOLDER)
    if file_path is None:
        return {"code": 200, "message": "上传失败"}

    return {"code": 200, "message": "上传成功", "file_path": file_path}
