from flask import Flask, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('message')
def handle_message(message):
    print('Received message: ' + message)
    if message == 'start':
        print(message)
        # Code to handle the start of recording
    elif message == 'stop':
        # Code to handle the stop of recording and receive audio file
        audio_file = request.files['audio']
        # Process or save the audio file as needed
        audio_file.save('path_to_save/audio.wav')
        # Send a response if needed

if __name__ == '__main__':
    socketio.run(app, debug=True)
