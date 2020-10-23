#program for encryption
def encryption(sentence):
    trans = ''
    for x in sentence:
        char = ord(x)
        if char >= 97:
            char -= 96
        else:
            char -= 64
        trans += str(char) + ' '
    return trans

print(encryption(input("enter the value you want to encrypt ? : ")))
