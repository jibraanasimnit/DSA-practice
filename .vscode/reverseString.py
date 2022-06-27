def reverseString(string):
    return reverseString(str(string[len-1])) + reverseString(str(string[len-2]))
print(reverseString('abcdefgh'))


