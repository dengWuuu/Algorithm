from AlgorithmWorld.model.model import User


def packUser(data):
    user = User()
    user.username = data['username']
    user.isRoot = data['isRoot']
    user.password = data['password']
    user.imageUrl = data['imageUrl']
    user.email = data['email']
    user.tel = data['tel']
    return user
