class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        rightSum = sum(nums)
        leftSum = 0
        for index,pivot in enumerate(nums):
            
            rightSum -= pivot
            print(leftSum,rightSum)
            if leftSum == rightSum:
                return index
            leftSum += pivot
        return -1
