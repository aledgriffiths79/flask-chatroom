# import os so that we will have access to the environment variables
import os
from flask import Flask, redirect

# initialise our new flask application
app = Flask(__name__)
messages = []

def add_messages(username, message):
  """Add messages to the 'messages' list"""
  messages.append("{}: {}".format(username, message))

def get_all_messages():
  """Get all the messages and separate them with a 'br'"""
  return "<br>".join(messages)

# create our app root decorator, which is going to be for our index page so that will be ("/")
@app.route("/")
# define the function that is going to be bound to our decorator: def.index().
def index():
  """Main page with instructions"""
  return "To send a message use /USERNAME/MESSAGE"

@app.route("/<username>")
def user(username):
  """Display chat messages"""
  return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())

@app.route("/<username>/<message>")
def send_message(username, message):
  # Docstrings for my function (notes to understand what going on using """write here""")
  """ Create a new message and redirect back to the chat page """
  add_messages(username, message)
  return redirect("/" + username)

app.run(debug=True)
# app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')))





