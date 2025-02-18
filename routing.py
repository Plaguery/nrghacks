from flask import Flask, render_template, request, redirect, session
import script
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send", methods=['POST'])
def send():
    #requests info
    email = request.form["email-input"]
    selected = request.form.get("message-type")

    #sends email address
    match selected:
        case 'a': script.sendInsult(email)
        case 'b': script.sendQuote(email)
        case 'c': script.sendFact(email)
    return render_template("thankyou.html")

    