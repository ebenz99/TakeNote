import speech_recognition as sr 
import logging
import threading
import time

r = sr.Recognizer()
"""
sample = sr.AudioFile('sample.wav')
with sample as source:
	audio = r.record(source)
	print(type(audio))
	text = r.recognize_google(audio)
print(text)
"""

mic = sr.Microphone()
with mic as source:
	r.adjust_for_ambient_noise(source)
	try:
		sample = r.listen(source)
    except sr.UnknownValueError:
	    # speech was unintelligible
	    print("Unable to recognize speech")
