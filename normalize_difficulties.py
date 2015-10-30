import json
import csv
import os
import ast
import math

svar_map={'S':[0,12],'r':[1,13],'R':[2,14],'g':[3,15],'G':[4,16],'m':[5,17],'M':[6,18],'P':[-5,7,19],'d':[-4,8],'D':[-3,9],'n':[-2,10],'N':[-1,11]}
single_map={'S':0,'r':1,'R':2,'g':3,'G':4,'m':5,'M':6,'P':7,'d':8,'D':9,'n':10,'N':11}
svar_index_map={}

input_file=open('nodes.csv','r')
nodes=csv.reader(input_file)

input_file=open('edges.csv','r')
edges=csv.reader(input_file)

ragas=[]
raganames=[]
binary_aaroh=[]
binary_avroh=[]

for i in nodes:
	if i[1]=='raga':
		ragas.append(int(i[0]))
		raganames.append(i[2])
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

musigmafile=open('raga_stats.csv','w')
fields=['RagaID','RagaName','Mu','Sigma']
musigmawriter=csv.DictWriter(musigmafile,fieldnames=fields)
musigmawriter.writeheader()

for l in range(len(ragas)):
	print ragas[l]
	possible_phrases=[]
	writefile=open(str(ragas[l])+'.csv','w')
	fieldnames=['PhraseID','Difficulty','Normalized Difficulty']
	writer=csv.DictWriter(writefile,fieldnames=fieldnames)
	writer.writeheader()
	index=1
	csvfile=open('difficulty.csv','r')
	phrases=csv.DictReader(csvfile)
	mindiff=1000
	maxdiff=0
	abs_difficulties=[]
	for k in phrases:
		i=ast.literal_eval(k['Phrase'])
		diff=float(k['Difficulty'])
		aaroh_exists=0
		avroh_exists=0
		for j in i:
			j=int(j)
			if j<0:
				if binary_aaroh[ragas[l]][j+12]=='0':
					aaroh_exists=1
					break
			elif j>11:
				if binary_aaroh[ragas[l]][j-12]=='0':
					aaroh_exists=1
					break
			else:
				if binary_aaroh[ragas[l]][j]=='0':
					aaroh_exists=1
					break
		if aaroh_exists==0:
			possible_phrases.append([index,diff])
			abs_difficulties.append(diff)
			if diff>maxdiff:
				maxdiff=diff
			if diff<mindiff:
				mindiff=diff
		for j in i:
			j=int(j)
			if j<0:
				if binary_avroh[ragas[l]][j+12]=='0':
					avroh_exists=1
					break
			elif j>11:
				if binary_avroh[ragas[l]][j-12]=='0':
					avroh_exists=1
					break
			else:
				if binary_avroh[ragas[l]][j]=='0':
					avroh_exists=1
					break
		if avroh_exists==0 and [index,diff] not in possible_phrases:
			possible_phrases.append([index,diff])
			abs_difficulties.append(diff)
			if diff>maxdiff:
				maxdiff=diff
			if diff<mindiff:
				mindiff=diff
		index=index+1
	for k in possible_phrases:
		k.append(float(float(k[1])-mindiff)/(maxdiff-mindiff))
		writer.writerow({'PhraseID':k[0],'Difficulty':k[1],'Normalized Difficulty':k[2]})
	mu=float(sum(abs_difficulties))/len(abs_difficulties)
	var=0
	for k in abs_difficulties:
		var=var+(k-mu)*(k-mu)
	var=float(var)/len(abs_difficulties)
	sigma=math.sqrt(var)
	musigmawriter.writerow({'RagaID':ragas[l],'RagaName':raganames[l],'Mu':mu,'Sigma':sigma})
	writefile.close()
	csvfile.close()
musigmafile.close()
