from app import db, app
from models import Language, Word, User
import csv
from faker import Faker

fake = Faker()

def seed_users(num_users):
    print('Seeding Users...')
    users = []
    for _ in range(num_users):
        try:
            username = fake.name()
            user = User(username=username)
            users.append(user)
        except Exception as e:
            print(f"Error adding user: {e}")

    db.session.add_all(users)
    db.session.commit()

def seed_languages():
    languages = [
        Language(name='Portuguese'),
        Language(name='Spanish'),
        Language(name='French'),
        Language(name='Japanese')
    ]
    db.session.bulk_save_objects(languages)


def seed_words(file, language_id):
    with open(file, mode='r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames

        has_kanji = 'Kanji' in headers
        has_frequency = 'Frequency' in headers 

        for row in reader:
            try:
                word = Word(
                    rank=int(row['Rank']),
                    word=row['Word'],
                    part_of_speech=row['Part of Speech'],
                    definition = row['English Translation'],
                    context=row['Phrase'],
                    english_context=row['English Phrase'],
                    language_id = language_id
                )
                
                if has_frequency:
                    word.frequency = row.get('Frequency',None) 
                
                if has_kanji:
                    word.kanji = row.get('Kanji', None)  

                db.session.add(word)

            except Exception as e:
                print(f"Error processing row: {e}")

        db.session.commit()

def main():
    with app.app_context():
        db.create_all()
        print("Clearing db...")
        Language.query.delete()
        Word.query.delete()
        User.query.delete()
        seed_users(20)
        seed_languages()
        seed_words('../backend/assets/French 5000.csv',3)
        seed_words('../backend/assets/Japanese 5000.csv',4)
        seed_words('../backend/assets/Spanish 5000.csv',2)
        seed_words('../backend/assets/Portuguese 5000.csv',1)

        db.session.commit() 

if __name__ == '__main__':
    main()

