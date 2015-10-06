import itertools
import json

generated_permutations={2:[],3:[],4:[],5:[]}
filtered_permutations={2:[],3:[],4:[],5:[]}


indices=[]
for i in range(-5,20,1):
	indices.append(i)

generated_permutations[2]=list(itertools.product(indices,repeat=2))
generated_permutations[3]=list(itertools.product(indices,repeat=3))
generated_permutations[4]=list(itertools.product(indices,repeat=4))
generated_permutations[5]=list(itertools.product(indices,repeat=5))

for i in generated_permutations:
	for j in generated_permutations[i]:
		if max(j)-min(j)<=10:
			filtered_permutations[i].append(j)

writefile=open('all_possible_permutations.json','w')
json.dump(filtered_permutations,writefile,indent=2)
