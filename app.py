#import Declarations
import datetime
from os import environ
from flask import Flask, render_template
from werkzeug.utils import secure_filename
#from werkzeug.security import generate_password_hash, check_password_hash
#from flask_login import UserMixin, login_user, login_manager, login_required, logout_user, current_user,LoginManager

app = Flask(__name__)

#Database Connection Strings-

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/our_users'


#SQL Handler and Migrator
#db = SQLAlchemy(app)
#migrate = Migrate(app, db)

#Login Manager
#login_manager = LoginManager()

#Login Manager Initializer & Re-director
#ogin_manager.init_app(app)
#login_manager.login_view = 'login'

#Manager Will Keep track of...
#@login_manager.user_loader
#def load_user(user_id):
#   return Users.query.get(int(user_id))

#Database Model
#class Users(db.Model, UserMixin):
    
    #General information-
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(255), nullable=False)
#    username = db.Column(db.String(255), nullable = False, unique=True)
#    email = db.Column(db.String(255), nullable=False, unique=True )
#    favorite_color = db.Column(db.String(255))
#    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    #Password
#    password_hash = db.Column(db.String(255))
    
    #Password-if error
#    @property
#    def password(self):
#        raise AttributeError('Password is not a readable attribute!')
    
    #Password setter & verify
#    @password.setter
#    def password(self,password):
#        self.password_hash=generate_password_hash(password)
    
#    def verify_password(self, password):
#        return check_password_hash(self.password_hash,password)
    
    #String handler
#    def __repr__(self):
#        return  '<Name %r>' % self.name

#Form Class-Main-Login
#class LoginForm(FlaskForm):
#    """description of class"""
#    username = StringField('User Name',validators=[ validators.data_required() ] )
#    password_hash = PasswordField('Password',validators=[ validators.data_required()])
#    submit = SubmitField("Submit")
    
#Form Class-Main
#class UserForm(FlaskForm):
#    """description of class"""
#    name = StringField('Name',validators=[ validators.data_required() ] )
#    username = StringField('User Name',validators=[ validators.data_required() ] )
#    email = StringField('Email',validators=[ validators.data_required() ])
#    favorite_color = StringField('Address')
#    password_hash = PasswordField('Password',validators=[ validators.data_required(), validators.equal_to('password_hash2', message="Passwords Don't Match")])
#    password_hash2 = PasswordField('Confirm Password', validators=[validators.data_required()])
#    submit = SubmitField("Submit")


#HTML page routing

#Homepage Route-
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'home.html',
        title='Home Page',
        year=datetime.datetime.now().year,
    )

#Contact Route-
@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.datetime.now().year,
        message='Send us a mail at'
    )

#About Route-   
@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.datetime.now().year,
        message='Your application description page.'
    )

#Products Route-
@app.route('/products')
def products():
    """Renders the product page."""
    return render_template(
        'Products.html',
        title='Products',
        year=datetime.datetime.now().year,
        message='Your products description page.'
    )

#Product1 Route-
@app.route('/prod1')
def prod1():
    """Renders the product page."""
    return render_template(
        'prod1.html',
        title='Solar Panel',
        year=datetime.datetime.now().year,
    )

#Product2 Route-
@app.route('/prod2')
def prod2():
    """Renders the product page."""
    return render_template(
        'prod2.html',
        title='Belts',
        year=datetime.datetime.now().year,
    )

#Product3 Route-
@app.route('/prod3')
def prod3():
    """Renders the product page."""
    return render_template(
        'prod3.html',
        title='ToothBrushes',
        year=datetime.datetime.now().year,
    )
#Product4 Route-
@app.route('/prod4')
def prod4():
    """Renders the product page."""
    return render_template(
        'prod4.html',
        title='Rugs',
        year=datetime.datetime.now().year,
    )

#Product5 Route-
@app.route('/prod5')
def prod5():
    """Renders the product page."""
    return render_template(
        'prod5.html',
        title='Lights',
        year=datetime.datetime.now().year,
    )

