# class Solution:
from typing import List 

def pivotIndex(nums: List[int]) -> int:  #add self as parameter
    pSum = list()
    sum = 0
    for num in nums:
        sum += num
        pSum.append(sum) 
    for i in list(range(len(pSum))):
        leftP = pSum[i] - nums[i]
        rightP = pSum[len(pSum) - 1] - pSum[i] 
        if leftP == rightP:
            return i
    return -1

nums = [1, 7, 3, 6, 5, 6]
pivotIndex(nums)