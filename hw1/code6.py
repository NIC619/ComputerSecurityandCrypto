import hashlib, time
import random, string

def ROR(b, n, width):
    return ((b << (width-n)) & (2**width-1)) | (b >> n)

def SHA384(m):
    return int(hashlib.sha384(m).hexdigest(), 16)

def compress(i, m, c):
    assert len(m) == 1
    x = SHA384(m)
    return x ^ ROR(c, 96, 384)

def myhash(m):
    IV = ord('C') ^ ord('N') ^ ord('S') ^ ord('c') ^ ord('n') ^ ord('s')
    c = IV
    for i, mb in enumerate(m):
        c = compress(i, mb, c)
    out = c + (len(m) % 24)
    return hex(out)[2:-1]

s1 = "HHGNucXFrMkntG"
md5S2 = "9718cd8b1fd3c209ebf6c08e09cb0199"
myhashS1 = myhash(s1)
s=string.lowercase+string.uppercase+string.digits

mainList = []
#mainList.append(["12345", "1"])

def brutal():
	for i in range(6,7):
		for j in range(100000):
			match = 0
			s2 = ''.join(random.sample(s,i))
			#print s2,
			#md5Final = hashlib.md5(s2).hexdigest()
			#print md5Final
			myhashS2 = myhash(s2)
			#print myhashS2
			for k in mainList:
				if myhashS2 == k[0]:
					k.append(s2)
					match = 1
			if match == 1:
				match = 0
			else:
				mainList.append([myhashS2, s2])
			#if myhashS2 == myhashS1 and md5Final == md5S2:
			#	return
	for i in mainList:
		if len(i) > 2:
			print i

if __name__ == '__main__':
	brutal()