# Vingenere challenge in Seccon CTF 2016
A little practice for CTF beginner.

##### Quick intro:
 - key: unknown
 - plaintext: SECCON{???????????????????????????????????}
 - ciphertext: LMIG}RPEDOEEWKJIQIWKJWMNDTSR}TFVUFWYOCBAJBQ
 - md5(plaintext): f528a6ab914c1ecf856a1d93103948fe

Encryption process:
*|ABCDEFGHIJKLMNOPQRSTUVWXYZ{}
-----------------------------
A|ABCDEFGHIJKLMNOPQRSTUVWXYZ{}
B|BCDEFGHIJKLMNOPQRSTUVWXYZ{}A
...
Z|Z{}ABCDEFGHIJKLMNOPQRSTUVWXY
{ |{}ABCDEFGHIJKLMNOPQRSTUVWXYZ
} |}ABCDEFGHIJKLMNOPQRSTUVWXYZ{