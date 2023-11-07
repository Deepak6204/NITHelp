from flask import Flask, render_template, request, jsonify, json, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
import gspread, os
from oauth2client.service_account import ServiceAccountCredentials
app = Flask(__name__)
app.secret_key = '3456yhjkiu6'

login_manager = LoginManager()
login_manager.init_app(app)

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(credentials)

# Open the Google Sheet by its title
sheet = gc.open_by_key('1bZjBEJjX6NfkJx-ciSgJesKcP4LtPhqAX0F92tMf85Y')

# Get all records
worksheet = sheet.get_worksheet(0) 



class User(UserMixin):
    def __init__(self, username):
        self.username = username
        # self.password = password
        
    def get_id(self):
        return self.username

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))

@login_manager.user_loader
def load_user(user):
    return User(user)

@app.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('index.html', user = current_user.username)
    else:
        return render_template('index.html', user = "Login")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form.get('uid')
    password = request.form.get('pass')
    
    email_column = worksheet.col_values(3)
    pass_column = worksheet.col_values(2)
    uid_column = worksheet.col_values(1)
    
    if(username in email_column):
        if(password == pass_column[email_column.index(username)]):
            name = uid_column[email_column.index(username)]
            user = User(username=name)
            login_user(user)
            return redirect("/")
        else:
            #add error messages
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
    
    # Add authentication logic here (for example, check against a hardcoded user)

@app.route('/signup', methods = ["POST"])
def signup():
    # data = request.get_json()
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    
    email_column = worksheet.col_values(3)
    if(email in email_column):
        return jsonify('this email is already used')
    
    #add data to the worksheet
    worksheet.append_row([username, password, email])
    return redirect('/')

@app.route('/ask')
def ask():
    
    # Define the file path
    file_path = 'data.json' 
    
    with open(file_path, 'rb+') as file:
        data_questions = json.load(file)
    if current_user.is_authenticated:
        return render_template('qna.html', data = data_questions,user = current_user.username)
    else:
        return render_template('qna.html',data = data_questions, user = "Login")

@app.route('/addAns', methods = ["POST"])
@login_required
def addAns():
    qid = request.form.get('id')
    ans = request.form.get('ans')
    new_ans = {
                "answer": ans,
                "username": current_user.username
            }
    file_path = 'data.json'
        # to add data this template can be used
    with open(file_path, 'r') as file:
        new_data = json.load(file)
        for entry in new_data:
            if entry["question_id"] == int(qid):
                entry["answers"].append(new_ans)
        
    with open(file_path, 'w') as file:
        file.seek(0)
        json.dump(new_data, file, indent=4)
    
    return redirect(url_for('ask'))

@app.route('/addQues', methods = ["GET", "POST"])
@login_required
def addques():
    # to add data this template can be used
    file_path = 'data.json'
    with open(file_path, 'rb+') as file:
        file_data = json.load(file)
        file.seek(-1, os.SEEK_END)

         # Truncate the file at this position
        file.truncate()
        
    question = request.form.get('ques')
    new_data = {
        "answers": [],
        "question": question,
        "question_id": file_data[-1]['question_id']+1
    }

    # Open the JSON file in append mode
    with open(file_path, 'a') as file:
        # Move the cursor to just before the last closing bracket
        file.seek(file.tell()-1)
        
        # If the file is not empty, add a comma before appending the new data
        if file.tell() > 1:
            file.write(',')

        # Add the new data
        json.dump(new_data, file, indent=4)
        file.write(']')
        
    return redirect(url_for('ask'))

@app.route('/notes')
@login_required
def notes():
    return render_template('notes.html' ,user = current_user.username)

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
    

@app.route('/readMore')
def readMore():
    if current_user.is_authenticated:
        return render_template('readMore.html', user = current_user.username)
    else:
        return render_template('readMore.html',user  = "Login")

if __name__ == '__main__':
    app.run(debug=True)







    # to add data this template can be used
#         new_data = {
#             "answers": [
#                 {
#                     "answer": "5 + 5 equals 10.",
#                     "username": "new_user1"
#                 },
#                 {
#                     "answer": "The result of 5 + 5 is 10.",
#                     "username": "new_user2"
#                 }
#             ],
#             "question": "What is 5 + 5?",
#             "question_id": 4
#         }
#     # Get the file size
#         file.seek(-1, os.SEEK_END)

#         # Truncate the file at this position
#         file.truncate()

# # Open the JSON file in append mode
#     with open(file_path, 'a') as file:
#         # Move the cursor to just before the last closing bracket
#         file.seek(file.tell()-1)
        
#         # If the file is not empty, add a comma before appending the new data
#         if file.tell() > 1:
#             file.write(',')

#         # Add the new data
#         json.dump(new_data, file, indent=4)
#         file.write(']')