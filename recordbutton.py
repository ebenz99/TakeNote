import recorder as rc
import time

rec = rc.Recorder(channels=1)
with rec.open('testaudio.wav', 'wb') as recfile2:
	recfile2.start_recording()
	time.sleep(7.0)
	recfile2.stop_recording()