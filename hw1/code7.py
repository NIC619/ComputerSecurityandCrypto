#60874 fox
import base64, hashlib
import random, string
from pwn import *
s1 = 'fox||818047\n'
h = 'xL7B5Q8TAhKfKp0Gvp/gBJ9OEn11y+7L4vK1wbf6NEg=\n'
def brutal():
	conn = remote('soc12.csie.ntu.edu.tw', 20100)
	conn.send(s1)
	conn.recvline()
	conn.send(h)
	reply = conn.recvline()
	#print reply
	if reply[0] == 'H':
		print reply
		return True
	conn.close()
if __name__ == '__main__':
	while True:
		if brutal() == True:
			break