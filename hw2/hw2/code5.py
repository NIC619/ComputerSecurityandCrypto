from Crypto.Cipher import AES
import itertools
#'SMMGSMSSSGGGMSMG'
final = 'f5cc8d697a9e67d62a1a83f0e45a8ae5'.decode('hex')
def Solution():
	iterlist = list(itertools.product(['M','G','S'],repeat = 8))
	leng = len(iterlist)
	for i in range(leng):
		for j in range(leng):
			key = ''.join(iterlist[i]) + ''.join(iterlist[j])
			#print key
			dec = AES.new(key, AES.MODE_ECB )
			pText = dec.decrypt(final)
			if pText == 'CNS{Brutef0RcE!}':
				print key
				print pText
				return

if __name__ == '__main__':
	Solution()