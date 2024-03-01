from models import UserProgress, db, Word

def update_user_progress(user_id, language_id, words_completed=1):
    user_progress = UserProgress.query.filter_by(user_id=user_id, language_id=language_id).first()
    
    if not user_progress:
        user_progress = UserProgress(user_id=user_id, language_id=language_id)
        db.session.add(user_progress)

    print(words_completed)

    # Calculate the level based on words learned
    new_level = (user_progress.words_learned // 500) + 1
    if new_level > user_progress.current_level:
        user_progress.current_level = new_level
    
    db.session.commit()
    return user_progress.current_level

def get_content_for_user(user_id, language_id):
    user_progress = UserProgress.query.filter_by(user_id=user_id, language_id=language_id).first()
    
    if user_progress:

        # For now each level unlocks 500 words
        max_words_unlocked = user_progress.current_level * 500
        
        content = Word.query.filter(
            Word.language_id == language_id,
            Word.rank <= max_words_unlocked  # Rank orders words by their learning sequence
        ).all()
        return content
    else:
        content = Word.query.filter(
            Word.language_id == language_id,
            Word.rank <= 500
        ).all()
        return content
        

