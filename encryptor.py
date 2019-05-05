import math
import string
from mod import Mod

alphabets = dict(zip(string.ascii_lowercase, range(0,26)))
print(alphabets)
with open('publickeys.rsaconf', 'r') as keyfile:
    n = int(keyfile.readline())
    e = int(keyfile.readline())
    
    message = input("Enter message to encrypt ")
    numMessage = []
    encryptedMessage = []
    for char in message:
        numMessage.append(alphabets[char])
    for char in numMessage:
        encryptedChar = char
        for i in range(1,e):
            encryptedChar = (encryptedChar*char) % n
        encryptedMessage.append(encryptedChar)
    print(encryptedMessage)
