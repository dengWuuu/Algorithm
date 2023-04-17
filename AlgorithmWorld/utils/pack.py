from AlgorithmWorld.model.model import User


def packUser(data):
    user = User()
    keys = data.keys()
    if 'userId' in keys: user.userId = data['userId']
    if 'username' in keys: user.username = data['username']
    if 'isRoot' in keys: user.isRoot = data['isRoot']
    if 'password' in keys:  user.password = data['password']
    if 'imageUrl' in keys:  user.imageUrl = data['imageUrl']
    if 'email' in keys: user.email = data['email']
    if 'tel' in keys:  user.tel = data['tel']
    return user
