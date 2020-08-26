from flask import Flask, request, jsonify
import bot
from flask import render_template


#app = Flask(__name__)
app = Flask(__name__, template_folder='template')


@app.route("/")
def chat():
    ip = request.remote_addr
    print(str(ip))
    #bot.reload()
    return render_template('chat.html')
    # while True:
    # msg = str(input('me> '))
    # print('bot> ' + bot.chat(msg))


@app.route("/get")
def get_bot_response():
    msg = request.args.get('msg')
    records = bot.chat(msg)
    return records


if __name__ == "__main__":
    app.run()

