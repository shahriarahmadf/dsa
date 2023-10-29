class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        nums[:] = [x for x in nums if x != val]

        return len(nums)
    
# another solution

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k