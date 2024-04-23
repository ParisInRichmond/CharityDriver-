from flask import Flask, render_template, request, redirect
import smtplib
app = Flask(__name__)

# Replace these values with your email and password
email_address = "your_email@gmail.com"
email_password = "your_email_password"

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/about')
def aboutUS():
    return render_template('about.html')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    
    # Send notification email
    send_notification(email)

    # You can also save the email to a database or file for later use
    
    return redirect('/')

def send_notification(email):
    subject = "New Newsletter Signup"
    body = f"Email: {email}"

    # Replace with your SMTP server details
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create an SMTP connection
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(email_address, email_password)

        # Send the email
        server.sendmail(email_address, email_address, f"Subject: {subject}\n\n{body}")

if __name__ == '__main__':
    app.run(debug=True)
