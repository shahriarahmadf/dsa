class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        import math
        A_list = sorted(A) # converting tuple to array because tuple is immutable
        size = math.floor(len(A_list)/2)
        count = 0
        current = None

        for x in A_list:
            if current != x:
                current = x
                count = 1
            else:
                count += 1
            if count > size:
                return current

# leetcode another solution Time complexity O(n), space complexity O(n)
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        majority = max(freq, key = lambda key: freq[key])

        return majority
    
# another solution Time O(nlogn) 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        threshold = len(nums)/2

        current = None
        current_freq = 0
        for num in nums:
            if current != num:
                current = num
                current_freq = 1
            else:
                current_freq += 1

            if current_freq > threshold :
                return current        
        