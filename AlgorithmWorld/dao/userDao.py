from AlgorithmWorld.extensions import db
from AlgorithmWorld.model.model import User


def delete1User(user: User):
    result: User = db.session.query(User).filter(User.userId == user.userId).first()
    # 软删除，就要更新result
    result.deleted = 1
    db.session.add(result)
    db.session.commit()
