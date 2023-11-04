import whisper
import os

directory = os.path.dirname(os.path.abspath(__file__))
print(directory)
start = 0
videoList = []
print(os.listdir(directory))

for file in os.listdir(directory):
    if file.endswith('.mp4'):
        start += 1
        model = whisper.load_model('base')
        result = model.transcribe(file)

        with open("Video " f'{start}' " transcription.txt", "w") as f:
            f.write(result["text"] + '\n')
