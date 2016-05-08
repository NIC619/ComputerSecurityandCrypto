import base64, hashlib
import random, string
import hmac
import math
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto import Random
from pwn import *
import itertools


def congruence(e,r):
	for i in range(r):
		if (e*i)%r == 1:
			return i

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def Solution():
	
	modu = '00:97:6a:14:48:a9:3e:12:93:7d:ca:66:8d:8d:51:fa:08:b7:64:a2:ed:12:7f:e0:d0:c3:96:1f:e8:f9'
	modu = ''.join(modu.split(":"))
	modu = int(modu,16)#4082123393941291671559653511747861522931371507349333528634013081659641
	#print modu2
	#prime = int(math.sqrt(modu2))
	#print prime_factors(modu2)
	p = 56456123156879545631321597123651131
	q = 72306123156879545631321683567941211
	#pq_congruence = 43706775814646142816742434194415603
	r = (p-1)*(q-1)
	#d = congruence(65537, r)
	d = 3230593587594168696112318065219869372567799064509384093990804067064873
	#use command openssl asn1parse -genconf to construct key pair base on inputs above
	f1 = open('flag.enc','r')
	flag = f1.read()
	f1.close()
	dec =  base64.b64decode(flag)
	f = open('flag', 'w')
	f.write(dec)
	f.close()

if __name__ == '__main__':
	Solution()