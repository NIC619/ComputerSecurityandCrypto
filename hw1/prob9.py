import signal
import sys
import os
import time
import hashlib
import hmac
from urlparse import parse_qsl
from itertools import izip_longest

sys.dont_write_bytecode = True
import secret

def alarm(time):
    def handler(signum, frame):
        print 'Timeout'
        exit()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(time)

def get_number(msg):
    number = raw_input(msg)
    try:
        number = int(number)
    except:
        return 0
    return number

def HMAC(data):
    return hmac.new(secret.KEY, data, hashlib.sha1).hexdigest()

def pick():
    number = get_number('How many you want to buy: ')
    if number <= 0:
        print 'What?'
    else:
        data = 'number=%d&price=10' % number
        print 'This is your order token, you can check out by this token'
        print data + '||' + HMAC(data)

def check_out():
    token = raw_input('Give me your order token: ')
    try:
        data, h = token.split('||')
        if HMAC(data) != h:
            print 'Verification error'
            return
        number =  dict(parse_qsl(data)).get('number', 0)
        price = dict(parse_qsl(data)).get('price', 10)

        try:
            number = int(number)
            price = int(price)
        except ValueError:
            number = 0
            price = 10
        if not isinstance(number, int) or not isinstance(price, int):
            return

        print 'You buy %d apple(s) and total price is %d' % (number, number * price)
        if number * price > secret.MONEY:
            print 'You don\'t have enough money'
        else:
            secret.MONEY -= number * price
            print 'Thank you for your purchasing'
    except:
        print 'This is not the token'

def show_money():
    print 'You have $%d' % secret.MONEY

def hash_service():
    def strxor(s1, s2):
        res = ''
        for a, b in izip_longest(s1, s2):
            if a == None: res += b
            elif b == None: res += a
            else: res += chr(ord(a) ^ ord(b))
        return res

    data = raw_input('Input the data and pay me $300, I can do hash for you: ')
    if data.find('number') != -1 or data.find('price') != -1:
        print 'System crashes...'
    elif secret.MONEY < 300:
        print 'You don\'t have enough money'
    else:
        secret.MONEY -= 300
        print hashlib.sha1(strxor(secret.KEY, data)).hexdigest()

def buy_flag():
    if secret.MONEY > 10000000:
        print 'Yay, the flag is %s' % secret.FLAG 
    else:
        print 'You don\'t have enough money'

def board():
    time.sleep(0.5)
    print '''
    -----------------------------------
    Welcome to Shopping Mall.
    [1] Pick apples into shopping cart
    [2] Check out
    [3] Show money
    [4] Hash service
    [5] Buy flag
    [6] Exit
    -----------------------------------
    '''

if __name__ == '__main__':
    alarm(30)
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', 0)
    secret.KEY = secret.KEY[:60]

    while True:
        board()
        choice = get_number('Input your choice: ')
        if choice == 1:
            pick()
        elif choice == 2:
            check_out()
        elif choice == 3:
            show_money()    
        elif choice == 4:
            hash_service()
        elif choice == 5:
            buy_flag()
        else:
            print 'Bye'
            exit()
