#!/usr/bin/python

import string
import commands


maxin = 0
index = 0
for i in string.printable:
	fo = open('try','w')
	pswd = 'CNS{T0p_Secr3t_0xFbf6bDc3C3Ed2F43eb1edd7c3EFbBa36}'
	#pswd += i
	#for j in range(0, 1):
	#	pswd += '+'
	pswd += '\n'
	#print pswd
	fo.write(pswd)
	fo.close()
	output = commands.getoutput('perf stat -e instructions:u ./timing-atk < try')
	#print '1',output
	intru = int(output.split()[5].replace(",", ""))
	if intru > maxin:
		maxin = intru
		index = i
print maxin,index