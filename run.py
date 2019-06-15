# import os so that we will have access to the environment variables
import os
# import datetime module from the datetime library which is a built in module in pythons standard library that allows us to work specifically with dates and times
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

# initialise our new flask application
app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []

def add_messages(username, message):
  """Add messages to the 'messages' list"""
  now = datetime.now().strftime("%H:%M:%S")
  messages_dict = {"timestamp": now, "from": username, "message": message }
  messages.append(messages_dict)

# create our app root decorator, which is going to be for our index page so that will be ("/")
@app.route("/", methods = ["GET", "POST"])
# define the function that is going to be bound to our decorator: def.index().
def index():
  """Main page with instructions"""

  if request.method == "POST":
    # create session username variable
    session["username"] = request.form["username"]

  if "username" in session:
    return redirect(session["username"])

  return render_template("index.html")

@app.route("/<username>")
def user(username):
  """Display chat messages"""
  return "<h1>Welcome, {0}</h1>{1}".format(username, messages)

@app.route("/<username>/<message>")
def send_message(username, message):
  # Docstrings for my function (notes to understand what going on using """write here""")
  """ Create a new message and redirect back to the chat page """
  add_messages(username, message)
  return redirect("/" + username)

app.run(debug=True)
# app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')))





