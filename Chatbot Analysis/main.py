import chatgui
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatgui.chatbot_response(msg))

if __name__ == "__main__":
    app.run() 
    


# while True:
#     msg = str(input("you: "))
#     if msg != ' ':
#         result = chatgui.chatbot_response(msg)

#         print("bot: ",result)
        
        