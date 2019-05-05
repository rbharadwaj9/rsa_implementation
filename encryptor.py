import math
import string

alphabets = dict(zip(string.ascii_lowercase, range(0,26)))
print(alphabets)
with open('keys.rsaconf', 'r') as keyfile:
    n = keyfile.readline()
    e = keyfile.readline()
    
    message = input("Enter message to encrypt ")
    numMessage = []
    for char in message:
        numMessage.append(alphabets[char])
    print(numMessage)     
