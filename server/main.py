from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def home():
    return "This is base route"


if __name__ == '__main__':
    app.run(debug=True)
    print('Starting')
    socketio.run(app)
