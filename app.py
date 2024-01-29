from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def dashboard():
    student_name = os.getenv('STUDENT_NAME', 'Student')
    learning_path = os.getenv('LEARNING_PATH', 'Not Set')
    interests = os.getenv('INTERESTS', 'None').split(',')

    return render_template('dashboard.html', 
                           student_name=student_name, 
                           learning_path=learning_path, 
                           interests=interests)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        feedback = request.form['feedback']
        with open('feedback.txt', 'a') as f:
            f.write(f"{feedback}\n")
        return 'Feedback submitted!'
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)