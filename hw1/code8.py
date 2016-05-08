import base64, hashlib
import random, string
from pwn import *


def brutal():
	conn = remote('soc12.csie.ntu.edu.tw', 20110)
	r = conn.recvline()
	r = conn.recvline()
	Nc = str(random.randint(100, 999))
	digest = base64.b64encode(hashlib.sha256('admin||'+Nc).digest())
	s = "admin||" + Nc + "||" + digest+'\n'
	conn.send(s)
	r = conn.recv()
	recv = conn.recvline()
	recv = recv.split('||')
	r = conn.recv()
	s = recv[1]+'||'+base64.b64encode(hashlib.sha256(recv[1]).digest())+'\n'
	conn.send(s)
	reply = conn.recvall()
	conn.close()
	if Nc == recv[0]:
		print reply
		return True
	else:
		return False
if __name__ == '__main__':
	while True:
		if brutal() == True:
			break