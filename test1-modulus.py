import math

print("a = b (mod n)")
b = int(input("Enter b "))
n = int(input("Enter n "))


def mod(b, n):
    print("B is: ", b)
    lower_level = 1
    while(b > n):
        nearest_perfect_square = math.floor(b**(1/2))
        if (b ** (1/2)) == nearest_perfect_square:  # Perfect Square
            lower_level = mod(nearest_perfect_square, n)
        else:  # odd
            square_difference = b - nearest_perfect_square
            lower_level = mod(nearest_perfect_square, n) * \
                mod(square_difference, n)
    while (b > n):
        b = (b - n)
    return b


def main():
    answer = mod(b, n)
    print(answer)


if __name__ == '__main__':
    main()
