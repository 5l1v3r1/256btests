#!/usr/bin/env python
import sys
import fileinput

P = 115792089237316195423570985008687907853269984665640564039457584007908834671663L
N = 115792089237316195423570985008687907852837564279074904382605163141518161494337L



#skip = int("00000000000000000000000000000000000000000000000000000027eb78574a",16)
skip = 0

def hexify(i):
	return hex(i).replace('0x','').replace('L','').zfill(64)

data = []
for line in fileinput.input():
	line = line.replace('0x','').replace('L','').replace('\n','')
	try:
		data.append(line)
	except:
		pass

#import random
#random.shuffle(data)

start = 0
end = len(data) -1
mid = int(end / 2)

def prepare(data):
	data2 = []
	for k in range(mid,end):
		data2.append(data[k])
	for k in range(mid,start,-1):
		data2.append(data[k])

	return data2

def invert(data):
	data2 = []
	for k in range(start,end):
		data2.append(data[k])
	return data2

for i in range(start,end):
	for j in range(start,end):
		#if i != j:
		s = data[i] + data[j]
		print s
		print s.title()
		s = data[i] + " " + data[j]
		print s
		print s.title()
		s = data[i].lower() + data[j].lower()
		print s
		print s.title()
		s = data[i].lower() + " " + data[j].lower()
		print s
		print s.title()
		s = data[i].upper() + data[j].upper()
		s = data[i].upper() + " " + data[j].upper()
		s = data[i].lower() + data[j].upper()
		print s
		print s.title()
		s = data[i].lower() + " " + data[j].upper()
		print s.title()
		s = data[i].upper() + data[j].lower()
		print s
		print s.title()
		s = data[i].upper() + " " + data[j].lower()
		print s
		print s.title()





