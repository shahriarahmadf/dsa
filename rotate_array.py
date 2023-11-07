class Solution:
    def reverse_array(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums

    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums = self.reverse_array(nums,0,len(nums)-1)
        nums = self.reverse_array(nums,0,k-1)
        nums = self.reverse_array(nums,k,len(nums)-1)
            
