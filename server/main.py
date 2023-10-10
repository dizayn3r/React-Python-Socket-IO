from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from flask_login import login_required
from flask import session, Response, redirect, url_for
import os

template_dir = os.getcwd()
app = Flask(__name__, template_folder=f"{template_dir}/templates")
app.config['SECRET_KEY'] = 'secret!'
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
# Set the CORS header to be "application/json"
app.config['CORS_HEADERS'] = 'application/json'
socketio = SocketIO(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Implement user authentication logic here
    # Check if username and password are valid

    if valid_login(username, password):
        session['username'] = username
        result = {"success": True, "message": "login succeeded"}
        return jsonify(result)
    else:
        result = {"success": False, "message": "unautherized"}
        return jsonify(result)

def valid_login(username, password):
    # Replace with your authentication logic (e.g., database query)
    return username == 'rajesh' and password == 12345

@socketio.on('connect')
def handle_connect():
    if 'username' in session:
        emit('message', 'Connected to the dashboard!')

@socketio.on('disconnect')
def handle_disconnect():
    pass  # Handle disconnect event if needed

if __name__ == '__main__':
    print('Starting')
    socketio.run(app, port=3000, allow_unsafe_werkzeug=True, debug = True)
