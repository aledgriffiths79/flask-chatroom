# import os so that we will have access to the environment variables
import os
from flask import Flask

# initialise our new flask application
app = Flask(__name__)

# create our app root decorator, which is going to be for our index page so that will be ("/")
@app.route("/")
# define the function that is going to be bound to our decorator: def.index().
def index():
  """Main page with instructions"""
  return "To send a message use /USERNAME/MESSAGE"

@app.route("/<username>")
def user(username):
  return "Hi " + username

@app.route("/<username>/<message>")
def send_message(username, message):
  return "{0}: {1}".format(username, message)

app.run(debug=True)
# app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')))





