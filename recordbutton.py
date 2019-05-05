import libs.recorder as rc
import time

rec = rc.Recorder(channels=1)
with rec.open('raw//testaudio.wav', 'wb') as recfile2:
	recfile2.start_recording()
	mystr = input()
	while mystr!="stop":
		mystr = input()
	recfile2.stop_recording()