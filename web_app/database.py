from dotenv import load_dotenv
import pymongo
import os

def get_connection_str():
    return os.getenv('MONGO_URI')

def get_db(num):
    cxn = pymongo.MongoClient(os.getenv('MONGO_URI'), serverSelectionTimeoutMS=5000)
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
        print(' *', "Failed to connect to MongoDB at",'mongodb://mongodb:27017/')
        print('Database connection error:', e)  # debug
    return db

def db_text_add(db, input_text, out_lang, output_text, code):
    db.hist.insert_one(
        {"input": input_text, "output_lang": out_lang, "output": output_text, "output_code": code})

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