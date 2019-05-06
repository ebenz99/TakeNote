import libs.recorder as rc
import time
import os
import pyaudio

rec = rc.Recorder(channels=1)
with rec.open(os.getcwd()+"/raw/testaudio.wav") as recfile2:
	recfile2.start_recording()
	mystr = input()
	while mystr!="stop":
		mystr = input()
	recfile2.stop_recording()