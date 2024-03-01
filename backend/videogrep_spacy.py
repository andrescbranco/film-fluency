import videogrep
from glob import glob
import subprocess
import spacy
from subprocess import run
import json
import os

def list_mp4_files(directory):
    video_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp4'):
                video_list.append(os.path.join(root, file))
    return video_list

def auto_youtube_search_download(query, max_videos=1):
    """
    Search youtube for a query, download videos with yt-dlp,
    and then makes a supercut with that query
    """

    args = [
        "yt-dlp",  # run yt-dlp
        f"https://www.youtube.com/results?search_query={query}",
        "--write-auto-sub",  # download youtube's auto-generated subtitles
        "-f",  # select the format of the video
        "22",  # 22 is 1280x720 mp4
        "--max-downloads",  # limit the downloads
        str(max_videos),
        "--playlist-end",
        str(max_videos),
        "-o",  # where to save the downloaded videos to
        "./assets/videos/" + query + "%(video_autonumber)s.mp4",  # save the video as the query + .mp4
    ]

    run(args)


def auto_youtube_url_download(url, name, language):
    """
    Search youtube for a query, download videos with yt-dlp,
    and then makes a supercut with that query
    """
    if language == 1:
        language = 'Portuguese'
    elif language == 2:
        language = 'Spanish'
    elif language == 3:
        language = 'French'
    elif language == 4:
        language = 'Japanese'
    else:
        return {'message: Unknow Language'}

    args = [
        "yt-dlp",  # run yt-dlp
        f"{url}",
        '-f',
        '22',
        "-o",  # where to save the downloaded videos to
        f"../frontend/assets/{language}/" + name + "%(video_autonumber)s.mp4",  # save the video as the query + .mp4
    ]

    run(args)

# auto_youtube_url_download('https://www.youtube.com/watch?v=a3C06AVn3DA','Y Tu Mama Tambien', 2)

# videofile = "../frontend/assets/Japanese/ Speech1.mp4"
# japanese = '../frontend/assets/Japanese/I have no enemies1.mp4'
# spanish = '../frontend/assets/Spanish/Madrid1.webm'
# english = '../frontend/assets/Braveheart_ William Wallace Freedom Speech [Full HD].mp4'
# transcript = videogrep.find_transcript(spanish,'json') 
# print(transcript)

def run_videogrep_transcribe(language):
    # Define the command as a list of arguments
    
    models = ['./components/vosk-model-pt-fb-v0.1.1-20220516_2113/vosk-model-pt-fb-v0.1.1-20220516_2113','/Users/andreschnydercastellobranco/code/projects/film-fluency/backend/components/vosk-model-es-0.42/vosk-model-es-0.42','/root/Development/code/phase-5/film-fluency/backend/components/vosk-model-fr-0.6-linto-2.2.0/vosk-model-fr-0.6-linto-2.2.0','/root/Development/code/phase-5/film-fluency/backend/components/vosk-model-ja-0.22/vosk-model-ja-0.22']
    model = models[language-1]

    if language == 1:
        language = 'Portuguese'
    elif language == 2:
        language = 'Spanish'
    elif language == 3:
        language = 'French'
    elif language == 4:
        language = 'Japanese'
    else:
        return {'message: Unknow Language'}

    video_list = list_mp4_files(f'../frontend/assets/{language}/')

    # Initialize the command with the executable and input flag
    command = ['videogrep', '--input']
    
    # Extend the command with the video files
    command.extend(video_list)
    
    #Add other vosk models for transcription
    command += ['--transcribe', '--model', model]
    
    # Run the command
    result = subprocess.run(command, capture_output=True, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        print("Command executed successfully.")
        # Optionally, print the output
        print("Output:", result)
    else:
        print("Error in executing command.")
        print("Error:", result)

def run_videogrep_search(language, word):

    if language == 1:
        language = 'Portuguese'
    elif language == 2:
        language = 'Spanish'
    elif language == 3:
        language = 'French'
    elif language == 4:
        language = 'Japanese'

    # Define the command as a list of arguments

    video_list = list_mp4_files(f'../frontend/assets/{language}/')

    # Initialize the command with the executable and input flag
    command = ['videogrep', '--input']
    
    # Extend the command with the video files
    command.extend(video_list)  # Adds all video paths in the list directly after --input
    
    # Continue building the command with the rest of the options
    command += ['--search', word, '--max-clips', '3', '-r','--search-type', 'sentence', '--padding', '1', '--output', f'{word}.mp4']
    
    # Run the command
    result = subprocess.run(command, capture_output=True, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        print("Command executed successfully.")
        # Optionally, print the output
        print("Output:", result)
    else:
        print("Error in executing command.")
        print("Error:", result.stderr)


def lucas(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return data
        except Exception as e:
            return str(e)

# json_data = lucas('../frontend/assets/Portuguese/audiencia_93548906_1_V (1).json')


# filtered_transcript = '\n'.join(
#     f"{item['content']} {int(item['start'])//3600:02d}:{(int(item['start'])%3600)//60:02d}:{(int(item['start'])%60):02d} - {int(item['end'])//3600:02d}:{(int(item['end'])%3600)//60:02d}:{(int(item['end'])%60):02d}"
#     for item in json_data
# )


# with open('filtered_transcript.txt', 'w') as file:
#     for item in json_data:
#         formatted_line = f"{item['content']} {int(item['start'])//3600:02d}:{(int(item['start'])%3600)//60:02d}:{(int(item['start'])%60):02d} to {int(item['end'])//3600:02d}:{(int(item['end'])%3600)//60:02d}:{(int(item['end'])%60):02d}\n"
#         file.write(formatted_line)
