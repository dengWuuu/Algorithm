import datetime

import sqlalchemy
from sqlalchemy import (
    create_engine,
    Integer,
    BigInteger,
    String,
    DateTime,
    FetchedValue
)
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from AlgorithmWorld.extensions import db

# 基础类
Base = sqlalchemy.orm.declarative_base()


class User(Base):
    """ 必须继承Base """
    # 数据库中存储的表名
    __tablename__ = "user"

    userId = db.Column(BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(String(20))
    password = db.Column(String(128))
    imageUrl = db.Column(String(250))
    isRoot = db.Column(Integer, default=0)
    updateTime = db.Column(DateTime, default=datetime.datetime.now())
    createTime = db.Column(DateTime, default=datetime.datetime.now())
    version = db.Column(BigInteger, nullable=False)
    deleted = db.Column(Integer, default=0)
    __mapper_args__ = {
        "version_id_col": version,
    }
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    # extra function to help judge user is administrator


class User_Record(Base):
    """ 必须继承Base """
    # 数据库中存储的表名
    __tablename__ = "user_record"
    recordId = db.Column(BigInteger, primary_key=True, autoincrement=True)
    userId = db.Column(BigInteger)
    AlgorithmPkgId = db.Column(BigInteger)
    updateTime = db.Column(DateTime, default=datetime.datetime.now())
    createTime = db.Column(DateTime, default=datetime.datetime.now())
    version = db.Column(BigInteger, nullable=False)
    deleted = db.Column(Integer, default=0)
    __mapper_args__ = {
        "version_id_col": version,
    }


class AlgorithmPkg(Base):
    """ 必须继承Base """
    # 数据库中存储的表名
    __tablename__ = "algorithm_pkg_id"
    algorithmPkgId = db.Column(BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(String(150))
    imageUrl = db.Column(String(250))
    userId = db.Column(BigInteger)
    tag = db.Column(String(30))
    location = db.Column(String(150))
    updateTime = db.Column(DateTime, default=datetime.datetime.now())
    createTime = db.Column(DateTime, default=datetime.datetime.now())
    version = db.Column(BigInteger, nullable=False)
    deleted = db.Column(Integer, default=0)
    __mapper_args__ = {
        "version_id_col": version,
    }


if __name__ == "__main__":
    # 创建引擎
    engine = create_engine(
        "mysql+pymysql://root:Aa1076766987@127.0.0.1:3306/AlgorithmWorld?charset=utf8mb4",
        # 超过链接池大小外最多创建的链接
        max_overflow=0,
        # 链接池大小
        pool_size=5,
        # 链接池中没有可用链接则最多等待的秒数，超过该秒数后报错
        pool_timeout=10,
        # 多久之后对链接池中的链接进行一次回收
        pool_recycle=1,
        # 查看原生语句（未格式化）
        echo=True
    )

    # 绑定引擎
    Session = sessionmaker(bind=engine)
    # 创建数据库链接池，直接使用session即可为当前线程拿出一个链接对象conn
    # 内部会采用threading.local进行隔离
    session = scoped_session(Session)
    # 删除表
    Base.metadata.drop_all(engine)
    # 创建表
    Base.metadata.create_all(engine)
