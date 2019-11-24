from . import main
from flask import render_template,url_for,flash,redirect
from .forms import RegistrationForm,LoginForm










# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'pitches all over in 60 seconds'

    posts = [

    {
        'author':'Nya',
        'title':'First Pitch',
        'content':'users content on first pitch',
        'date_posted': 'October 12,2015'
    },
    {
        'author':'Shee',
        'title':'Third Pitch',
        'content':'users content on first pitch',
        'date_posted':'October 19,2015'
    },
     {
        'author':'Joy',
        'title':'second Pitch',
        'content':'users content on first pitch',
        'date_posted':'October 20,2015'
    },
    ]
    return render_template('index.html',title=title,posts=posts)


@main.route('/register', methods=['GET','POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.login'))
        title = "New Account"
    return render_template('register.html',form = form)



@main.route('/login',methods = ['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
        
        
        return redirect( url_for('main.index'))
        flash('Succsessfully Logged in')

        
    title = "Pitches login"        
    return render_template('login.html',login_form=login_form,title=title)

# @main.route('/login',methods = ['GET','POST'])
# def login():
#     login_form = LoginForm()
#     if login_form.validate_on_submit():
#         user = User.query.filter_by(email=login_form.email.data).first()
#         if user is not None and user.verify_password(login_form.password.data):
#             login_user(user,login_form.remember.data)
#             return redirect(request.args.get('next') or url_for('main.index'))

#         flash('Invalid username or Password')
#     title = "Watchlist login"        
#     return render_template('login.html',login_form=login_form,title=title)