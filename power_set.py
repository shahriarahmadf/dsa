class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            result += [i + [num] for i in result]
        return result

class Solution2:
    def __init__(self):
        self.result = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result.append([])
        self.backtrack(nums)
        self.result.sort()
        return self.result

    def backtrack(self,nums):
        if not nums:
            return
        if nums not in self.result:
            self.result.append(nums)

        for i in range(0,len(nums)):
            self.backtrack(nums[:i] + nums[i+1:])