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
        sample_rate_hertz=16000,
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