def findMaxAverage(arr, n, k):
        answer = []
        sum = 0
        i = 0
        ans = 0
        j = 0
        nums = arr
        while(i<=k-1):
                sum = (sum + nums[i]/k)
                i += 1
        temp = sum
        while(j < len(nums)-k):
            sum = sum - (nums[j]/k) + (nums[j+k]/k)
            j += 1
            if sum > temp:
                temp = sum
                ans = j
        for index in range(ans, ans+k):
            answer.append(arr[index])
        return (answer)
Arr= [1,12,-5,-6,50,3]
print(findMaxAverage(Arr,6,4))
    