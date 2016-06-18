#!/usr/bin/env python

import random
import sys

mod = 2**30
#incre = raw_input()
#start = 9223372036854775807
fo = open('input6-2.txt','w')
pert = 2**29+2**25+2**12
j = pert
fo.write(str(2**25+2**12)+'\n')  #first write to occupy
for i in range(1,25000):         #fill in all possible slots of pert
	j = (5*j+1 + pert)
	pert >>= 5
	fo.write(str(j%(2**17))+'\n')
x = (2**29+2**25+2**12)          
for i in range(25000, 50000):    #pert x25000 times
	#x += 2**17
	fo.write(str(x) + '\n')

#print count
fo.close