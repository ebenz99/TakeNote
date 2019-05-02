# TakeNote

This is *officially* a GCP project. I wanted to use sphinx originally, but as far as I can tell, they really hate usability.

## My Steps

1. `pip install SpeechRecognition` - a python wrapper library for a lot of different speech recognition APIs
2. `brew install portaudio` - done because PyAudio requires `portaudio.h`, which isn't default on Mac
3. `pip install PyAudio` - this is the key to getting microphone input
4. `pip install pydub` - will be used for converting audio file types
5. `brew install ffmpeg` - *Very* necessary for audio file format conversion. This one will take a minute--there are like 30 dependencies it needs to also install.
6. To make sure all of your versions are compatible, open up an ipython session and type the following:
   ```
	import speech_recognition as sr

	with sr.Microphone() as source:
		pass
   ```
7. `pip install wave` for plotting
8. I recorded some test audio in QuickTime, which unfortunately (as far as I can tell) only exports in `.m4a` now. If you can't get a `.wav` file but you want to make your own, record something in `.m4a` format and run `converter.py` from this repository.


## Pipeline

recordbutton.py->wavtoflac.py->main.py



## Future Plans

1. "Record button" will begin a session
2. "Stop recording" will end session
3. ~~Will use SciPy (maybe Tensorflow for recognizing "Take Note" if SciPy isn't good enough) to mark all instances of "TakeNote" in audio~~ Currently using GCP Speech to Text API for keyword recognition and timestamps
4. Repeat and mark all long pauses
5. Parse with speech recognizer from each timestamp of each "Take Note" to silence
6. Append recognized text to end of file