import numpy as np
import matplotlib.pyplot as plt
	
inputfile=open('tohist.txt','r')
lines=inputfile.readlines()
frequency={}
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
		sequence=notes[j]+' '+notes[j+1]
		if sequence in frequency:
			frequency[sequence]=frequency[sequence]+1
		else:
			frequency[sequence]=1
		if j<len(notes)-2:
			sequence=sequence+' '+notes[j+2]
		else:
			continue
		if sequence in frequency:
		 	frequency[sequence]=frequency[sequence]+1
		else:
		 	frequency[sequence]=1
		if j<len(notes)-3:
			sequence=sequence+' '+notes[j+3]
		else:
			continue
		if sequence in frequency:
		 	frequency[sequence]=frequency[sequence]+1
		else:
		 	frequency[sequence]=1
		if j<len(notes)-4:
			sequence=sequence+' '+notes[j+4]
		else:
			continue	
		if sequence in frequency:
		 	frequency[sequence]=frequency[sequence]+1
		else:
			frequency[sequence]=1
'''print frequency
x=np.arange(len(frequency))
plt.bar(x,frequency.values(),align='center',width=0.5)
#plt.xticks(x,frequency.keys())
plt.xlim(0,500)
max_freq=max(frequency.values())+1
plt.ylim(0,max_freq)
plt.show()'''

inputfile.close()
outputfile=open('histogram.txt','w')
for i in frequency:
	outputfile.write(i+' : '+str(frequency[i])+'\n')
