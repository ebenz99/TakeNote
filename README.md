# TakeNote

## My Steps

1. `pip install SpeechRecognition` - a python wrapper library for a lot of different speech recognition APIs
2. `brew install portaudio` - done because PyAudio requires `portaudio.h`, which isn't default on Mac
3. `pip install PyAudio` - this is the key to getting microphone input
4. To make sure all of your versions are compatible, open up an ipython session and type the following


`import speech_recognition as sr

with sr.Microphone() as source: 
		pass`

5. 