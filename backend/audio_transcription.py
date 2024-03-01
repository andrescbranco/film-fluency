import openai
import whisper


openai.api_key = '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'

def transcribe(audio_path):
    audio_file = open(f'{audio_path}','rb')
    output = openai.audio.transcriptions.create(
        model = 'whisper-1',
        file = audio_file,
        response_format= 'text',
    )
# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")
    print(output)

#If you transcribe the audio locally it is more prone to error but there's the segmentation attribute which will be needed for the listening feautures of the app, maybe using a language parameter makes it less prone to error, check https://github.com/ufal/whisper_streaming/blob/main/README.md for streaming transcriptions and translations 
def transcribe_with_timestamps_local(audio_path):
    
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    
    for segment in result['segments']:
        start_time = segment['start']
        end_time = segment['end']
        text = segment['text']

    print(f"{start_time}-{end_time}: {text}")
    

def translate_local(audio_path):
    
    model = whisper.load_model("base")
    result = model.transcribe(audio_path, task = 'translate')  

    print(result)

def translate(audio_path):
    audio_file = open(f'{audio_path}','rb')
    output = openai.audio.translations.create(
        model = 'whisper-1',
        file = audio_file,
        response_format = 'text'
        
    )
    print(output)

transcribe('./frontend/assets/Braveheart_ William Wallace Freedom Speech [Full HD].mp4')
