from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()


# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = f"{os.getenv('MAIL_USERNAME')}@gmail.com"

mail = Mail(app)

@app.route('/')
def dashboard():
    student_name = os.getenv('STUDENT_NAME', 'Timis')
    learning_path = os.getenv('LEARNING_PATH', 'DevOps Engineer')
    interests = os.getenv('INTERESTS', 'Becoming the best on my department').split(',')
    return render_template('dashboard.html', 
                           student_name=student_name, 
                           learning_path=learning_path, 
                           interests=interests)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        feedback_text = request.form['feedback']
        send_email(name, email, feedback_text)
        flash('Thank you for your feedback!', 'success')
    return render_template('feedback.html')

def send_email(name, email, feedback_text):
    msg = Message('Feedback Received', recipients=[os.getenv('MAIL_USERNAME')])  
    msg.body = f'Feedback from: {name} ({email})\n\nFeedback: {feedback_text}'
    mail.send(msg)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
