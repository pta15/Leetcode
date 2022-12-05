def pivotIndex(nums):
    i = 0
    for i in range(len(nums)):
        print("index is: ", nums[i])
        leftSum = sum(nums[:i])
        rightSum = sum(nums[i+1:])
        if leftSum == rightSum:
            return i
        i += 1
    return -1
        

nums = [1,5,2,4]
print(pivotIndex(nums))
