#!/usr/bin/python

import signal, os, sys
import time
import hashlib

#import secret

sys.dont_write_bytecode = True

def alarm(time):
    def handler(signum, frame):
        print 'Timeout!'
        exit()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(time)

def md5(m):
    return hashlib.md5(m).hexdigest()

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


'''if  __name__ =='__main__':
    alarm(20)
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', 0)
    
    S1, md5_S2 = secret.gen_string()
    
    print "S1 =", S1
    print "myhash(S1) =", myhash(S1)
    print "Give me S2 such that myhash(S1) = myhash(S2) and md5(S2) =", md5_S2

    S2 = raw_input()
    
    if myhash(S1) == myhash(S2) and md5(S2) == md5_S2 and S2 == secret.S2:
        print 'Here\'s the flag: ' + secret.FLAG'''

