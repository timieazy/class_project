# Student Portfolio Dashboard

## Overview
The Student Portfolio Dashboard is a Flask-based web application designed for educational purposes. It showcases a personalized dashboard for DevOps students, displaying their name, current learning path, and interests. It also includes a feedback submission feature.

## Features
- Personalized welcome message using environment variables
- Display of the student's current learning path and interests
- Feedback submission form

## Installation

### Prerequisites
- Python 3
- Flask
- Gunicorn

### Setup
1. **Clone the Repository**
   ```
   git clone [repository-url]
   cd [repository-directory]
   ```

2. **Install Dependencies**
   ```
   pip install Flask gunicorn
   ```

3. **Set Environment Variables**
   Replace `[name]`, `[learning_path]`, and `[interests]` with your actual values.
   ```
   export STUDENT_NAME=[name]
   export LEARNING_PATH=[learning_path]
   export INTERESTS=[interests]
   ```

## Running the Application

### Development Mode
Run the application in development mode using Flask:
```
flask run
```
Access the application via `http://localhost:5000` in your web browser.

### Production Mode with Gunicorn
Run the application in production mode using Gunicorn:
```
gunicorn -w 4 app:app
```
This command starts Gunicorn with 4 worker processes. Access the application as configured by Gunicorn (default is `http://127.0.0.1:8000`).

## Usage
- **Dashboard**: View your personalized information on the main page.
- **Feedback**: Submit feedback through the feedback form.

## Customization
You can customize the application by editing the HTML templates in the `templates` directory and the CSS file in the `static` directory.

## Contributing
Contributions to the project are welcome. Please follow the standard fork-and-pull request workflow.