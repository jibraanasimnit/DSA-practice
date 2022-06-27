
rev = 0
def reverseNum(num):
    global rev
    if ( num>0 ):  
        remainder = num % 10  
        rev = (rev * 10) + remainder  
        reverseNum(num // 10)  
    return rev  
print(reverseNum(1))
