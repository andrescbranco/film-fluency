from datetime import datetime, timedelta
from models import db

def super_memo(user_word, score):

    user_word.new_word = False

    if score >= 3:
        if user_word.repetitions == 0:
            user_word.interval = 1
        elif user_word.repetitions == 1:
            user_word.interval = 6
        else:
            user_word.interval = round(user_word.interval * user_word.ease_factor)
        user_word.repetitions += 1
    else:
        user_word.repetitions = 0
        user_word.interval = 1 

    if score == 0:
        user_word.learned = True
    
    if user_word.repetitions == 5:
        user_word.learned = True

    user_word.ease_factor = max(1.3, user_word.ease_factor + 0.1 - (5 - score) * (0.08 + (5 - score) * 0.02))

        #Calculate the date and add inteval
    today = datetime.today().date()

# Define the interval (5 days in this case)
    interval = timedelta(days=user_word.interval)

# Calculate the new date
    user_word.next_review_date = today + interval

    db.session.add(user_word)
    db.session.commit()

