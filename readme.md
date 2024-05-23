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

<!-- ### 5. Set Up the Database
Initialize the SQLite3 database:

```bash
python
>>> from app import db
>>> db.create_all()
>>> exit()
``` -->

### 5. Create credentials.json
If your project uses Google Sheets for some functionality, ensure you have the credentials.json file in the root directory. Obtain this file from the Google Cloud Console.

### 6. Run the Application
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

# Contributing

# Contributing to This Project

Thank you for your interest in contributing to this project! This guide will help you fork the repository, make your changes, and submit a pull request.

## Getting Started

### 1. Fork the Repository

1. Navigate to the repository page on GitHub.
2. Click the "Fork" button in the upper right corner of the page to create a copy of the repository under your GitHub account.

### 2. Clone the Forked Repository

Once you have forked the repository, clone it to your local machine:

1. Go to your GitHub profile and find the forked repository.
2. Click the "Code" button and copy the URL.
3. Open your terminal or command prompt.
4. Run the following command to clone the repository:
```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/REPOSITORY_NAME.git
```
5. Navigate to the cloned repository directory:
```bash
   cd REPOSITORY_NAME
```
### 3. Set Up a Virtual Environment (Optional but Recommended)

It's a good practice to use a virtual environment to manage dependencies:

1. Create a virtual environment:
```bash
   python3 -m venv venv
```
2. Activate the virtual environment:

   - On macOS and Linux:
```bash
     source venv/bin/activate
```
   - On Windows:
```bash
     venv\Scripts\activate
```
### 4. Install Dependencies

Install the required dependencies using the `requirements.txt` file:
```bash
   pip install -r requirements.txt
```
## Making Changes

### 1. Create a New Branch

Before making any changes, create a new branch to keep your changes isolated from the main branch:
```bash
   git checkout -b your-branch-name
```
### 2. Make Your Changes

Make the necessary changes in your local repository.

### 3. Commit Your Changes

Once you've made your changes, commit them to your branch:

1. Stage your changes:
```bash
   git add .
```
2. Commit your changes with a descriptive message:
```bash
   git commit -m "Description of the changes"
```
### 4. Push Your Changes

Push your changes to your forked repository on GitHub:
```bash
   git push origin your-branch-name
```
## Submitting a Pull Request

### 1. Navigate to Your Forked Repository

Go to your forked repository on GitHub.

### 2. Open a Pull Request

1. Click the "Compare & pull request" button next to your recently pushed branch.
2. Review the changes to ensure they are correct.
3. Add a title and description for your pull request, explaining what changes you made and why.
4. Click the "Create pull request" button to submit your PR.

### 3. Wait for Review

The project maintainers will review your pull request. They may ask for additional changes or provide feedback. Once your pull request is approved, it will be merged into the main repository.

## Additional Tips

- Keep your pull requests small and focused on a single change or feature to make them easier to review.
- Follow the project's coding style and guidelines.
- Write clear and descriptive commit messages.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

Thank you for contributing!



