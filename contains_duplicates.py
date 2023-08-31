class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        count = {}
        
        for x in nums:
            if x in count:
                return True
            else:
                count[x] = 1
        return False
