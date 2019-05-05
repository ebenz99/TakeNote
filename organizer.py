import speech_recognition as sr 
import logging
import threading
import time
import os
import pickle

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./TakeNote-89a084a7097d.json"


#adopted from GCP github
def transcribe_gcs_with_word_time_offsets(mcontent):
	"""Transcribe the given audio file asynchronously and output the word time
	offsets."""
	from google.cloud import speech
	from google.cloud.speech import enums
	from google.cloud.speech import types
	client = speech.SpeechClient()



	audio = types.RecognitionAudio(content=mcontent)
	config = types.RecognitionConfig(
		encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
		sample_rate_hertz=48000,
		language_code='en-US',
		enable_word_time_offsets=True)

	operation = client.long_running_recognize(config, audio)

	print('Waiting for operation to complete...')
	result = operation.result(timeout=90)

	for result in result.results:
		alternative = result.alternatives[0]
		print(u'Transcript: {}'.format(alternative.transcript))
		print('Confidence: {}'.format(alternative.confidence))

		for word_info in alternative.words:
			word = word_info.word
			start_time = word_info.start_time
			end_time = word_info.end_time
			print('Word: {}, start_time: {}, end_time: {}'.format(
				word,
				start_time.seconds + start_time.nanos * 1e-9,
				end_time.seconds + end_time.nanos * 1e-9))
		return alternative.words



mydir = os.getcwd()+"/chunks/flac/"
info = []

for (dirpath, dirnames, filenames) in os.walk(mydir):
	for filename in filenames:
		with open(mydir+filename, 'rb') as fd:
			mcontent = fd.read()
			info.append(transcribe_gcs_with_word_time_offsets(mcontent))
		os.remove(mydir+filename)

#prepping for pickle
mystr = ""
strings = []
for wObjectList in info:
	mystr = ""
	for wObject in wObjectList:
		mystr += wObject.word
		#print(type(wObject.word))
		#print(wObject.word)
		mystr += " "
		#print(mystr)
	strings.append(mystr)
	mystr = ""

#print(strings)

#pickle dumping time
os.chdir(os.getcwd()+"//pickles")
outfile = open("words.pkl", "wb")
pickle.dump(strings,outfile)
outfile.close
