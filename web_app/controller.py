from flask import Flask, render_template, request
from dotenv import dotenv_values
from flask_bootstrap import Bootstrap
from flask_gtts import gtts
import speech_recognition as sr
from PIL import Image
from pytesseract import pytesseract
import os
import flask
import trans
import pymongo


# instantiate the app
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://db:27017/'
bootstrap = Bootstrap(app)
gtts(app)


def get_db(num):
    # load_dotenv('.env')
    config = dotenv_values(".env")
    cxn = pymongo.MongoClient(os.getenv('MONGO_URI'),
                              serverSelectionTimeoutMS=5000)
    db = ""
    if num == 0:
        # store a reference to the database
        db = cxn["language"]
    else:
        db = cxn["text"]
    try:
        # verify the connection works by pinging the database
        # The ping command is cheap and does not require auth.
        cxn.admin.command('ping')
        # if we get here, the connection worked!
        print(' *', 'Connected to MongoDB!')
    except Exception as e:
        # the ping command failed, so the connection is not available.
        # render_template('error.html', error=e) # render the edit template
        print(' *', "Failed to connect to MongoDB at",
              'mongodb://mongodb:27017/')
        print('Database connection error:', e)  # debug
    return db


def db_lang_init(db):
    db.langs.delete_many({})
    db.langs.insert_many([{"lang": "Bulgarian", "code": "bg"},
                          {"lang": "Czech", "code": "cs"},
                          {"lang": "Danish", "code": "da"},
                          {"lang": "German", "code": "de"},
                          {"lang": "Greek", "code": "el"},
                          {"lang": "English", "code": "en"},
                          {"lang": "Spanish", "code": "es"},
                          {"lang": "Estonian", "code": "et"},
                          {"lang": "Finnish", "code": "fi"},
                          {"lang": "French", "code": "fr"},
                          {"lang": "Hungarian", "code": "hu"},
                          {"lang": "Italian", "code": "it"},
                          {"lang": "Japanese", "code": "ja"},
                          {"lang": "Korean", "code": "ko"},
                          {"lang": "Latvian", "code": "lv"},
                          {"lang": "Dutch", "code": "nl"},
                          {"lang": "Polish", "code": "pl"},
                          {"lang": "Portuguese", "code": "pt"},
                          {"lang": "Romanian", "code": "ro"},
                          {"lang": "Russian", "code": "ru"},
                          {"lang": "Slovak", "code": "sk"},
                          {"lang": "Swedish", "code": "sv"},
                          {"lang": "Tamil", "code": "ta"},
                          {"lang": "Filipino", "code": "tl"},
                          {"lang": "Ukrainian", "code": "uk"},
                          {"lang": "Vietnamese", "code": "vi"},
                          {"lang": "Chinese (Simplified)", "code": "zh-CN"},
                          ])


def db_text_add(db, input_text, out_lang, output_text, code):
    db.hist.insert_one(
        {"input": input_text, "output_lang": out_lang, "output": output_text, "output_code": code})


# ****************** All Routes ******************************#

# route for homepage
# Takes in a audio file and display the transcript of the audio file


@app.route('/', methods=["GET", "POST"])
def home():
    db = get_db(0)
    # initalize the database with the languages that can be translated
    db_lang_init(db)
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
    db = get_db(0)
    db_text = get_db(1)
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
    db_text_add(db_text, transcript, out, in_out, t)
    return render_template('translate.html', in_out=in_out, transcript=transcript, out=out, t=t)


@app.route('/dashboard', methods=["GET"])
def dashboard_display():
    lang = get_db(0).langs.find({})
    translations = get_db(1).hist.find({})
    count = get_db(1).hist.count_documents({})
    return render_template('dashboard.html', translations=translations, count=count, lang=lang)


@app.route('/dashboard/delete', methods=["GET", "POST"])
def delete_history():
    lang = get_db(0).langs.find({})
    get_db(1).hist.delete_many({})
    return render_template('dashboard.html', lang=lang)


@app.route('/dashboard/sort_filter', methods=["GET", "POST"])
def filter_sort_history():
    if request.method == "POST":
        lang = get_db(0).langs.find({})
        sort = request.form.get('sort')
        filter = request.form.get('filter')
        if sort != "None" and filter != "None":
            translations = get_db(1).hist.find(
                {"output_lang": str(filter)}).sort(sort, 1)
            count = get_db(1).hist.count_documents(
                {"output_lang": str(filter)})
        elif sort != "None" and filter == "None":
            translations = get_db(1).hist.find({}).sort(sort, 1)
            count = get_db(1).hist.count_documents({})
        elif sort == "None" and filter != "None":
            translations = get_db(1).hist.find({"output_lang": str(filter)})
            count = get_db(1).hist.count_documents(
                {"output_lang": str(filter)})
        elif sort == "None" and filter == "None":
            translations = get_db(1).hist.find({})
            count = get_db(1).hist.count_documents({})
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
        lang = get_db(0).langs.find({})
        f.filename = "user_image.jpg"
        f.save(f.filename)
        global transcript
        transcript = pytesseract.image_to_string("user_image.jpg")
        return render_template('image_analysis.html', transcript=transcript, out=lang)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
