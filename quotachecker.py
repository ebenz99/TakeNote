from pydub import AudioSegment
import os

mydir = os.getcwd()+"//chunks//flac"
overallT = 0
currT = 0


for (dirpath, dirnames, filenames) in os.walk(mydir):
	for filename in filenames:
		if filename.endswith('.flac'):
			phrase = AudioSegment.from_file(mydir+"//"+filename)
			currT = len(phrase)
			print(currT)
			if(currT > 15500):
				os.remove(mydir+"//"+filename)
				print("TOO LONG")
				exit(3)
			overallT += currT

if(overallT > 60000):
	print("TOO LONG")
	exit(3)