#Product6 Route-
@app.route('/prod6')
def prod6():
    """Renders the product page."""
    return render_template(
        'prod6.html',
        title='Phone cases',
        year=datetime.datetime.now().year,
    )
    
#Login Route-
#@app.route('/login', methods= ['GET','POST'])
#def login():
#    form= LoginForm()
#    if form.validate_on_submit():
#        user = Users.query.filter_by(username=form.username.data).first()
#        if user:
#            #check hash
#            if check_password_hash(user.password_hash, form.password_hash.data):
#                login_user(user)
#                flash("Login Successful")
#                return redirect(url_for('dashboard'))
#            else:
#                flash("Wrong Password try again")
#        else:
#            flash("User does not exist")
#    return render_template(
#        'login.html',form=form,
#        title='Login',
#        year=datetime.now().year,
#        )

#Logout Function Handler
#@app.route('/logout',methods=['GET','POST'])
#@login_required
#def logout():
#    logout_user()
#    flash('You Have been logged out')
#    return redirect('/login')

#Registration Route::Add User-
#@app.route('/user/add', methods=['GET','Post'])
#def add_user():
#    name= None
#    form = UserForm()
#    if form.validate_on_submit():
#        user = Users.query.filter_by(email = form.email.data ).first()
#        if user is None:
#            #Hashing Password
#            hashed_pw = generate_password_hash(form.password_hash.data, "sha256")
#            user = Users(username=form.username.data , name = form.name.data, email = form.email.data, favorite_color = form.favorite_color.data, password_hash=hashed_pw )
#            #Session to Add and Commit to database
#            db.session.add(user)
#            db.session.commit()
#        #Clearing Forms after use
#        name = form.name.data
#        form.name.data = ''
#        form.email.data = ''
#        form.favorite_color.data = ''
#        form.password_hash.data = ''
#        form.username.data = ''
#        # Display Message After Creation and redirect afterwards
#        flash ("User Added Sucessfully!")
#    our_users = Users.query.order_by(Users.date_added)
#    return render_template(
#        'add_user.html',
#        title='Registration',
#        year=datetime.now().year,
#        form=form,
#        name=name,
#        our_users=our_users
#        )
    

#Update record Route::Update Info-
#@app.route('/update/<int:id>', methods = ['GET','POST'])
#@login_required
#def update(id):
#    form = UserForm()
#    name_to_update = Users.query.get_or_404(id)
#    if request.method == 'POST':
#        #Find Info
#        name_to_update.name = request.form['name']
#        name_to_update.email = request.form['email']
#        name_to_update.favorite_color = request.form['favorite_color']
#        try:
#            #Saving Changes
#            db.session.commit()
#            flash("Users Updated Sucessfully!")
#            return render_template("Update.html",
#                                   form = form, 
#                                   name_to_update = name_to_update,
#                                   title='Update',
#                                   year=datetime.now().year
#                                   )
#        except:
#            #Incase Of Problem
#            flash("Error! Looks like a problem occurred.")
#            return render_template("Update.html",
#                                   form = form, 
#                                   name_to_update = name_to_update,
#                                   title='Update',
#                                  year=datetime.now().year
#                                   )
#    else:
#        #return the page itself
#       return render_template("Update.html",
#                                   form = form, 
#                                   name_to_update = name_to_update,
#                                   id=id,
#                                   title='Update',
#                                   year=datetime.now().year
#                                   )

#Delete User Route::DeleteUser-
#@app.route('/delete/<int:id>')
#@login_required
#def delete(id):
    #Find user to delete
#    user_to_delete = Users.query.get_or_404(id)
#    name= None
#    form = UserForm()
#    try:
        #Session to Delete user
#        db.session.delete(user_to_delete)
#        db.session.commit()
#        #Message and return template to register user
#        flash('User Deleted Sucessfully!')
#        our_users = Users.query.order_by(Users.date_added)
#        
#         return render_template(
#            'add_user.html',
#            title='Registration',
#            year=datetime.now().year,
#            form=form,
#            name=name,
#            our_users=our_users
#        )
#    except:
#        #Incase problem
#        flash("Error, Problem with database")
    
### Application runner ###
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT,debug=True)