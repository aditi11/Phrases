import json
import ast

filename=open('permutations.json')
phrases=json.load(filename)
svars=['S','r','R','g','G','m','M','P','d','D','n','N']
transpositions={"3":[],"4":[],"5":[]}

for i in phrases:
	for j in phrases[i]:
		indices=[]
		for k in range(len(j)):
			indices.append((svars.index(str(j[k]))-5)%12)
		for k in range(12):
			sequence=''
			for l in indices:
				sequence=sequence+svars[l]
			if sequence not in transpositions[i]:
				transpositions[i].append(sequence)
			for l in range(len(indices)):
				indices[l]=(indices[l]+1)%12

filename.close()
writefile=open('transpositions.json','w')
json.dump(transpositions,writefile,indent=7)
