from flask import Flask, render_template, request, redirect, session
import script
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send", methods=['POST'])
def send():
    #update (currently placeholders)
    name = request.form["name"]
    email = request.form["email-input"]
    # send email here
    