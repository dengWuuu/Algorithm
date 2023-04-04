import hashlib

salt = "%&***(*9"


# 使用md5密码加密函数
def password_md5(password):
    md5 = hashlib.md5(password.encode("utf-8"))
    md5.update(salt.encode("utf-8"))
    return md5.hexdigest()
