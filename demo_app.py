from flask import Flask, render_template, request, jsonify, redirect, url_for
import json

app = Flask(__name__)
app.secret_key = '3456yhjkiu6'

@app.route('/')
def index():
    return render_template('index.html', user="Guest")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('login.html')

@app.route('/ask')
def ask():
    file_path = 'data.json'
    with open(file_path, 'rb+') as file:
        data_questions = json.load(file)
    return render_template('qna.html', data=data_questions, user="Guest")

@app.route('/notes')
def notes():
    return render_template('notes.html', user="Guest")

@app.route('/readMore')
def readMore():
    return render_template('readMore.html', user="Guest")

if __name__ == '__main__':
    app.run(debug=True)
