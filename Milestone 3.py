from argostranslate import package, translate
import os
import urllib.request

link = 'https://drive.google.com/drive/folders/11wxM3Ze7NCgOk_tdtRjwet10DmtvFu3i'

fileName = 'en_es.argosmodel'

urllib.request.urlretrieve(link, fileName)
print(f'Downloaded {fileName} successfully.')

# for some reason this worked before now it doesn't, might be because of lines 5-10
# package.install_from_path('en_es.argosmodel')

installedLanguages = translate.get_installed_languages()

translation = installedLanguages[0].get_translation(installedLanguages[1])

directory = os.path.dirname(os.path.abspath(__file__))
vidNum = 0
wordList = []

for file in os.listdir(directory):
    if file.endswith('transcription.txt'):
        vidNum += 1
        with open(file, 'r') as f:
            wordList = f.read().split(' ')

        with open('Video ' f'{vidNum}' ' translation.txt', 'w', encoding='utf-8') as w:
            for word in wordList:
                w.write(translation.translate(word).replace('.', '.\n') + ' ')