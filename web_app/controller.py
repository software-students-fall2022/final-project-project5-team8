from flask import Flask, render_template, request
from dotenv import dotenv_values
# from flask_bootstrap import Bootstrap
from flask_gtts import gtts
import speech_recognition as sr
from PIL import Image
from pytesseract import pytesseract
import database
from PIL import Image
from pytesseract import pytesseract
import os
import flask
import trans
import pymongo


# instantiate the app
app = Flask(__name__)
app.config['MONGO_URI'] = database.get_connection_str
gtts(app)


# ****************** All Routes ******************************#

# route for homepage
# Takes in a audio file and display the transcript of the audio file


@app.route('/', methods=["GET", "POST"])
def home():
    db = database.get_db(0)
    # initalize the database with the languages that can be translated
    database.db_lang_init(db)
    # pass database in twice for both drop down menus
    # inp = db.langs.find({})
    out = db.langs.find({})
    if request.method == "POST":
        # get audio from app.js
        f = request.files['audio_data']
        # save audio to audio.wav file through flask server
        with open('audio.wav', 'wb') as audio:
            f.save(audio)
            file = 'audio.wav'
        if file:
            # implement speech recognition
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            # save the audio translation to global variable for easy accesibility
            global transcript
            transcript = recognizer.recognize_google(data, key=None)
    # pass database in to be read in home.html
    return render_template('home.html', out=out)


# route for translating the recognized audio file input using machine learning
@app.route('/translate', methods=["POST"])
def translate():
    # get the options selected from input and output from home.html
    inp = "English"
    out = request.form.get('output')
    db = database.get_db(0)
    db_text = database.get_db(1)
    # using the languages chosen by the user locate their doc in the database
    src = db.langs.find_one({"lang": inp})
    targ = db.langs.find_one({"lang": str(out)})
    # isolate the code to be used for translation
    s = src["code"]
    t = targ["code"]
    # call the trans function and translate the text to language
    try:
        in_out = trans.trans(transcript, s, t)
    except:
        return render_template('translate.html', error=True)
    database.db_text_add(db_text, transcript, out, in_out, t)
    return render_template('translate.html', in_out=in_out, transcript=transcript, out=out, t=t)


@app.route('/dashboard', methods=["GET"])
def dashboard_display():
    lang = database.get_db(0).langs.find({})
    translations = database.get_db(1).hist.find({})
    count = database.get_db(1).hist.count_documents({})
    return render_template('dashboard.html', translations=translations, count=count, lang=lang)


@app.route('/dashboard/delete', methods=["GET", "POST"])
def delete_history():
    lang = database.get_db(0).langs.find({})
    database.get_db(1).hist.delete_many({})
    return render_template('dashboard.html', lang=lang)


@app.route('/dashboard/sort_filter', methods=["GET", "POST"])
def filter_sort_history():
    if request.method == "POST":
        lang = database.get_db(0).langs.find({})
        sort = request.form.get('sort')
        filter = request.form.get('filter')
        if sort != "None" and filter != "None":
            translations = database.get_db(1).hist.find(
                {"output_lang": str(filter)}).sort(sort, 1)
            count = database.get_db(1).hist.count_documents(
                {"output_lang": str(filter)})
        elif sort != "None" and filter == "None":
            translations = database.get_db(1).hist.find({}).sort(sort, 1)
            count = database.get_db(1).hist.count_documents({})
        elif sort == "None" and filter != "None":
            translations = database.get_db(1).hist.find(
                {"output_lang": str(filter)})
            count = database.get_db(1).hist.count_documents(
                {"output_lang": str(filter)})
        elif sort == "None" and filter == "None":
            translations = database.get_db(1).hist.find({})
            count = database.get_db(1).hist.count_documents({})
        return render_template('dashboard.html', translations=translations, count=count, lang=lang)


@app.route('/upload_image', methods=["GET"])
def upload_image_page():
    return render_template('image_analysis.html')


@app.route('/upload_image', methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        f = request.files['image']
        if f.filename == "":
            return render_template('image_analysis.html', error=True)
        lang = database.get_db(0).langs.find({})
        f.filename = "user_image.jpg"
        f.save(f.filename)
        global transcript
        transcript = pytesseract.image_to_string("user_image.jpg")
        return render_template('image_analysis.html', transcript=transcript, out=lang)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
