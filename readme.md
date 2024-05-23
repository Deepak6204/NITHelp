# Flask Q&A Application

This project is a Q&A web application built with Flask. Users can sign up, log in, ask questions, and provide answers. The project uses SQLite3 for the database and includes user authentication.

## Features

- User authentication (sign up, log in, log out)
- Ask questions
- Provide answers to questions
- View notes (requires login)

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Getting Started

Follow these steps to fork and use this code.

### 1. Fork the Repository

1. Go to the repository page on GitHub.
2. Click the "Fork" button in the upper right corner to create a copy of the repository under your GitHub account.

### 2. Clone the Repository

Clone the forked repository to your local machine:

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/REPOSITORY_NAME.git
cd REPOSITORY_NAME
```

### 3. Set Up a Virtual Environment
It's recommended to use a virtual environment to manage dependencies. Run the following commands:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 4. Install Dependencies
Install the required Python packages using the requirements.txt file:

```bash
pip install -r requirements.txt
```

### 5. Set Up the Database
Initialize the SQLite3 database:

```bash
python
>>> from app import db
>>> db.create_all()
>>> exit()
```

### 6. Create credentials.json
If your project uses Google Sheets for some functionality, ensure you have the credentials.json file in the root directory. Obtain this file from the Google Cloud Console.

### 7. Run the Application
Run the Flask application:

```bash
flask run
```
The application should now be running on http://127.0.0.1:5000/.

### Project Structure
```bash
.
├── app.py
├── templates
│   ├── index.html
│   ├── login.html
│   ├── qna.html
│   ├── notes.html
│   ├── readMore.html
│   └── ...
├── static
│   ├── css
│   │   └── styles.css
│   ├── js
│   │   └── scripts.js
│   └── ...
├── data.json
├── requirements.txt
└── README.md
```

### How to Use
#### Sign Up
1. Navigate to the /signup page.
2. Fill in the required details (username, email, and password).
3. Click "Sign Up".
#### Log In
1. Navigate to the /login page.
2. Enter your email and password.
3. Click "Log In".
4. Ask a Question
5. Log in to your account.
6. Navigate to the /ask page.
7. Enter your question in the provided form and submit.
#### Answer a Question
1. Log in to your account.
2. Navigate to the /ask page.
3. Find a question you want to answer.
4. Enter your answer in the provided form and submit.
#### View Notes
1. Log in to your account.
2. Navigate to the /notes page to view your notes.
3. Contributing

#### Feel free to submit issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.


