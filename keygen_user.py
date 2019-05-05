import math
import sys
from fractions import gcd

numValid = False
while numValid == False:
    p = input("Enter p: A positive prime number")
    if p > 1:
        for i in range(2,p)
            if (p % i) == 0:
                numValid = True
                break
            else
                print("Please enter a prime number")
    else:
        print("Please enter a positive prime number")
    
numValid = False
while numValid == False:
    q = input("Enter q: A positive prime number")
    if q > 1:
        for i in range(2,q)
            if (q % i) == 0:
                numValid = True
                break
            else
                print("Please enter a prime number")
    else:
        print("Please enter a positive prime number")

n = p*q

numValid = False
while numValid == False:
    e = input("Enter e: your private key")
    if gcd(e,n) != 1:
        print("The inverse of this won't exist, hence RSA won't work. Enter a different number.")
    else:
        numValid = True

with open("keys.rsaconf","w") as keyfile:
    keyfile.write(n)
    keyfile.write(e)
