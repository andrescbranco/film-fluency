import os
import random

def select_random_mp4_file(dir_path):
    try:
        files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
  
        mp4_files = [f for f in files if f.lower().endswith('.mp4')]
        
        if not mp4_files:
            return "No MP4 files found in the directory."
        
        selected_file = random.choice(mp4_files)
        
        return os.path.join(dir_path, selected_file)
    except Exception as e:
        return str(e)
    