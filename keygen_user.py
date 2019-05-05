import math
import sys
from fractions import gcd

while True:
    p = int(input("Enter p: A positive prime number "))
    if p > 1:
        for i in range(2,p):
            if (p % i) == 0:
                print("Please enter a prime number")
                break
        else:
            break
    else:
        print("Please enter a positive prime number")
    
while True:
    q = int(input("Enter q: A positive prime number "))
    if q > 1:
        for i in range(2,q):
            if (q % i) == 0:
                print("Please enter a prime number")
                break
        else:
            break
    else:
        print("Please enter a positive prime number")

n = p*q

while True:
    e = int(input("Enter e: your private key "))
    if gcd(e,n) != 1:
        print("The inverse of this won't exist, hence RSA won't work. Enter a different number.")
    else:
        break
#Calculate d with d = e^-1 mod(p-1)(q-1)
d= 11

with open("privatekeys.rsaconf","w") as keyfile:
    keyfile.write(str(p))
    keyfile.write(str(q))
    keyfile.write(str(n))
    keyfile.write(str(e))
    keyfile.write(str(d))

with open("publickeys.rsaconf","w") as keyfile:
    keyfile.write(str(n))
    keyfile.write(str(e))
