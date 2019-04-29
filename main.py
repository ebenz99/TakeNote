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
recognizer = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
	r.adjust_for_ambient_noise(source)
	try:
		sample = r.listen(source)
		text = recognizer.recognize_google(sample)
		print(text)
	except sr.UnknownValueError:
		# speech was unintelligible
		print("Unable to recognize speech")
