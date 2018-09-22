import re

fileBuffer = ""
with open('names.txt', 'r') as fileO:
	fileBuffer = fileO.read()

mObj = re.findall(r'([a-zA-Z]+)', fileBuffer, re.I)

if mObj:
	with open('names.json', 'w') as fileO:
		fileO.write("[\n")
		for mm in mObj:
			fileO.write("\"")
			fileO.write(mm)
			fileO.write("\",\n")
		fileO.write("]\n")
