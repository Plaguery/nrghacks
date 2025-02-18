from flask import Flask, render_template, request, redirect, session
from email_validator import EmailNotValidError, validate_email
import script
app = Flask(__name__)
status = 0

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send", methods=['POST'])
def send():
    #requests info
    email = request.form["email-input"]

    if(validate(email)):
        selected = request.form.get("message-type")
        #sends email address
        match selected:
            case 'a': status = script.sendInsult(email)
            case 'b': status = script.sendQuote(email)
            case 'c': status = script.sendFact(email)
            case 'd': status = script.sendPhoto(email)
        return render_template("thankyou.html", responseCode = status)
    else:
        return render_template("index.html", emailInvalid = True)
    
    
    

def validate(email):
    try:
        email_info = validate_email(email)  # validate and get email info
        email = email_info.normalized  # validates the address and gives you its normalized form
        return True
    except EmailNotValidError as e:  # catch invalid emails
        return False