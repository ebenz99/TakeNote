# TakeNote

## My Steps

1. `pip install SpeechRecognition` - a python wrapper library for a lot of different speech recognition APIs
2. `brew install portaudio` - done because PyAudio requires `portaudio.h`, which isn't default on Mac
3. `pip install PyAudio` - this is the key to getting microphone input
4. `pip install pydub` for conversion's sake
4. `brew install ffmpeg` - again for conversion's sake. This one will take a minute because if you don't have it installed already, there are like 30 dependencies it needs to also install.
4. To make sure all of your versions are compatible, open up an ipython session and type the following:
~~~~
import speech_recognition as sr

with sr.Microphone() as source:
	pass
~~~~
This should run without error (and without doing anything noticeable)

5. Downloaded some test audio with `curl https://github.com/realpython/python-speech-recognition/blob/master/audio_files/harvard.wav --output sample.wav`. If you don't have curl installed, just go to that link and download it to your current directory manually.