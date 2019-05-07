print("a = b (mod n)")
b = int(input("Enter b "))
n = int(input("Enter n "))

def mod(b,n):
    while(b != 1):
        if b % 2 == 0:  #even
            mod((b/2),n)
        else:i  #odd
            mod(((b-1)/2),n) * (b%n)
    return b   
