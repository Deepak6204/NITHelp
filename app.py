from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import json

app = Flask(__name__)
app.secret_key = '3456yhjkiu6'

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def get_id(self):
        return self.username

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1000), nullable=False)
    answers = db.relationship('Answer', backref='question', lazy=True)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(1000), nullable=False)
    username = db.Column(db.String(150), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))

@login_manager.user_loader
def load_user(user):
    return User.query.filter_by(username=user).first()

@app.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('index.html', user=current_user.username)
    else:
        return render_template('index.html', user="Login")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form.get('uid')
    password = request.form.get('pass')
    
    user = User.query.filter_by(email=username).first()
    
    if user and check_password_hash(user.password, password):
        login_user(user)
        return redirect("/")
    else:
        return redirect(url_for('login'))

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    
    if User.query.filter_by(email=email).first():
        return jsonify('This email is already used')
    
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    return redirect('/')

@app.route('/ask')
def ask():
    with open('data.json', 'rb+') as file:
        data_questions = json.load(file)
    if current_user.is_authenticated:
        return render_template('qna.html', data=data_questions, user=current_user.username)
    else:
        return render_template('qna.html', data=data_questions, user="Login")

@app.route('/addAns', methods=['POST'])
@login_required
def addAns():
    qid = request.form.get('id')
    ans = request.form.get('ans')
    
    new_ans = Answer(answer=ans, username=current_user.username, question_id=qid)
    db.session.add(new_ans)
    db.session.commit()
    
    return redirect(url_for('ask'))

@app.route('/addQues', methods=['GET', 'POST'])
@login_required
def addques():
    question = request.form.get('ques')
    
    new_question = Question(question=question)
    db.session.add(new_question)
    db.session.commit()
    
    return redirect(url_for('ask'))

@app.route('/notes')
@login_required
def notes():
    return render_template('notes.html', user=current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route('/profile')
@login_required
def profile():
    if current_user.is_authenticated:
        return redirect('/')
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
