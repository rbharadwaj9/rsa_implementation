print("a = b (mod n)")
b = int(input("Enter b "))
n = int(input("Enter n "))

def mod(b,n):
    lowerLevel = 1;
    while(b > 2):
        if b % 2 == 0:  #even
            lowerLevel = mod((b/2),n)
        else:  #odd
            lowerLevel = mod(((b-1)/2),n) * (b%n)
    modulus = (lowerLevel ** 2) % n
    return modulus

def main():
    mod(b,n)

if __name__ == '__main__':
    main()
