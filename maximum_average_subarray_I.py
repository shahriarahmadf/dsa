# 8-9 min

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        total = sum(nums[:k])
        max_total = total

        start = 0
        for pointer in range(k,len(nums)):
            total -= nums[start]
            start += 1
            total += nums[pointer]
            max_total = max(total,max_total)
        
        return max_total/k