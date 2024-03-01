from models import db, UserWord, UserProgress
from user_progress import get_content_for_user
# def check_words_learned_for_user(user_progress_id):
        
#     learned_count = UserWord.query.filter(
#         UserWord.user_progress_id == user_progress_id,
#         UserWord.learned == True,
#         ).count()
        
#         # Fetch or create the user's progress for this language
#     user_progress = UserProgress.query.filter_by(
#         user_progress_id==user_progress_id,
#         ).first()
        
#     user_progress.words_learned = learned_count

#     print(f"Updated words learned count for user {user_progress_id}.")

def categorize_content_by_new_word_status(content, user_progress):
    
    # Separate the content based on the new_word attribute
    new_words = []
    old_words = []
    
    for word in content:
        user_word = UserWord.query.filter_by(user_progress_id=user_progress.id, word_id=word.id).first()
        if user_word.new_word==True:
            new_words.append(word)
        else:
            old_words.append(word)
    
    return new_words, old_words
