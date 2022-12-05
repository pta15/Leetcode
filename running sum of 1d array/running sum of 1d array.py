def oneDArr(nums):
    arr2 = []
    i = 0
    while i< len(nums):
        if i == 0:
            j = nums[i]
            arr2.append(j)
        else:
            j = nums[i] + j
            arr2.append(j)
        i += 1
    print(arr2)

def oneDArr2(nums):
    arr2 = []
    length = len(nums)
    i = 0
    total = 0
    for i in range(length):
        total += nums[i] 
        arr2.append(total)
        i += 1
    return arr2
    

nums1 = [1,2,3,5]
#oneDArr(nums1)
print(oneDArr2(nums1))
#print(arr1[0])
