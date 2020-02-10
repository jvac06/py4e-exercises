# class Solution:
from typing import List 

def pivotIndex(nums: List[int]) -> int:  #add self as parameter
    pSum = list()
    i = 0
    for num in nums:  #issue with range(len) is provding (0,6) output
        print("num is:", num)
        sum = 0
        sum += num
        print("sum is:", sum)
        pSum[i] = sum   #Use .append instead
        print(pSum)
        i+= 1
    for a in list(range(len(pSum))):
        leftP = pSum[c]
        rightP = pSum[len(pSum) - 1] - pSum[a] - nums[a]
        if leftP == rightP:
            return a
        else:
            return -1

nums = [1, 7, 3, 6, 5, 6]
pivotIndex(nums)