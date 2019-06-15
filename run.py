# import os so that we will have access to the environment variables
import os
from flask import Flask

# initialise our new flask application
app = Flask(__name__)
messages = []

def add_messages(username, message):
  message.append("{}: {}".format(username, message))

# create our app root decorator, which is going to be for our index page so that will be ("/")
@app.route("/")
# define the function that is going to be bound to our decorator: def.index().
def index():
  """Main page with instructions"""
  return "To send a message use /USERNAME/MESSAGE"

@app.route("/<username>")
def user(username):
  """Display chat messages"""
  return "Welcome, {0}".format(username, messages)

@app.route("/<username>/<message>")
def send_message(username, message):
  # Docstrings for my function (notes to understand what going on using """write here""")
  """ Create a new message and redirect back to the chat page """
  return "{0}: {1}".format(username, message)

app.run(debug=True)
# app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')))





