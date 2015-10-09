import csv
	
inputfile=open('tohist.txt','r')
lines=inputfile.readlines()

class transitions:
	def __init__(self,s,t):
		self.source=s
		self.target=t
		self.frequency=1
	def increment(self):
	 	self.frequency=self.frequency+1

phrases=[]

for i in range(len(lines)):
	line=lines[i].split('\n')
	line=line[0]
	values=line.split(' ')
	notes=[]
	for j in values:
		if j=='':
			continue
		notes.append(j)
	for j in range(len(notes)-1):
		exists=0
		for instance in phrases:
			if instance.source==notes[j] and instance.target==notes[j+1]:
				exists=1
				instance.increment()
				break
		if exists==0:
			phrases.append(transitions(notes[j],notes[j+1]))

	for j in range(len(notes)-2):
		exists=0
		for instance in phrases:
			if instance.source==notes[j]+' '+notes[j+1] and instance.target==notes[j+2]:
				exists=1
				instance.increment()
				break
		if exists==0:
			phrases.append(transitions(notes[j]+' '+notes[j+1],notes[j+2]))
	for j in range(len(notes)-3):
		exists=0
		for instance in phrases:
			if instance.source==notes[j]+' '+notes[j+1] and instance.target==notes[j+2]+' '+notes[j+3]:
				exists=1
				instance.increment()
				break
		if exists==0:
			phrases.append(transitions(notes[j]+' '+notes[j+1],notes[j+2]+' '+notes[j+3]))
	
csvfile=open('transitional_probabilities.csv','w')
fieldnames=['From','To','Probability']
writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
writer.writeheader()
total=0
for i in phrases:
	total=total+i.frequency
for i in phrases:
	writer.writerow({'From':i.source,'To':i.target,'Probability':float(i.frequency)/total})
csvfile.close()
