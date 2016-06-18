#!/usr/bin/env python

import zipfile
import binascii
import itertools
import string
with zipfile.ZipFile('secret.zip','r') as myzip:
	#print myzip.getinfo()
	#print myzip.infolist()
	nameList = myzip.namelist()
	sizeList = []
	crcList = []
	#print 'CRC of each file:'
	#print string.printable
	for i in nameList:
		crcList.append(getattr(myzip.getinfo(i),'CRC'))
		sizeList.append(getattr(myzip.getinfo(i),'file_size'))
		#print getattr(myzip.getinfo(i),'compress_size')
		#print i,' crc: ',crcList[-1]

	prodList = itertools.product(string.printable,repeat=3)
	iterList = []
	iterCrcList = []
	for i in prodList:
		iterList.append(''.join(i))
		iterCrcList.append( binascii.crc32(''.join(i)) & 0xffffffff)
	#print iterCrcList
	for i in range(0,(len(sizeList)-1)):
		print 'find',nameList[i],':',iterList[iterCrcList.index(crcList[i])]

	prodList = itertools.product(string.printable,repeat=2)
	iterList = []
	iterCrcList = []
	for i in prodList:
		iterList.append(''.join(i))
		iterCrcList.append(binascii.crc32(''.join(i)) & 0xffffffff)
	if crcList[-1] in iterCrcList:
		print 'find',nameList[-1],':',iterList[iterCrcList.index(crcList[-1])]