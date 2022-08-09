
#Calculate number of days greater than average

no_of_days = int(input('enter no. of days :'))
total = 0
array_temp = []

for i in range(1, no_of_days+1):
    temp = int(input("day"+str(i)+'temp : ' ))
    array_temp.append(temp)
    total = total + temp
avg = total/no_of_days
print(array_temp)
number = 0
for i in array_temp:
    if i > avg:
        number = number+1
print('\n number of days having temp greater than '+ str(avg) + ' are : ' + str(number))
