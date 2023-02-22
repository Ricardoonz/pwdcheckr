from flask import Flask, render_template, request
from waitress import serve
import bcrypt

# Initialize Flask app
app = Flask(__name__)

# Define password strength algorithm
def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '='] for char in password):
        score += 1
    return score

# Define home route
@app.route('/')
def home():
    return render_template('index.html')

# Define password strength route
@app.route('/password_strength', methods=['POST'])
def password_strength():
    password = request.form['password']
    score = check_password_strength(password)
    recommendations = []
    if score == 0:
        message = "Password is too weak"
    elif score == 1:
        message = "Password is weak"
        recommendations = ["Add more characters"]
    elif score == 2:
        message = "Password is medium"
        recommendations = ["Add more characters", "Use a combination of uppercase and lowercase letters"]
    elif score == 3:
        message = "Password is strong"
        recommendations = ["Add more characters", "Use a combination of uppercase and lowercase letters", "Add numbers or special characters"]
    elif score == 4:
        message = "Password is very strong"
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return render_template('password_strength.html', message=message, score=score, recommendations=recommendations, hashed_password=hashed_password)

# Run app
if __name__ == '__main__':
    app.run(debug=True)
    serve(app, host="0.0.0.0", port=8080)
