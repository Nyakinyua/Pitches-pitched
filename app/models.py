# from datetime import datetime
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager




# ***********************************************************************************************************************************
# -----------------------------------------------------------------------------------------------------------------------------------
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ************************************************************************************************************************************
# ------------------------------------------------------------------------------------------------------------------------------------

class User(UserMixin,db.Model):
    '''
    class with a table that defines all the User properties
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(225), unique=True, nullable=False)
    email = db.Column(db.String(225), unique=True, nullable=False)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure =db.Column(db.String(225), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    pitches = db.relationship('Post',backref='author', lazy='True')
    
    
    @property
    def password(self):
        '''
        function that raises an attribute error when one enters a password
        '''
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        '''
        function that generates a hashed password and saves it in the database
        '''

        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        '''
        function that verifies a password to check if theres a match
        '''
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):

        return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(20))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(13), nullable=False)
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)
    content = db.Column(db.String,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):

        return f"post('{self.title}','{self.date_posted}')"

class Coments(db.Model):
    __tablename__='comments'
    id=db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(250))
    comment= db.Column(db.String())