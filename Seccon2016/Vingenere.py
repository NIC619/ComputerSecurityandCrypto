import itertools
import hashlib

#https://score-quals.seccon.jp/question/
#c_x are the known cipher text , p_x are the known plain text
'''
c_1 = 'EDOEE'
c_2 = 'KJWMN'
c_3 = 'VUFWY'

p_1 = 'SECCON{'
p_2 = 'BCDEDEF'
p_3 = 'KLMNOPQ'
p_4 = 'VWXYYZ}'

cc_x are decrypted cipher text using key in combi set, i.e, guessed plaintext
'''

#letters used in here ABC.....XYZ{}
s = string.uppercase + '{' + '}'

#new ord() and chr() for decryption using the particular set of letters shown above
def new_ord(a):
	if a == '{':
		return 26
	elif a == '}':
		return 27
	else:
		return ord(a)-65

def new_chr(n):
	if n == 26:
		return '{'
	elif n == 27:
		return '}'
	else:
		return chr(n+65)
#if the set of letters used are just alphabets, new_ord() and new_chr() won't be needed

combi = itertools.product(s, repeat = 5)			#combination of all possible key
for i in combi:
	cc_1 = ''										
	cc_2 = ''
	cc_3 = ''
	for j,k in enumerate(i):
		ord_1 = (new_ord(c_1[j]) - new_ord(k) + 28)%28
		cc_1 += new_chr( ord_1 )

		ord_2 = (new_ord(c_2[j]) - new_ord(k) + 28)%28
		cc_2 += new_chr( ord_2 )

		ord_3 = (new_ord(c_3[j]) - new_ord(k) + 28)%28
		cc_3 += new_chr( ord_3 )

	p = p_1 + cc_1 + p_2 + cc_2 + p_3 + cc_3 + p_4	#put all plaintest pieces together
	if hashlib.md5(p).digest().encode('hex') == 'f528a6ab914c1ecf856a1d93103948fe':
		print p
