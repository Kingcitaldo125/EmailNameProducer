import json
import random

names = json.loads(open('names.json').read())

def produceNames(numbr):
	global names
	nms = []
	for i in range(numbr):
		name = ""
		name += names[random.randrange(0,len(names))]
		name += str(random.randrange(0,100))
		name += "@yahoo.com"
		nms.append(name)
	return nms

nameListLength = 50
with open("emails.json", "w") as ff:
	ff.write("[\n")
	for ii,pp in enumerate(produceNames(nameListLength)):
		ff.write(pp)
		if ii == nameListLength-1:
			ff.write("\n")
		else:
			ff.write(",\n")
	ff.write("]\n")
