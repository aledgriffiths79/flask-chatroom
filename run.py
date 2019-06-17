# import os so that we will have access to the environment variables
import os
# import datetime module from the datetime library which is a built in module in pythons standard library that allows us to work specifically with dates and times
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for

# initialise our new flask application
app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "randomstring123")
messages = []

def add_message(username, message):
  """Add messages to the 'messages' list"""
  now = datetime.now().strftime("%H:%M:%S")
  messages.append({"timestamp": now, "from": username, "message": message })

# create our app root decorator, which is going to be for our index page so that will be ("/")
@app.route("/", methods = ["GET", "POST"])
# define the function that is going to be bound to our decorator: def.index().
def index():
  """Main page with instructions"""

  if request.method == "POST":
    # create session username variable
    session["username"] = request.form["username"]

  if "username" in session:
    return redirect(url_for("user", username=session["username"]))

  return render_template("index.html")

@app.route("/chat/<username>", methods = ["GET", "POST"])
def user(username):
  """Add and display chat messages"""

  if request.method == "POST":
    username = session["username"]
    message = request.form["message"]
    add_message(username, message)
    return redirect(url_for("user", username=session["username"]))

  return render_template("chat.html", username = username, chat_messages = messages)

# app.run(debug=True)
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')))





