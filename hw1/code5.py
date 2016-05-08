import hashlib, time
import random, string
from pwn import *
s1 = "ineed"
#zb7X
md5S1 = "b1f0ba98f39fd533494ee3120e712156"
s=string.lowercase+string.digits+string.uppercase
def brutal():
	while True:
		for i in range(2,10):
			for j in range(36**i):
				s2 = ''.join(random.sample(s,i))
				print s2,
				md5Final = hashlib.md5(s2 + md5S1).hexdigest()
				print md5Final
				count = 0
				index = 0
				for k in md5Final:
					if k == 'f':
						count += 1
					if index == 4:
						break
					index += 1
				if count == 5:
					return md5Final
if __name__ == '__main__':
	conn = remote('soc12.csie.ntu.edu.tw', 20080)
	rcv = conn.recvline()
	conn.send(s1+'\n')
	rcv = conn.recvline()
	conn.send(md5S1+'\n')
	rcv = conn.recv()
	#md5S2 = hashlib.md5('zb7X').hexdigest()
	conn.send('zb7X\n')
	rcv = conn.recvline()
	print rcv