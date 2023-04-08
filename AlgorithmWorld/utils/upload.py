import datetime
import os
import platform
import random

from flask import request

ALLOWED_EXTENSIONS = {'png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF'}
SPACER = {'Linux': '/', 'Windows': '\\', 'Mac': '/'}
print(SPACER.get('Windows'))

def create_uuid():  # 生成唯一的图片的名称字符串，防止图片显示时的重名问题
    now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")  # 生成当前时间
    random_num = random.randint(0, 100)  # 生成的随机整数n，其中0<=n<=100
    if random_num <= 10:
        random_num = str(0) + str(random_num)
    unique_num = str(now_time) + str(random_num)
    return unique_num


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def upload_files(base_path):
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    image = request.files.get('image')

    if not allowed_file(image.filename):
        return None
    spacer = SPACER.get(platform.system())
    # file path
    filename = create_uuid() + image.filename
    file_path = base_path + spacer + filename
    image.save(file_path)
    return file_path
