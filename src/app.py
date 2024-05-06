from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, current_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from models import User, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'secret-key-goes-here'
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    else:
        return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('profile'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already taken')
        else:
            hashed_password = generate_password_hash(password)
            new_user = User(username=username, password=hashed_password, email=email)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/profile')
def profile():
    if current_user.is_authenticated:
        return render_template('profile.html', user=current_user)
    else:
        return redirect(url_for('login'))
    
@app.route('/services')
def services():
    if current_user.is_authenticated:
        return render_template('services.html', user=current_user)
    else:
        return redirect(url_for('login'))
    
@app.route('/Main')
def Main():
    if current_user.is_authenticated:
        return render_template('Main.html', user=current_user)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/Tovars')
def Tovars():
    if current_user.is_authenticated:
        return render_template('Tovars.html', user=current_user)
    else:
        return redirect(url_for('login'))
    
@app.route('/Contacts')
def Contacts():
    if current_user.is_authenticated:
        return render_template('Contacts.html', user=current_user)
    else:
        return redirect(url_for('login'))
    
@app.route('/Description_1Server')
def Description_1Server():
    if current_user.is_authenticated:
        return render_template('Description_1Server.html', user=current_user)
    else:
        return redirect(url_for('login'))
    
@app.route('/Description_2Server')
def Description_2Server():
    if current_user.is_authenticated:
        return render_template('Description_2Server.html', user=current_user)
    else:
        return redirect(url_for('login'))
    
@app.route('/Description_3Server')
def Description_3Server():
    if current_user.is_authenticated:
        return render_template('Description_3Server.html', user=current_user)
    else:
        return redirect(url_for('login'))
    
@app.route('/Description_4Server')
def Description_4Server():
    if current_user.is_authenticated:
        return render_template('Description_4Server.html', user=current_user)
    else:
        return redirect(url_for('login'))
    
@app.route('/Description_5Server')
def Description_5Server():
    if current_user.is_authenticated:
        return render_template('Description_5Server.html', user=current_user)
    else:
        return redirect(url_for('login'))
    
@app.route('/Description_6Server')
def Description_6Server():
    if current_user.is_authenticated:
        return render_template('Description_6Server.html', user=current_user)
    else:
        return redirect(url_for('login'))
    
@app.route('/Description_7Server')
def Description_7Server():
    if current_user.is_authenticated:
        return render_template('Description_7Server.html', user=current_user)
    else:
        return redirect(url_for('login'))
    
@app.route('/Description_8Server')
def Description_8Server():
    if current_user.is_authenticated:
        return render_template('Description_8Server.html', user=current_user)
    else:
        return redirect(url_for('login'))
    
@app.route('/Description_9Server')
def Description_9Server():
    if current_user.is_authenticated:
        return render_template('Description_9Server.html', user=current_user)
    else:
        return redirect(url_for('login'))
    
@app.route('/Description_10Server')
def Description_10Server():
    if current_user.is_authenticated:
        return render_template('Description_10Server.html', user=current_user)
    else:
        return redirect(url_for('login'))
    
@app.route('/Description_11Server')
def Description_11Server():
    if current_user.is_authenticated:
        return render_template('Description_11Server.html', user=current_user)
    else:
        return redirect(url_for('login'))
    
@app.route('/Description_12Server')
def Description_12Server():
    if current_user.is_authenticated:
        return render_template('Description_12Server.html', user=current_user)
    else:
        return redirect(url_for('login'))
    
@app.route('/Description_13Server')
def Description_13Server():
    if current_user.is_authenticated:
        return render_template('Description_13Server.html', user=current_user)
    else:
        return redirect(url_for('login'))
    
@app.route('/Description_14Server')
def Description_14Server():
    if current_user.is_authenticated:
        return render_template('Description_14Server.html', user=current_user)
    else:
        return redirect(url_for('login'))
    
@app.route('/Description_15Server')
def Description_15Server():
    if current_user.is_authenticated:
        return render_template('Description_15Server.html', user=current_user)
    else:
        return redirect(url_for('login'))
    
@app.route('/Buy')
def Buy():
    if current_user.is_authenticated:
        return render_template('Buy.html', user=current_user)
    else:
        return redirect(url_for('login'))
    
@app.route('/zakazano')
def zakazano():
    if current_user.is_authenticated:
        return render_template('zakazano.html', user=current_user)
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5000)

