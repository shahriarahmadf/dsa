class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        total = -1e5
        total_max = -1e5

        for x in nums:
            if x > (total+x):
                total = x
            else:
                total += x
            if total>total_max:
                total_max=total
        return total_max

