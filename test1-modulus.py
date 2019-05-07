print("a = b (mod n)")
b = int(input("Enter b "))
n = int(input("Enter n "))

def mod(b,n):
    print("B is: ", b)
    lowerLevel = 1;
    while(b > n):
        if b % 2 == 0:  #even
            lowerLevel = mod((b/2),n)
        else:  #odd
            lowerLevel = mod(((b-1)/2),n) * (b%n)
    modulus = (lowerLevel ** 2) % n
    return modulus

def main():
    answer = mod(b,n)
    print(answer)

if __name__ == '__main__':
    main()
