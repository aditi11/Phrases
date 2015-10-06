import json
import itertools
from itertools import permutations
from itertools import combinations

svars=['S','r','R','g','G','m','M','P','d','D','n','N']
possible_svars=['S','r','R','g','G','m','M','P']
generated_permutations=[]
string_permutations={3:[],4:[],5:[]}

for i in range(3):
	generated_permutations.append([p for p in itertools.product(possible_svars,repeat=i+2)])

for i in range(len(generated_permutations)):
	for perm in generated_permutations[i]:
		for first_svar in possible_svars:
			old_sequence=first_svar
			for svar in perm:
				old_sequence=old_sequence+svar
			if old_sequence[0]=='S':
				sequence=old_sequence
			else:
				sequence=''
				difference=possible_svars.index(old_sequence[0])
				for j in range(len(old_sequence)):
					sequence=sequence+svars[((possible_svars.index(old_sequence[j])-difference)%12)]
			if sequence not in string_permutations[i+3]: 
				string_permutations[i+3].append(sequence)

output_file=open('permutations.json','w')
json.dump(string_permutations,output_file,indent=7)
