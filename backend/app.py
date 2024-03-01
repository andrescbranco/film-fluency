from flask import Flask, request, jsonify
# from flask_bcrypt import Bcrypt
from models import db, User, Word, Language, UserProgress, UserWord
from flask_migrate import Migrate
import os
from flask_cors import CORS
from user_progress import *
from learned_word_count import *
from super_memo import *
import random
from text_comparison import *
from listening_randomizer import *
import videogrep
import json

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
CORS(app, origins=["http://localhost:5173"], allow_headers='Content-Type')
# bcrypt = Bcrypt(app)

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Code challenge</h1>'

@app.route("/vocabulary/<int:language_id>")
def get_words_by_language_id(language_id):
    vocabulary = Word.query.filter_by(language_id=language_id).all() 
    return [word.to_dict() for word in vocabulary]

@app.post('/select-languages')
def select_language():
    data = request.json
    print("data unpacked")
    print(f"\n>> Our current data: \n{data}")
    print(f"\n>> Current data's type: {type(data)}")

    user_id = data.get('user_id')
    language_id = data.get('language_id')

    existing_progress = UserProgress.query.filter_by(user_id=user_id, language_id=language_id).first()
    
    if existing_progress:
        return {"message": "User already has progress in this language", "progress_id": existing_progress.id}, 200
    
    # If not, create a new UserProgress
    new_progress = UserProgress(user_id=user_id, language_id=language_id, words_learned=0, current_level=1)

    print("profile object instantiated")
    db.session.add(new_progress)
    print("new profile added to database")
    db.session.commit()
    print("new profile committed to database for storage")

    return new_progress.to_dict(), 201

@app.route('/user/<int:id>')
def get_user_by_id(id):
    user = db.session.get(User,id)
    return user.to_dict()

@app.get("/user_progress/<int:user_id>")
def get_user_progress_by_user_id(user_id):
    user = UserProgress.query.filter_by(user_id=user_id).all()
    return [user_p.to_dict(rules=['-language','-user']) for user_p in user]


@app.get('/user/<int:user_id>/language/<int:language_id>/get_learn_review/<int:learn_review>')
def filter_learn_review(user_id,language_id,learn_review):
    user_progress = UserProgress.query.filter_by(user_id=user_id, language_id=language_id).first()

    content = get_content_for_user(user_id,language_id)

    new_words, old_words = categorize_content_by_new_word_status(content,user_progress)

    if learn_review == 0:
        return [word.to_dict() for word in new_words]
    else:
        return [word.to_dict() for word in old_words]
      

@app.get('/get_content/<int:user_id>/<int:language_id>')
def get_content(user_id, language_id):
    user_progress = UserProgress.query.filter_by(user_id=user_id, language_id=language_id).first()
    
    # Get_content_for_user returns a list of Word objects in the users level
    content = get_content_for_user(user_id, language_id)

    if content:
        for word in content:
            user_word = UserWord.query.filter_by(user_progress_id=user_progress.id, word_id=word.id).first()
            if not user_word:
                # If UserWord does not exist, create it and set new_word to True indicating it's a new word for the user
                user_word = UserWord(user_progress_id=user_progress.id, word_id=word.id)
                db.session.add(user_word)

        db.session.commit()  # Commit any new UserWord instances
        return {'message':'Content fetched'}
    else:
        return {"message": "No content available at the current level"}, 404
    
@app.patch('/patch_user_word/<int:word_id>/<int:user_id>/<int:language_id>/<int:score>')
def update_user_word(word_id,user_id,language_id,score):
    user_progress = UserProgress.query.filter_by(user_id=user_id, language_id=language_id).first()
    user_word = UserWord.query.filter_by(user_progress_id=user_progress.id, word_id=word_id).first()
    super_memo(user_word, score)

    return {'message':'UserWord updated'}

@app.post('/text_comparison/<int:user_id>/<int:language_id>')
def text_comparison(user_id,language_id):
    user_id = user_id
    language_id = language_id
    data = request.json
    similarity = calculate_similarity(data['user_input'],data['transcript'])
    differences = highlight_differences(data['user_input'], data['transcript'])

    response = {
        'similarity': similarity,
        'differences': differences,
    }

    return jsonify(response)

@app.get('/listening_randomizer/<int:language_id>')
def listening_randomizer(language_id):
    if language_id == 1:
        language = 'Portuguese'
    elif language_id == 2:
        language = 'Spanish'
    elif language_id == 3:
        language = 'French'
    elif language_id == 4:
        language = 'Japanese'

    path = f'../frontend/assets/{language}'

    selected_video = select_random_mp4_file(path)

    new_path = "/".join(part for part in selected_video.split("/") if part != "frontend")

    transcript = videogrep.find_transcript(selected_video,'json')

    def read_json_data(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return data
        except Exception as e:
            return str(e)

    json_data = read_json_data(transcript)

    filtered_transcript = ' '.join(item['content'] for item in json_data)

    response = {
        'video_url' : new_path,
        'transcript': filtered_transcript
    } 

    return jsonify(response)




if __name__=="__main__":
    app.run(port=5555, debug=True)



