from datetime import datetime
from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(13), unique=True, nullable=False)
    # email = db.Column(db.String(20), unique=True, nullable=False)
    # image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    # password =db.Column(db.String(30), nullable=False)
    # posts = db.relationship('Post',backref='author', lazy='True')
    # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    
    def __repr__(self):

        return f"post('{self.username}')"


# class Role(db.Model):
#     __tablename__ = 'roles'

#     id = db.Column(db.Integer,primary_key = True)
#     name = db.Column(db.String(255))
#     users = db.relationship('User',backref = 'role',lazy="dynamic")


#     def __repr__(self):
#         return f'User {self.name}'

# class Post(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     title = db.Column(db.String(13), nullable=False)
#     date_posted = db.Column(db.DateTime,default=datetime.utcnow)
#     content = db.Column(db.String,nullable=False)
#     user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

#     def __repr__(self):

#         return f"post('{self.title}','{self.date_posted}')"