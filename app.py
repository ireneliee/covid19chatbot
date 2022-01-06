from chatbot import chatbot
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
  return render_template("index.html")

# url get, this get go to the index html, take the msg from there
# pass the msg to get_response function from chatbot
# then will return a chatbot response, and make it as the return string of get_bot_response
# ??? so get_reponse is a function of chatbot???
@app.route("/get") 
def get_bot_response():
  userText = request.args.get('msg')
  return str(chatbot.get_response(userText))

if __name__ == "__main__":
  app.run() 
