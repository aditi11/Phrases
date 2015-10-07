import json
import csv
from math import exp

input_file=open('all_possible_permutations.json','r')
phrases=json.load(input_file)
#svars={"shuddh":[-5,-3,-1,0,2,4,5,7,9,11,12,14,16,17,19],"komal":[-4,-2,1,3,6,8,10,13,15,18]}
#adjacency=[[-4,-3],[-2,-1],[1,2],[3,4],[5,6],[8,9],[10,11],[13,14],[15,16],[17,18]]
consonance=[0,12,7,5,4,9,-5,19,17,3,8,-3,16,-4,15,2,14,-1,11,-2,10,6,18,1,13]
interval=[0,2,4,7,5,3,1,9,10,8,6]


csvfile=open('difficulty.csv','w')
fieldnames=['Phrase','Number','Span','Consonance','Interval','Consequent svars','Difficulty']
writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
writer.writeheader()


for i in phrases:
	number=int(i)
	for j in phrases[i]:
		minimum=min(j)
		maximum=max(j)
		span=maximum-minimum
		'''komal_svars=0
		for k in j:
			if k in svars["komal"]:
				komal_svars=komal_svars+1
		order=0
		for k in range(len(j)-1):
			order=order+abs(j[k]-j[k+1])
		order=float(order)/number
		adjacent_pairs=0
		for k in range(len(j)-1):
			temp=[]
			temp.append(j[k])
			if j[k+1]>j[k]:
				temp.append(j[k+1])
			else:
				temp.insert(0,j[k+1])
			if temp in adjacency:
				adjacent_pairs=adjacent_pairs+1
		complexity=komal_svars+(2*adjacent_pairs)
		if order==0:
		  	difficulty=0
		else:
			difficulty=(float((float(span)/number)+number+complexity))/(order*order)
			difficulty='%.3f'%difficulty'''
		differences=0
		cons=0
		for k in range(len(j)-1):
			differences=differences+interval.index(abs(j[k]-j[k+1]))
		for k in j:
			cons=cons+exp(float(consonance.index(k)/10))
		consecutive=0
		count_dict={}
		for k in j:
			if k not in count_dict:
				count_dict[k]=0
		count=0
		index=0
		while index<number-1:
			if j[index]==j[index+1]:
				count=count+1
				if index==number-2:
					if count>count_dict[j[index]]:
						count_dict[j[index]]=count+1
				index=index+1
			else:
				if count>count_dict[j[index]]:
					count_dict[j[index]]=count+1
					count=0
				index=index+1
		consequent=0
		for k in count_dict:
			consequent=consequent+count_dict[k]
		difficulty=cons+differences+float(span)/number+number-consequent
		writer.writerow({'Phrase':j,'Number':number,'Span':span,'Consonance':'%.3f'%cons,'Interval':differences,'Consequent svars':consequent,'Difficulty':difficulty})

csvfile.close()
