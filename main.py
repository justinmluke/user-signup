from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template("signup_form.html")    

@app.route('/', methods=["POST"])
def signup_validation():    
    username = request.form['username']
    password = request.form['password']
    verify_pass = request.form['verify_pass']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if username.strip() == "":
        username_error = "Please enter a valid username"
        username = username
    else:
        if len(username) < 3 or len(username) > 20:
            username_error = "Username must between 3 and 20 characters"
            username = username
        else:
            if " " in username:
                username_error = "Username cannot contain any spaces"
                username = username    

    if password.strip() == "":
            password_error = "Please enter a valid password"
            password = ""
    else:
        if len(password) < 3 or len(password) > 20:
            password_error = "Password must between 3 and 20 characters"
            password = ""
        else:
            if " " in password:
                password_error = "Password cannot contain any spaces"
                password = "" 

    if verify_pass.strip() != password.strip():
        verify_error = "Passwords do not match"
        verify_pass = ""
        password = ""

    if email.strip() == "":
        pass
    else:    
        if "@" not in email or "." not in email:
            email_error = "Please enter a valid email address"
            email = email
        else:
            if len(email) < 3 or len(email) > 20:
                email_error = "Please enter a valid email address"
                email = email

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template("signup_confirmation.html", username=username)
    else:
        return render_template("signup_form.html", username_error=username_error,
        password_error=password_error, verify_error=verify_error, email_error=email_error,
        username=username,email=email)         

app.run()    