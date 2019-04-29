import speech_recognition as sr 

r = sr.Recognizer()

sample = sr.AudioFile('sample.m4a')
with sample as source:
	audio = r.record(source)
	print(type(audio))
	text = r.recognize_google(audio)
print(text)