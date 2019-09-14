import string

alphabets = dict(zip(string.ascii_lowercase, range(0, 26)))
print(alphabets)
with open('publickeys.rsaconf', 'r') as keyfile:
    n = int(keyfile.readline())
    e = int(keyfile.readline())

    message = input("Enter message to encrypt ")
    num_message = []
    encrypted_message = []
    for char in message:
        num_message.append(alphabets[char])
    for char in num_message:
        encrypted_char = char
        for i in range(1, e):
            encrypted_char = (encrypted_char*char) % n
        encrypted_message.append(encrypted_char)
    print(encrypted_message)
