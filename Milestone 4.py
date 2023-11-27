import os
import pyttsx3

tts = pyttsx3.init()

tts.setProperty('rate', 150)
tts.setProperty('voice', r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')
directory = os.path.dirname(os.path.abspath(__file__))
vidNum = 0

for file in os.listdir(directory):
    if file.endswith('translation.txt'):
        vidNum += 1
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()

        tts.save_to_file(text, f'Video {vidNum} text-to-speech.mp4')

        tts.runAndWait()
