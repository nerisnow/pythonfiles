from caesarcipher import  CaesarCipher
import random
from niri import caesar_cipher
cipher=CaesarCipher('Ie',offset=2)
print(cipher.encoded)
def generateRandomString():
    strings = ''
    for i in range(1,100):
        raand=random.randint(65,123)
        strint=chr(raand)
        strings=strings+strint
    print(strings)
    ciphers=CaesarCipher(strings,offset=2)
    print(ciphers.encoded)
    caesar_cipher(strings, 2)
generateRandomString()

