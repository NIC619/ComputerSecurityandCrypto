Problem 6:
	I use openssl to complete key transform and decryption.
	And since prime-factorizatuin takes too long, I just store
	each values of RSA public/private key components. Then I
	build private key by creating key.txt and commands below:
		1. openssl asn1parse -genconf key.txt -out key.der
		2. openssl rsa -in key.der -inform der -outform pem -check -out key.pem
	And by running code6.py, flag, which is the base64 decoded
	version of flag.enc, will be created.
	Finally, with command:
		3. openssl rsautl -raw -decrypt -in flag -inkey key.pem
	to complete decryption.



Problem 7:
	First, use command:
		1. openssl req -in Meow.csr -text -noout
	to extract public key and transform it to interger.
	Second, just like problem 6, build private key with key.txt
	and the 1st and 2nd commands in problem 6. Then use the private
	key to decrypt:
		2. openssl rsautl -raw -decrypt -in flag2 -inkey key2.pem -out pswd.bin
	Finally, run code7 to use the password to log into the server.


Problem 8:
	use command:
		1. openssl req -x509 -newkey rsa:2048 -out ans8.cert -nodes -days 30
	and fill out the information to create self-signed certificate.
	Key : CNS{And_Teh_BeTa_Key_IS___JOHN_CENA!!DODODODOOOO~}