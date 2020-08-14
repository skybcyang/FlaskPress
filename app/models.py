from app import db

# 在这来定义数据表
class Admin(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(36), nullable=False)
    password = db.Column(db.String(36), nullable=False)

    def __init__(self,id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %s>'%(self.username)
