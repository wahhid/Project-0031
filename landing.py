from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET KEY'] = 'mysecret'
socketio = SocketIO(app)


@app.route("/landing")
def landing():
    return render_template('landingpage.html')

@app.route("/send")
def send():
    return render_template('sendmessage.html')

@socketio.on('message')
def handleMessage(msg):
    print ('Message : ' + msg)
    send(msg,broadcast=True)


if __name__ == '__name__':
    socketio.run(app)

