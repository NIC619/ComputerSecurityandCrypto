import base64, hashlib
import random, string
import hmac
from itertools import izip_longest
from pwn import *

ipad = ''
for i in range(64):
	ipad += '\x36'
ipod = ''
for i in range(64):
	ipod += '\x5c'

hash1 = 'a4e2634f4138ce958306b549f9b342317f8a2b7b'            #calculated hash of ipad||'null'
len_ext_atk_hash = 'e4381882f945f2aad90141c90ea67ea68ec363e7' #calculated hash of lenth_extension_attack of hash1||'&number=-1000000'
hash2 = 'df9e0df4959d5a60b5febcd6bd4f6d1807ee9a90'            #calculated hash of ipod||len_ext_atk_hash
data = 'null' + '800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000220266e756d6265723d2d31303030303030'.decode('hex') + '||'
#print data
'''def HMAC(data):
    return hmac.new(secretKey, data, hashlib.sha1).hexdigest()
def strxor(s1, s2):
	res = ''
	for a, b in izip_longest(s1, s2):
		if a == None: res += b
		elif b == None: res += a
		else: res += chr(ord(a) ^ ord(b))
	return res
'''
def brutal():
	conn = remote('soc12.csie.ntu.edu.tw', 20120)
	rcv = conn.recv()

	#data1 = ipad + 'null\n'
	#conn.send('4\n')
	#rcv = conn.recv()
	#conn.send(data1)
	#rcv = conn.recv()
	#print rcv
	#rcv = conn.recv()
	#data1 = ipod + len_ext_atk_hash.decode('hex') + '\n'
	#conn.send('4\n')
	#rcv = conn.recv()
	#conn.send(data1)
	#rcv = conn.recv()
	#print rcv
	#rcv = conn.recv()
	conn.send('2\n')
	conn.recv()
	conn.send(data + hash2 + '\n')
	rcv = conn.recv()
	rcv = conn.recv()
	#print rcv
	conn.send('5\n')
	rcv = conn.recv()
	print rcv
	conn.close()
if __name__ == '__main__':
	brutal()