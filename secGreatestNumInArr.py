from cmath import inf


a = [1, 2, 3, 4, 5, 6, 7, 8, 11, 10]
searchedNum = -inf
secondLast = -inf
for element in a:
        if searchedNum < element:
            secondLast =   searchedNum
            searchedNum = element
        elif secondLast < element:
            secondLast = element
print(secondLast)