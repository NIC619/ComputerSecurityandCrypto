#!/usr/bin/python

import signal
import sys
import os
import time
import random
import string
from base64 import b64encode
from Crypto.Cipher import AES
from sympy import isprime

import secret
FLAG1 = secret.FLAG1
FLAG2 = secret.FLAG2
KEY = secret.KEY
IV = ''.join([random.choice(string.letters + string.digits) for i in xrange(16)])
NONCE = 0

def alarm(time):
    def handler(signum, frame):
        print 'Timeout'
        exit()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(time)

def RSA():
    def get_prime():
        while True:
            n = random.randint(2**1023, 2**1024)
            if isprime(n): 
                return n

    p = get_prime()
    q = get_prime()
    e = 65537
    n = p * q
 
    plaintext0 = int(raw_input().encode('hex'), 16)
    plaintext1 = int(FLAG2[:20].encode('hex'), 16)
    plaintext2 = int(FLAG2[20:40].encode('hex'), 16)
    plaintext3 = int(FLAG2[40:].encode('hex'), 16)
    assert plaintext0 < n
    assert plaintext1 < n
    assert plaintext2 < n
    assert plaintext3 < n

    ciphertext0 = pow(plaintext0, e, n)
    ciphertext1 = pow(plaintext1, e, n)
    ciphertext2 = pow(plaintext2, e, n)
    ciphertext3 = pow(plaintext3, e, n)
    print n
    print ciphertext0
    print ciphertext1
    print ciphertext2
    print ciphertext3


def CBC():
    global IV, NONCE
    BS = 16
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    
    plaintext = raw_input()
    if plaintext == 'exit': 
        return False
    data = plaintext + FLAG1 + str(NONCE)
    aes = AES.new(KEY, AES.MODE_CBC, IV)
    ciphertext = aes.encrypt(pad(data))
    IV = ciphertext[-8:].encode('hex')
    print b64encode(ciphertext)
    
    return True


def main():
    global IV, NONCE
    while True:
        print
        print '----------------------'
        print '[0] Defeat AES CBC Mode'
        print '[1] Defeat RSA'
        print '----------------------'
        num = raw_input().strip()
        if num == '0':
            print b64encode(IV)
            NONCE = random.getrandbits(512)
            while CBC(): pass
        elif num == '1':
            RSA()

if __name__ =='__main__':
    alarm(150)
    sys.dont_write_bytecode = True
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', 0)
    time.sleep(2)
    main()
    
    
