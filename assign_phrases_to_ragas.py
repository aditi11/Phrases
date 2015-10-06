import json
import csv
import os

svar_map={'S':[0,12],'r':[1,13],'R':[2,14],'g':[3,15],'G':[4,16],'m':[5,17],'M':[6,18],'P':[-5,7,19],'d':[-4,8],'D':[-3,9],'n':[-2,10],'N':[-1,11]}
single_map={'S':0,'r':1,'R':2,'g':3,'G':4,'m':5,'M':6,'P':7,'d':8,'D':9,'n':10,'N':11}
svar_index_map={}

input_file=open('all_possible_permutations.json','r')
phrases=json.load(input_file)

input_file=open(os.path.join('../data','nodes.csv'),'r')
nodes=csv.reader(input_file)

input_file=open(os.path.join('../data','edges.csv'),'r')
edges=csv.reader(input_file)

ragas=[]
binary_aaroh=[]
binary_avroh=[]

for i in nodes:
	if i[1]=='raga':
		ragas.append(int(i[0]))
		binary_aaroh.append('100000000000')
		binary_avroh.append('100000000000')
	elif i[1]=='svar':
		svar_index_map[int(i[0])]=i[2]

for i in edges:
	if len(i[2])<=3:
		svar=int(i[1])
		raga=int(i[0])
		if i[2][0]=='a':
			binary_aaroh[ragas.index(raga)]=binary_aaroh[ragas.index(raga)][:single_map[svar_index_map[svar]]]+'1'+binary_aaroh[ragas.index(raga)][single_map[svar_index_map[svar]]+1:]
		else:
			binary_avroh[ragas.index(raga)]=binary_avroh[ragas.index(raga)][:single_map[svar_index_map[svar]]]+'1'+binary_avroh[ragas.index(raga)][single_map[svar_index_map[svar]]+1:]

possible_phrases_aaroh=[]
possible_phrases_avroh=[]
raga_id=ragas.index(105)

for k in phrases:
	print k
	for i in phrases[k]:
		flag1=0
		flag2=0
		for j in i:
			j=int(j)
			if j<0:
				if binary_aaroh[raga_id][j+12]=='0':
					flag1=1
					break
			elif j>11:
				if binary_aaroh[raga_id][j-12]=='0':
					flag1=1
					break
			else:
				if binary_aaroh[raga_id][j]=='0':
					flag1=1
					break
		if flag1==0:
			possible_phrases_aaroh.append(i)
		for j in i:
			j=int(j)
			if j<0:
				if binary_avroh[raga_id][j+12]=='0':
					flag2=1
					break
			elif j>11:
				if binary_avroh[raga_id][j-12]=='0':
					flag2=1
					break
			else:
				if binary_avroh[raga_id][j]=='0':
					flag2=1
					break
		if flag2==0:
			possible_phrases_avroh.append(i)
	
output_file=open('raga_phrase_aaroh_avroh_map.json','w')
output_file.write('Raga: 105\nAaroh: ')
json.dump(possible_phrases_aaroh,output_file,indent=2)
output_file.write('\nAvroh: ')
json.dump(possible_phrases_avroh,output_file,indent=2)
output_file.close()
