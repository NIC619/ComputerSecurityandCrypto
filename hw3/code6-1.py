#!/usr/bin/env python

import random

incre = 2**30
fo = open('input6-1.txt','w')
for i in range(1,50001):
	#print i
	fo.write(str((62233*i)%incre)+'\n')
	
fo.close