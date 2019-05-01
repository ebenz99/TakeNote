import os
from pocketsphinx import AudioFile


speech = AudioFile(audio_file="sample.wav")

for phrase in speech:
    print(phrase)