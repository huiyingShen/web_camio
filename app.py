import os
from flask import Flask,render_template,send_from_directory


app = Flask(__name__, static_folder="static", template_folder='templates')
AUDIO_FOLDER = os.path.join("static", "audio")

@app.route("/")
def camio():
    return render_template('index.html')

@app.route("/ps1")
def ps1():
    return render_template('ps1.html')

@app.route("/ps2")
def ps2():
    return render_template('ps2.html')

@app.route("/ps3")
def ps3():
    return render_template('ps3.html')
@app.route("/click")
def click():
    return render_template('click.html')

@app.route("/tts")
def tts():
    return render_template('tts.html')

@app.route("/hands")
def hands():
    return render_template('hands.html')

@app.route("/mp3")
def mp3():
    return render_template('mp3.html')

@app.route('/songs')
def songs():
    songs = os.listdir(AUDIO_FOLDER)  # List all the audio files
    return render_template('songs.html', songs=songs)

@app.route('/audio/<filename>')
def stream_audio(filename):
    return send_from_directory(AUDIO_FOLDER, filename)

if __name__ == "__main__":
    # cer = os.path.join(os.path.dirname(__file__), 'server.crt')
    # key = os.path.join(os.path.dirname(__file__), 'server.key')
    # app.run(host='0.0.0.0', port=8443, debug = True, ssl_context=(cer, key))
    app.run(host='localhost', port=8000, debug = True)

