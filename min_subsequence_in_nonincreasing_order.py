class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums.reverse()
        small_sum = sum(nums)
        large_sum = 0
        subsequence = []

        for num in nums:
            subsequence.append(num)
            large_sum += num
            small_sum -= num
            if large_sum > small_sum:
                break
            
        return subsequence

        