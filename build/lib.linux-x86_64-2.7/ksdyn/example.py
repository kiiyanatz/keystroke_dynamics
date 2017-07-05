from functools import partial

from core import KeystrokeCaptureData
from model import Fingerprint, FingerprintDatabase
from sugar import create_fingerprint_from_capture_data
# from flask import Flask, render_template, request

# app = Flask(__name__)

DATA_DIR = "/home/kiiya/Projects/python_projects/keystroke_dynamics/data/"


example_text1 = '''
    Wikipedia is a free-access,
    free content Internet encyclopedia,
    supported and hosted by the non-profit Wikimedia Foundation.
    Those who can access the site and follow its rules can
    edit most of its articles.
    Wikipedia is ranked among the ten most popular websites and
    constitutes the Internet's largest
    and most popular general reference work.
'''


def get_some_keystrokes():
    print "Please write the following text. When you're finished, press Ctrl-C"
    print "------------------"
    print example_text1
    data = KeystrokeCaptureData()
    try:
        import capture_keys
        capture_keys.start(data.on_key)
    except KeyboardInterrupt:
        pass
    print "\n"
    return data


def create_fingerprint():
    username = raw_input("what's your name? ")
    data = get_some_keystrokes()
    print type(data)
    data.save_to_file(DATA_DIR + username)
    fingerprint = create_fingerprint_from_capture_data(username, data)
    fingerprint.save_to_file(DATA_DIR + username)
    print "Finished creating fingerprint!"


def match_fingerprint():
    db = FingerprintDatabase().load_from_dir(DATA_DIR)
    data = get_some_keystrokes()
    f = create_fingerprint_from_capture_data("NoName", data)
    best = db.best_match(f)
    print "Best match: ", best.name


# @app.route('/')
# def index():
#     title = 'Wifi Login'
#     return render_template('index.html', title=title, example_text1=example_text1)


# @app.route('/continue')
# def continue_signup():
#     title = 'Continue login'
#     return render_template('continue.html', title=title, example_text1=example_text1)

if __name__ == '__main__':
    print "Choose an option:\n  1) create new fingerprint\n  2) match text to a existing fingerprint"
    try:
        option = int(raw_input())
    except Exception:
        print "Bad option"
        exit()
    print "\n\n"
    if option == 1:
        create_fingerprint()
    elif option == 2:
        match_fingerprint()
    else:
        print "Bad option"
    # app.run(debug=True)
