from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    # password_hash = db.Column(db.String) 

    user_progress = db.relationship("UserProgress", back_populates="user", cascade = 'all, delete-orphan')

    serialize_rules = ['-user_progress.user']

    def __repr__(self):
        return f'<User {self.id}>'

class UserProgress(db.Model, SerializerMixin):
    __tablename__ = 'users_progress'
    id = db.Column(db.Integer, primary_key=True)
    words_learned = db.Column(db.Integer, default=0) 
    current_level = db.Column(db.Integer, default=1)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    language_id = db.Column(db.Integer, db.ForeignKey('languages.id'), nullable=False)

    user = db.relationship('User', back_populates='user_progress')
    language = db.relationship('Language', back_populates='user_progress')
    user_word = db.relationship('UserWord', back_populates='user_progress')

    serialize_rules = ["-user.user_progress", "-language.user_progress", '-user_word.user_progress']

    def __repr__(self):
        return f'<User_Progress {self.id}>'

class Language(db.Model,SerializerMixin):
    __tablename__ = 'languages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    user_progress = db.relationship('UserProgress', back_populates='language')
    word = db.relationship('Word', back_populates='language')

    serialize_rules = ['-user_progress.language','-word.language']

    def __repr__(self):
        return f'<Language {self.id}>'


class Word(db.Model, SerializerMixin):
    __tablename__='words'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String)
    part_of_speech = db.Column(db.String)
    definition = db.Column(db.String)
    context = db.Column(db.String)
    english_context = db.Column(db.String)
    rank = db.Column(db.Integer)
    frequency = db.Column(db.Integer, default = None)
    kanji = db.Column(db.String, default = None)
    romaji = db.Column(db.String, default = None) 

    language_id = db.Column(db.Integer, db.ForeignKey('languages.id'), nullable=False)

    language = db.relationship('Language', back_populates='word')
    user_word = db.relationship("UserWord", back_populates='word')

    def to_dict(self):
        # Basic serialization
        data = {
            'id': self.id,
            'word': self.word,
            'part_of_speech': self.part_of_speech,
            'definition': self.definition,
            'context': self.context,
            'english_context': self.english_context,
            'rank':self.rank,
            'frequency':self.frequency,
            'kanji':self.kanji
        }
        return data

    def __repr__(self):
        return f'<Word {self.id}>'
    
class UserWord(db.Model, SerializerMixin):
    __tablename__ = 'user_words'
    id = db.Column(db.Integer, primary_key=True)
    user_progress_id = db.Column(db.Integer, db.ForeignKey('users_progress.id'))
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'))
    learned = db.Column(db.Boolean, default=False, nullable=False)
    new_word = db.Column(db.Boolean, default=True, nullable=False)
    next_review_date = db.Column(db.Date, nullable=True) 
    repetitions = db.Column(db.Integer, default = 0)
    ease_factor = db.Column(db.Float, default = 2.5)

    user_progress = db.relationship('UserProgress', back_populates='user_word')
    word = db.relationship('Word', back_populates='user_word')

    serialize_rules = ['-user_progress.user_word', '-word.user_word']

    def __repr__(self):
        return f'<UserWord {self.id}>'





