#!/usr/bin/python
import signal
import sys
import os
import time
import random
import string
from math import sin
from urlparse import parse_qs
from base64 import b64encode
from base64 import b64decode
from re import match
from Crypto.Cipher import AES

import secret
FLAG = secret.FLAG
SALT = secret.SALT[:96]
KEY = secret.KEY
IV = secret.IV
REVOKED_NUM = secret.REVOKED_NUM

USERS = set()

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[-1])]

def AES_encrypt(m):
    m = pad(m)
    aes = AES.new(KEY, AES.MODE_OFB, IV)
    return b64encode(aes.encrypt(m))

def AES_decrypt(c):
    c = b64decode(c)
    aes = AES.new(KEY, AES.MODE_OFB, IV)
    return unpad(aes.decrypt(c))


def alarm(time):
    def handler(signum, frame):
        print 'Timeout'
        exit()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(time)

def myhash(s):
    assert(len(s) < 2**30)
    def G(X,Y,Z):
        return ((X & Z) | (~Z & Y)) & 0xFFFFFFFF
    def H(X,Y,Z):
        return (X ^ Y ^ Z) & 0xFFFFFFFF
    def I(X,Y,Z):
        return (Y ^ (~Z | X)) & 0xFFFFFFFF
    def J(X,Y,Z):
        return ((~X & Z) | (~X & Z ^ ~Y)) & 0xFFFFFFFF
    def K(X,Y,Z):
        return ((~X ^ ~Z) | (~X & Y)) & 0xFFFFFFFF
    def L(X,Y,Z):
        return ((~X & Y ^ Z) | (X & Y)) & 0xFFFFFFFF
    def ROL(X,Y):
        return (X << Y | X >> (32 - Y)) & 0xFFFFFFFF

    A = 0x6A09E667
    B = 0xBB67AE85
    C = 0x3C6EF372
    D = 0xA54FF53A
    E = 0x510E527F
    F = 0x9B05688C
    X = [int(0xFFFFFFFF * sin(i)) & 0xFFFFFFFF for i in xrange(256)]

    s_size = len(s)
    s += chr(0xc0)
    if len(s) % 72 > 64:
        while len(s) % 72 != 0: s += chr(0)
    while len(s) % 72 < 64: s += chr(0)
    s += hex(s_size * 8)[2:].rjust(16, '0').decode('hex')

    for i, ch in enumerate(s):
        k, l = ord(ch), i & 0x1f
        A = (B + ROL(A + G(B,C,D) + X[k], l)) & 0xFFFFFFFF
        B = (C + ROL(B + H(C,D,E) + X[k], l)) & 0xFFFFFFFF
        C = (D + ROL(C + I(D,E,F) + X[k], l)) & 0xFFFFFFFF
        D = (E + ROL(D + J(E,F,A) + X[k], l)) & 0xFFFFFFFF
        E = (F + ROL(E + K(F,A,B) + X[k], l)) & 0xFFFFFFFF
        F = (A + ROL(F + L(A,B,C) + X[k], l)) & 0xFFFFFFFF

    return ''.join(map(lambda x : hex(x)[2:].strip('L').rjust(8, '0'), [B, A, D, E, C, F]))

def gen_identification(login):
    global SALT, KEY
    s = 'login=%s' % login + '&role=guest'
    s += myhash(SALT + s)
    s = AES_encrypt(s)
    return s

def register():
    global USERS
    name = raw_input('Your login name: ').strip()
    if not match('^[\w]+$', name):
        print '[-] Wrong'
        return
    if len(USERS) > 0:
        print '[-] User group is already full'
    else:
        USERS.add(name)
        print '[+] Good login name\nYour identification:\n%s' % gen_identification(name)

def authentication():
    global SALT, KEY
    identification = raw_input('Provide your identification:\n').strip()
    try:
        identification = AES_decrypt(identification)
        auth_str, hashsum = identification[0:-48], identification[-48:]
        if myhash(SALT + auth_str) == hashsum:
            data = parse_qs(auth_str, strict_parsing = True)
            if 'revoked' in data:
                print '[-] Authentication failed: revoked identification'
                return
            print '[+] Welcome, %s!' % data['login'][0]
            if 'admin' in data['role']:
                print FLAG
        else:
            print '[-] Authentication failed'
    except:
        print '[-] Error'

def revoked_identification():
    global SALT, KEY, REVOKED_NUM
    if REVOKED_NUM <= 0:
        return
    name = ''.join([random.choice(string.letters + string.digits) for _ in xrange(64)])
    revoked_token = ''.join([random.choice(string.letters + string.digits) for _ in xrange(64)])
    s = 'login=%s&revoked=%s' % (name, revoked_token)
    s += myhash(SALT + s)
    s = AES_encrypt(s)
    print s
    REVOKED_NUM -= 1


def main():
    while True:
        print
        print '----------------------'
        print '[0] Register'
        print '[1] Login'
        print '[2] Revoked identification'
        print '----------------------'
        num = raw_input().strip()
        if num == '0':
            register()
        elif num == '1':
            authentication()
        elif num == '2':
            revoked_identification()

if __name__ == '__main__':
    alarm(60)
    sys.dont_write_bytecode = True
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', 0)
    time.sleep(2)
    main()


