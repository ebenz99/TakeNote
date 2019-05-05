import os
import pickle
import re

mydir = os.getcwd()


toWrite = []
infile = open(mydir+"/pickles/words.pkl", "rb")
info = pickle.load(infile)
for sentence in info:
	mysentence = sentence.lower()
	instances = []
	for inst in re.finditer("take note", mysentence):
		instances.append(inst.start())
	if len(instances) == 0:
		pass
	elif len(instances) == 1:
		toWrite.append(sentence[instances[0]:])
	else:
		print(len(instances))
		for idx, stridx in instances[:-1]:
			toWrite.append(sentence[stridx:instances[idx+1]])
		toWrite.append(sentence[instances[len(instances)-1]:])
infile.close()
os.remove(mydir+"/pickles/words.pkl")

f = open(mydir+"/output/notes.txt","w")
for phrase in toWrite:
	f.write(phrase)
f.close()

